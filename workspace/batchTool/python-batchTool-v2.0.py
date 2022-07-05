"""
	log:
	2022.03=>
			初版功能
			initFilePathDict(self)		# 初始化目标文件字典
			findSameFile(self)			# 找到相同的文件
			showAfileMd5(self,file)		# 显示一个文件md5值
			changeAFileMd5(self,file)	# 修改一个文件md5值,通过向文件未添加一个字符串来改变md5值
			changeMd5(self)				# 批量修改md5值
			addExt(self,ext=".mp4")		# 批量给文件添加后缀名，默认为.mp4
			subString(self,string="")	# 批量删除文件中的指定字符串

	批处理工具:批量修改某一目录及其子目录下的文件
"""
import os,shutil,re,random,argparse,hashlib
class Hanime1MeTool():
	def __init__(self,srcPath):
		self.srcPath = srcPath	# 目标文件夹
		self.filePathDict = dict()	# 目标文件字典{"文件名filename":文件路径filepath}
		# 调用函数
		self.initFilePathDict()	# 初始化目标文件字典
		# self.findSameFile()		# 手动去掉重复文件
	
	def initFilePathDict(self):		# 初始化目标文件字典
		for root,dirs,files in os.walk(self.srcPath):
			for file in files:
				if file not in self.filePathDict.keys():	# 文件名不在字典中
					self.filePathDict[file] = root		# 添加加到字典中
				else:									# 文件名在字典中
					self.filePathDict[file] = self.filePathDict[file] + ">" + root			# 路径之间使用“>”链接，文件名、路径中不能含有“>”

	def findSameFile(self):		# 找到相同的文件
		flag = False			# 标记是否需要手动去重
		for file in self.filePathDict.keys():
			path  = self.filePathDict[file]
			if ">" in path:		# 打印出同名文件的信息
				print("多个同名文件：",file)
				for filepath in path.split(">"):
					print("\t路径：",filepath)
				flag = True
		if flag==True:
			print("请手动对文件去重后，再运行本程序。。。")
			os.system("pause")
			os.system("break")
		if flag == False:
			print("无重复文件。。。")

	def showAfileMd5(self,file):	# 显示一个文件md5值
		md5Value = str()
		if os.path.exists(file):
			with open(file, 'rb') as f:
				md5 = hashlib.md5()
			while True:
				buffer = f.read(4096)
				if not buffer:
					break
				md5.update(buffer)
			md5Value = md5.hexdigest()
		return md5Value

	def changeAFileMd5(self,file):	# 修改一个文件md5值,通过向文件未添加一个字符串来改变md5值
		try:
			characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
			random_str = ''.join(random.choice(characters))
			with open(file, 'ab') as f:
				f.write(random_str.encode('utf-8'))
			print("md5 changed...")
		except:
			pass

	def changeMd5(self):	# 批量修改md5值
		for file in self.filePathDict.keys():
			path  = self.filePathDict[file]		# 遍历文件
			print(file)
			self.changeAFileMd5(file=os.path.join(path,file))	# 修改md5

	def addExt(self,ext=".mp4"):	# 批量给文件添加后缀名，默认为.mp4
		for file in self.filePathDict.keys():
			path = self.filePathDict[file]
			old = os.path.join(path,file)
			new = os.path.join(path,file+ext)
			shutil.move(old,new)
			print("addExt...---->",new)

	def subString(self,string=""):	# 批量删除文件中的指定字符串
		for file in self.filePathDict.keys():
			path = self.filePathDict[file]
			old = os.path.join(path,file)
			new = os.path.join(path,re.sub(r""+string,"",file))
			shutil.move(old,new)
			print("subString...---->",new)

	def classFile(self,dirNum=0):	# 创建dirNum个文件夹，按照dirNum的个数给文件分组到不同的文件夹	
		pass

if __name__ == "__main__":
	srcPath = "D:/entertain/video/cos"
	obj = Hanime1MeTool(srcPath=srcPath)
	obj.changeMd5()
	