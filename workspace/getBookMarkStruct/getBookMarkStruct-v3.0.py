"""
	log:
		2022.01.07-23:58     simpleHtml函数---->修改文件夹缩进错误
			 在线工具 ----- 2
                 小书签 ----- 4
	         工具 ----- 2
	                 阅读 ----- 4
"""


"""
	本版本根据v2.0进行改进,根据用户所输入的目录结构来寻找目标书签；
	而非同v2.0一样先获取所有结构后在进行筛选
"""


"""
	特别注意:
		python无法直接匹配"制表符(\t)",“只能用四个空格(" "*4)
	说明:
		本项目使用pc版firefox浏览器导出的书签进行操作
		1.本项目提取书签结构流程:
			简化书签(剔除不必要的参数)-->按照标签获取书签结构
			根据正则来匹配文件夹,书签标题、书签url
		2.本项目中的书签结构:
			dirRoot(根目录)
				|-dirNO01-01(第一层第01文件夹)
					|-dirNO02-01(第二层第01文件夹)
					|	|-bmline01(书签行01)
					|	|-bmline02(书签行02)
					|-dirNO02-02(第二层第02文件夹)
					|	|-bmline03(书签行03)
					|—bmline04(书签行04)
					|-bmline05(书签行05)
					...
				|-dirNO01-02(第一层第02文件夹)
					...
		3.本项目中书签结构的字典(bmdict)结构:
			dirRoot = 
				{
					deep:00,
					sondir:{dirNO01-01:01,dirNO01-02:01,},
					directbm:{
						bmTitle06:bmUrl06,
						bmTitle07:bmUrl07,
						...
					},
					dirNO01-01:{
						deep:01,
						sondir:{
							dirNO02-01:02,
							dirNO02-02:02,
							...
						},
					},
					dirNO01-02:{
						deep:01,
						sondir:{
							sondir03:sondir03deep,
							sondir04:sondir04deep,
							sondir05:sondir05deep,
							...
						},
					},
					dirNO02-01:{
						deep:02,
						sondir:{},
						directbm:{
							bmTitle01:bmUrl01,
							bmTitle02:bmUrl02,
							...
						},
					},
					dirNO02-02:{
						deep:02
						sondir:{},
						directbm:{
							bmTitle03:bmUrl03,
							bmTitle04:bmUrl04,
							bmTitle05:bmUrl05,
							...
						},
					},
				}
			简化:
				dirdict = 
					{
						# deep:深度;dirdeep:文件夹所在的“绝对深度”;每个书签字典必须要有该属性
						deep:dirdeep,
						# sondir:文件夹下的第一级子文件夹;sondirName:子文件夹名;sondirDeep:子文件夹的“绝对深度”;每个书签字典必须要有该属性,可以为空
						sondir:{sondirName:sondirDeep,...},
						# directbm:直接存放在当前文件夹下的书签;bmTitle:书签标题;bmUrl:书签的url地址;每个书签字典必须要有该属性,可以为空
						directbm:{bmTitle:bmUrl,...}
						# 深度为01的子文件夹
						dir01{deep:01,sondir:...,directbm:....},
						...
						# 深度为02的子文件夹
						dir02{deep:02,sondir:...,directbm:....},
						...
						# 深度为03的子文件夹
						dir03{deep:03,sondir:...,directbm:....},
						...
					}
			书签提取主要提取bmTitle和bmUrl		   
		4.本项目的一些函数及变量:
			变量:
				dirRoot:书签根目录
				srcbmfile:源书签路径
				simplehtmlstring:简化后的书签字符串
				bmdict:书签字典,包含所有不同深度的文件夹，书签
				bmline:书签行,包含bmTitle和bmUrl
			函数:
				# 1)简化书签,htmlfile：源书签路径；返回简化后字符串
				simpleHtml(htmlfile)	
				# 2)获取书签文件夹的深度，返回一个字典，格式{mindeep:,maxdeep:}
				getBmDeep(htmlstring)	
				# 3)获取书签结构的字典，返回一个字典bmdict
				getBmStruct(bmdeep)		
				# 4)过滤书签字典，获取相应的文件夹，返回一个书签字典bmdict
				# bmdict:书签字典，“可以是最高级的父文件夹，也可以是子文件夹”
				# bmdeep:“根据文件夹的深度”获取文件夹及其下的所有书签，bmdeep=-1默认获取所有文件夹
				# bmdirkw:“根据文件夹的关键字”来获取文件夹及其下的所有书签，bmdirkw=str()默认获取所有文件夹
				# 首选“根据文件夹关键字”获取文件夹
				filerBmDir(bmdict,bmdirkw=str(),bmdeep=-1)	
"""
import re,os

class getBmStruct():
	# 初始化函数
	def __init__(self,srcbmfile,aimdirpath=str()):
		self.srcbmfile = srcbmfile 									# 源书签文件路径
		self.aimdirpath = aimdirpath								# 目标文件夹路径,格式"/root/tec/sw"
		self.mindirdeep = 1 										# 简化后，每行前都至少有一个制表符
		self.tulinkflag = "===}"									# bmTitle与bmurl之间连接形式
		self.htmlstring = self.simpleHtml(htmlfile = self.srcbmfile)		# 简化后的html字符串

	def getlinedeep(self,line):	# 获取一行的深度,最低为1
		deep = 0
		while not (line.startswith(" "*4*deep) and not line.startswith(" "*4*(deep+1))):
			deep += 1
		return deep

	def isbmdir(self,line):	# 判断是否为书签文件夹
		if (not self.tulinkflag in line) and len(line)>0 and (not "javascript" in line):
			return True
		return False

	def findalldir(self):			# 匹配所有的文件夹及深度
		maxdeep = 0		# 最大深度，根据缩进"\t"获取书签的层数
		mindeep = 0 	# 基准深度
		htmlstringlist = self.htmlstring.split("\n")		# 按行分割后的字典
		alldirdeepdict = dict()			# 返回的字典
		for linecontent in htmlstringlist: # 先遍历内容会有错
			dirdeep = self.getlinedeep(linecontent)
			# 判断是否为书签行
			if self.isbmdir(linecontent):	
				dirname = linecontent.lstrip(" "*4*dirdeep)
				alldirdeepdict[dirname] = dirdeep
		return alldirdeepdict

	# 1)简化书签,htmlfile：源书签路径；返回简化后字符串
	def simpleHtml(self,htmlfile):
		simplehtmlstring = str()
		with open(srcbmfile,"r",encoding="utf-8") as readfile:
			simplehtmlstring = readfile.read()
		simplehtmlstring = re.sub(pattern = r"ADD_DATE=\".*\"", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"LAST_MODIFIED=\".*\"", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"ICON=\"(.*)\"", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<DT>(.*)about:blank</A>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<DL><p>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"</DL><p>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<DT><H3 >", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"</H3>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<DT><A HREF=\"", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"</A>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<[^>]+>.*<[^>]+>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"<[^>]+>", repl = '', string = simplehtmlstring)
		simplehtmlstring = re.sub(pattern = r"\"( *)>", repl = self.tulinkflag, string = simplehtmlstring)
		simplehtmlstringlist = simplehtmlstring.split("\n")
		simplehtmlstring = str()
		for line in simplehtmlstringlist:
			if not line.isspace() and line!="" and len(line)>1:
				simplehtmlstring += line + "\n"
		# 修改缩进错误
		tempsavelinelist = list()
		nowlinedeep = 0 
		nextlinedeep = 0
		for i in range(len(simplehtmlstringlist)-1):
			nowline = simplehtmlstringlist[i]
			nextline = simplehtmlstringlist[i+1]
			nowlinedeep = self.getlinedeep(nextline)
			nextlinedeep = self.getlinedeep(nextline)
			if nowlinedeep-nextlinedeep > 1:
				dif = nowlinedeep+1
				nextline = " "*4*dif+nextline.lstrip(" ")
				simplehtmlstringlist[i+1] = nextline
		# pass
		return simplehtmlstring

	# 2)获取目标文件夹下的所有文件夹及书签
	def getBmStruct(self):
		bmdict = {
			"dirname":self.aimdirpath,
			"dirdeep":-1,
			"sondir":{},
			"sonbm":{},
		}
		htmlsplitlist = self.htmlstring.split("\n")		# 书签文件内容的按行分割
		aimpathlist = [i for i in self.aimdirpath.split("/")if len(i)>0]	# 把目标路径分割
		aimhtmlstringlist = list()

		return bmdict

	
	

if __name__=="__main__":
	srcbmfile = "./bm-firefox-2022.01.03.html"
	gbms = getBmStruct(srcbmfile=srcbmfile,aimdirpath="/root/singin")
	with open("simplebm.txt","w",encoding="utf-8") as writefile:
		writefile.write(gbms.htmlstring)

	# alldirdict = gbms.findalldir()
	# for i in alldirdict.keys():
	# 	print(" "*4*alldirdict[i],i,"-----",alldirdict[i])

	ts = " "*4*3+"aaa"
	print(ts.lstrip(" "))