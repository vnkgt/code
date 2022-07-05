"""
    开发环境:
        python3
            pillow包
            playsound包
            numpy包
        ffmpeg软件
    字符动画:
        class AsciiAnimation
        0.主控函数  run
        1.视频信息初始化   __init__
        其它:
            清屏命令:clean_command(windows:"cls" ubuntu:"clean")
        视频相关:
            视频地址:video_path
            视频所在的文件夹:video_dir
            视频的名字:video_name
            视频的后缀名:video_name_ext
            视频帧率:video_fps
        视频生成图片相关属性:
            图片所在文件夹:img_dir(文件夹名:video_name+"_video2img_dir")
            图片大小:img_width(宽度),img_height(高度)
            图片名:img_name(video_name+"_img_数字".jpg")
        图片生成字符文本相关:
            亮度替换列表:art_word
            字符文本所在文件夹:imgtext_dir(文件夹名:video_name+"_img2imgtext_dir")
            字符文本名:imgtext_name(文本名称格式:video_name+"_imgtext_数字" #无后缀名)
        图片生成字符图片相关:
            亮度替换列表:art_word
            字符画所在的文件夹:textimg_dir(文件夹名:video_name+"_img2textimg_dir")
            字符画ming:textimg_name(字符画名:video_name+"_textimg_数字.jpg")
        bgm相关:
            bgm名:bgm_name(名称格式:video_name+"_bgm.mp3")
            bgm地址:bgm_path(格式:video_dir+"/"+bgm_name)
        字符图片+bgm合成视频相关:
            字符视频名:textvideo_name(格式:video_name+"_text"+video_ext)
            字符视频地址:textvideo_path(格式:video_dir+"/"+textvideo)
        2.视频转换为图片   video2img
        3.图片转换为字符文本 img2imgtext
        4.图片转换为字符图片 img2textimg
        5.提取视频bgm      get_bgm
        6.按原帧率将字符图片合成字符视频   textimg2video
        7.播放字符视频    display_video
        8.直接打印播放图片字符文本  display_imgtext
        9.浏览器传输字符动画class NetAsciiAnimation
            1)创建监听套件字__init__
            2)获取客户端套件字get_client
            3)开启一个线程给浏览器传递字符server2client
"""


import os   #文件夹处理
import shutil
from PIL import Image,ImageDraw   #图片处理
import numpy        #图片处理
from playsound import playsound #播放音频
import threading
import time

class AsciiAnimation():
    def __init__(self,videoPath,flag=0):   #1初始化
        #其它
        self.flag = flag #是否删除现有的所有文件夹;0:删除;其它:不删除
        self.clean_command = "cls"  #清屏命令
        self.num = 6
        self.number_formant = "%{num}d".format(num = self.num)  #ffmpeg转换文件名中数字格式
        self.number_read_formant = "%0.{num}d".format(num = self.num)
        #视频相关
        self.video_path = os.path.abspath(videoPath) #视频绝对路径
        self.video_dir = os.path.dirname(self.video_path)   #视频所在文件夹
        self.video_name,self.video_name_ext = os.path.splitext(os.path.split(self.video_path)[1])   #视频名称,视频后缀名
        self.video_fps = 30     #视频帧率
        #视频生成图片相关
        self.img_dir = os.path.join(self.video_dir,self.video_name+"video2img_dir") #图片文件夹
        self.img_name = self.video_name + "_img_{index}.jpg" #图片名格式
        self.img_path = os.path.join(self.img_dir,self.img_name.format(index=self.number_read_formant))  #图片路径模板格式
        self.img_num = 0    #图片张数
        all_img_list = list(os.walk(self.img_dir))  # 遍历图片字符文件夹
        for root, dirs, files in all_img_list:
            for file in files:
                self.img_num += 1
        #图片生成字符文本相关
        self.art_word = " .,;]}0w%#@"  #字符替换列表
        self.imgtext_dir = os.path.join(self.video_dir,self.video_name+"_img2imgtext_dir")  #所有文本所在的文件夹
        self.imgtext_name = self.video_name + "_imgtext_{index}.txt"   #文本文件名格式
        self.imgtext_path = os.path.join(self.imgtext_dir,self.imgtext_name.format(index=self.number_read_formant))    #图片文本路径模板格式
        self.img_size = 130  # 截取图片的宽度
        # self.img_height = self.img_width // 3  # 截取图片的高度
        self.light_level = 255  #一个像素的最高亮度
        #图片生成字符图片相关
        self.textimg_dir = os.path.join(self.video_dir,self.video_name+"_img2textimg_dir")  #所有字符图片所在的文件夹
        self.textimg_name = self.video_name + "_textimg_{index}.jpg"    #文本图片名格式
        self.textimg_path = os.path.join(self.textimg_dir,self.textimg_name.format(index=self.number_read_formant))    #文本图片路径模板格式
        self.textimg_font = "./msyhbd.ttc"  #字符图片字体地址
        self.font_size = 14 #字符图片中字体的大小
        self.draw_size = (self.img_size*6,(self.img_size//3)*15) #画字符画的画布大小
        #bgm相关
        self.bgm_name = self.video_name + "_bgm.mp3"    #bgm名
        self.bgm_path = os.path.join(self.video_dir,self.bgm_name)  #bgm路径
        #字符图片合成视频相关
        self.textvideo_name = self.video_name + "_text"+self.video_name_ext  #字符视频名
        self.textvideo_path = os.path.join(self.video_dir,self.textvideo_name)  #字符视频路径

    def video2img(self):    #2视频转图片
        img_name = self.img_name.format(index=self.number_formant)
        img_save_path = os.path.join(self.img_dir,img_name)
        video2img_command = 'ffmpeg -i {videopath} -r {fps} {imgpath}'  # 视频转图片命令
        video2img_command = video2img_command.format(videopath=self.video_path,fps=self.video_fps,imgpath=img_save_path)
        os.system(video2img_command)

    def img2imgtext(self):  #3图片转字符文本
        countor = 1
        while countor<=self.img_num:
            imgpath = self.img_path % countor
            txt_path = self.imgtext_path % countor
            img = Image.open(imgpath).convert('L')  # 打开图片并转换灰度
            img = img.resize((self.img_size, self.img_size // 3))  # 修改图片大小
            data = numpy.array(img)[:self.img_size//3, :self.img_size]  # 保存图片信息数组
            with open(txt_path, 'w', encoding='utf-8') as f:  # 写入输出文件
                for row in data:
                    for pixel in row:
                        # 将像素亮度与对应的字符对应(根据slef.art_word的列表长度替换)
                        # pixel:图片中像素亮度      light_level:最亮像素的亮度     art_word:与亮度对应的字符列表
                        pixel_word_index = pixel // (self.light_level // len(self.art_word) + 1)
                        f.write(self.art_word[pixel_word_index])
                    f.write('\n')
                f.close()
            countor += 1
            print("finish transforming {0}====>{1}".format(imgpath,txt_path))
        print("Finish img2imgtext!!!")

    def img2textimg(self):  #4图片转字符图片
        countor = 1
        while countor<=self.img_num:
            origin_img_path = self.img_path % countor   #原图片路径
            textimg_path = self.textimg_path % countor  #字符图片路径
            cav = Image.new(mode="RGB",size=self.draw_size,color="black")   #创建新画布
            textimg = ImageDraw.Draw(im=cav,mode=None)  #创建画布对象
            img = Image.open(origin_img_path).convert('L')  # 打开原图片并转换灰度
            img = img.resize((self.img_size, self.img_size // 3))  # 修改原图片大小
            img_data = numpy.array(img)[:self.img_size // 3, :self.img_size]  # 保存原图片信息数组
            cav_word = str()    #写入画布对象的字符串
            for row in img_data:
                for pixel in row:
                    # 将像素亮度与对应的字符对应(根据slef.art_word的列表长度替换)
                    # pixel:图片中像素亮度      light_level:最亮像素的亮度     art_word:与亮度对应的字符列表
                    pixel_word_index = pixel // (self.light_level // len(self.art_word) + 1)
                    cav_word += self.art_word[pixel_word_index]
                cav_word += "\n"
            textimg.text(xy=(0,0),text=cav_word,fill=(255,255,255),font=None)# 参数：位置、文本、填充、字体
            cav.save(textimg_path)  #保存字符图片
            countor+=1
            print("finish transforming {0}====>{1}".format(origin_img_path,textimg_path))
        print("Finsh img2textimg!!!")


    def get_bgm(self):  #5提取bgm
        video_get_bgm_command = 'ffmpeg -i {videopath} -f mp3 {bgmpath}'
        video_get_bgm_command = video_get_bgm_command.format(videopath=self.video_path,bgmpath=self.bgm_path)
        os.system(video_get_bgm_command)

    def textimg2video(self):    #6bgm_字符图片按帧率转换为视频
        #fps:帧率 textimgpath:字符图片地址 bgmpath:bgm地址 outvideopath:视频输出地址
        textimg2video_command = 'ffmpeg -r {fps} -i {textimgpath} -i {bgmpath} -s 1920x1080 {outvideopath}'.format(fps = self.video_fps,textimgpath=os.path.join(self.textimg_dir,self.textimg_name.format(index=self.number_formant)),bgmpath=self.bgm_path,outvideopath=self.textvideo_path)
        os.system(textimg2video_command)


    def display_video(self):    #7播放视频
        display_command = f"ffplay -i {videopath}".format(videopath=self.textvideo_path)
        os.system(display_command)

    def display_imgtext(self):  #8直接打印字符文本
        def dispaly_music():
            if os.path.exists(self.bgm_path):
                playsound(self.bgm_path)
        all_img_list = list(os.walk(self.img_dir))  # 遍历图片字符文件夹
        file_num = 0
        for root, dirs, files in all_img_list:  #获取文件的个数
            file_num += len(files)
            file_num += len(files)
        bgm_display = threading.Thread(target=dispaly_music)
        bgm_display.start() #播放bgm
        countor = 0
        while countor<file_num-1:
            if countor%(self.video_fps//10)==0:
                os.system(self.clean_command)
                txt_path = self.imgtext_path % (countor+1)
                with open(txt_path,"r") as f:
                    print(f.read())
                    f.close()
                time.sleep(round(1/self.video_fps,2))
            countor += 1

if __name__=="__main__":
    videopath = "./op.mp4"
    a = AsciiAnimation(videopath)
    a.video2img()
    a.img2imgtext()
    a.img2textimg()
    a.get_bgm()
    a.textimg2video()
    a.display_imgtext()