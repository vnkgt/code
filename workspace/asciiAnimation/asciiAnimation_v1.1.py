# encoding = utf-8
# author: github@vnkgt
# last edit time: 2021.08.20.22:22
"""
开发环境:
	Pillow
	numpy
	软件:
		ffmpeg
变量:
	mainDir:视频所在的文件夹
	videoPath:视频路径(含文件名)
	videoName:视频名
	bgmPath:bgm路径(含文件名)
	bgmName:videoName.mp3
	imgDir:视频转图片文件夹(默认为黑白)
		图片格式:
			videoPath/imgDir/videoName-%0.6d.jpg
	textDir:图片转换文本文件夹
		文本格式:
			videoPath/textDir/videoName-%0.6d.txt
	textimgDir:图片转字符图片文件夹
		字符图片格式:
			video/textimgDir/videoName-%0.6d.jpg
	textimg2videoPath:
		文件格式:
			videoPath/videoName-out.mp4
函数:
	video2img(videoPath,outputDir)视频转图片
	img2text(imgDir,)
"""
import os,shutil,re
import numpy
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont
import matplotlib.pyplot as plt

class AsciiAnimation():
	# videoPath:视频路径 delmiddle:是否删除以前的中间文件 ffmpeg:ffmpeg命令路径(默认ffmpeg已经添加到PATH环境变量)
	def __init__(self, videoPath, delmiddle = True, ffmpeg = "ffmpeg"):
		# 文件参数
		# 视频路径
		self.videoPath = videoPath
		# 视频所在文件夹
		self.mainDir = os.path.dirname(os.path.abspath(self.videoPath))
		# 视频文件名
		self.videoName = os.path.splitext(os.path.split(self.videoPath)[1])[0]
		# 输出视频文件路径
		self.outputVideoPath = os.path.join(self.mainDir,self.videoName+"-out.mp4")
		# bgm名
		self.bgmName =  self.videoName + "-bgm.mp3"
		# bgm路径
		self.bgmPath = os.path.join(self.mainDir,self.bgmName)
		# 文件后缀数字的长度(视频长会生成更多的图片，需要更长位数的数字后缀)
		self.fileAddNumLen = 6
		# img文件夹,文件格式及路径
		self.imgDir = os.path.join(self.mainDir,self.videoName+"-imgDir")
		self.imgFile = os.path.join(self.imgDir,self.videoName+"-%{0}d.jpg".format(self.fileAddNumLen))
		# img2text图片转文本文件夹,文件格式及路径
		# self.textDir = os.path.join(self.mainDir,self.videoName+"-textDir")
		# self.textFile = os.path.join(self.textDir,self.videoName+"-%{0}d.txt".format(self.fileAddNumLen))
		# img2textimg图片转字符图片文件夹格式及路径
		self.textimgDir = os.path.join(self.mainDir,self.videoName+"-textimgDir")
		self.textimgFile = os.path.join(self.textimgDir,self.videoName+"-%{0}d.jpg".format(self.fileAddNumLen))
		# 所有中间文件,文件夹列表
		self.middleDirList = [self.imgDir,self.textimgDir,]
		self.middleFileList = [self.bgmPath]
		if delmiddle == True:
			for d in self.middleDirList:
				if os.path.exists(d):
					shutil.rmtree(d)
					os.mkdir(d)
				else:
					os.mkdir(d)
			for f in self.middleFileList:
				if os.path.exists(f):
					os.remove(f)
			print("msg--->have del middle file and dirs")
		# ffmpeg参数
		# ffmpeg命令路径
		self.ffmpeg = ffmpeg
		# 视频转图片时的帧率
		self.ffmpegfps = 30
		print("msg--->init over")
		# 图片转字符图转字符文件参数
		# 对应亮度对应的字符
		self.asciiWord = list("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;,.*@-+#$%^")  # 字符列表
		# 字符长度
		self.asciiWordLen = len(self.asciiWord)
		# 新图片大小(width,height)
		self.resize = (100,120)

	# 主控函数
	def run(self, color=(0,255,255)):	# 默认绿色字符串
		# 视频转图片
		self.video2img()
		# 获取bgm
		self.getbgm()
		# 图片转字符图片
		for root,dirs,files in os.walk(self.imgDir):
			for file in files:
				self.img2textimg(inputImg=os.path.join(self.imgDir,file), outputImg=os.path.join(self.textimgDir,file), fontcolor=color)
		# 字符图片转视频
		self.img2video()
	# 提取bgm
	def getbgm(self):
		ffmpegCommand = "{ffmpeg} -i \"{videoPath}\" \"{bgmPath}\"".format(ffmpeg = self.ffmpeg, videoPath = self.videoPath, bgmPath = self.bgmPath)
		os.system(ffmpegCommand)

	# 视频转图片
	def video2img(self):
		ffmpegCommand = "{ffmpeg} -i \"{videoPath}\" -r {fps} \"{imgFile}\"".format(ffmpeg = self.ffmpeg, videoPath = self.videoPath, fps = self.ffmpegfps, imgFile = self.imgFile)
		os.system(ffmpegCommand)
	

	# 一张图片转黑白文本图片;color:输出图片中字符的颜色;inputImg:输入文件;outputImg:输出文件
	def img2textimg(self,inputImg,outputImg,fontcolor):
		# 输出的所有文字
		outputString = str()
		# 打开图片
		img = Image.open(inputImg)
		# 修改图片尺寸
		img = img.resize((self.resize[0],self.resize[1]//3))
		# 获取图片尺寸(width,height)
		imgsize = img.size
		# 创建新图片,黑色背景
		# 新图片背景的颜色
		cav = Image.new(mode="RGB",size=(self.resize[0]*6,self.resize[1]*5),color = "black")   
		# 在新图片中创建画布对象
		drawcav = ImageDraw.Draw(im=cav,mode=None)
		for row in range(0,imgsize[1]):		# row相当于y
			for line in range(0,imgsize[0]):	# line相当与x
				# 获取(row,line)处的像素
				pixel = img.getpixel(xy=(line,row))
				# 转为灰度
				r = pixel[0]
				g = pixel[1]
				b = pixel[2]
				gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
				# 将灰度对应字符列表中的字符,获取其对应的字符
				unit = (256+1)/len(self.asciiWord)	# 最高亮度为256,亮度对应字符
				getword = self.asciiWord[int(gray/unit)] # (gray/(256+1))*len(),灰度对应列表长度的“几分之几处”
				outputString += getword
			# 换行加空格
			getword = "\n"
			outputString += getword
			# 字符写入画布,参数：位置、文本、填充颜色、字体
		drawcav.text(xy=(0,0),text=outputString,fill=fontcolor,font=None)
		# plt.figure("badapple")
		# plt.imshow(cav)
		# plt.show()
		# 保存图片
		cav.save(outputImg)	
		print(inputImg,"----->",outputImg)

	# 图片转视频(默认转黑白字符画)
	def img2video(self):
		ffmpegCommand = "{ffmpeg} -r {fps} -i \"{textimgFile}\" -i \"{bgm}\" -s 1920x1080 \"{outputVideo}\"".format(ffmpeg=self.ffmpeg,fps=self.ffmpegfps,textimgFile=self.textimgFile,bgm=self.bgmPath,outputVideo=self.outputVideoPath)
		# print(ffmpegCommand)
		os.system(ffmpegCommand)

if __name__ == "__main__":
	a = AsciiAnimation("./op.mp4",delmiddle=True)
	a.run()