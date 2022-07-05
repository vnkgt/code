"""
	说明:
		本项目是基于缩进、html每行进行正则匹配实现的,特别注意:
			1)".html"读写时的编码解码
			2)".html"读取时用readlines(),可以直接生成由每行组成的一个列表
			3)注意缩进问题,本项目通过缩进匹配确定书签文件夹内容,读文件不成功时可多次尝试不同的“tabNum参数”
			4)本项目值使用chrome导出的书签进行过测试,其它浏览器导出的书签请自行尝试
		书签结构:
			根目录(mainFloder)							# level = 0,目录等级0
				|-书签行(bmLine01)						#	level = 1,目录等级1
				|-书签行(bmline02)						#	level = 1,目录等级1
				|-文件夹(folder01)						#	level = 1,目录等级1
				|-文件夹(folder02)						#	level = 1,目录等级1
					|-子文件(sonFolder01)			#	level = 2,目录等级2
					|-子文件(sonFolder02)			#	level = 2,目录等级2
					|-书签行(bmLine01)					#	level = 2,目录等级2
					|-书签行(bmLine02)					#	level = 2,目录等级2
					|-书签行(bmLine03)					#	level = 2,目录等级2
			整个html:mainFolder
			文件夹名:folderName
			文件夹下包含所有的文件,文件夹:folderContent
			书签行包含的所有内容(a标签):lineContent
			书签行:url:网站
						title:标签名
		".html"文件操作注意事项:
			1)
				htmlfile.read().decode("utf-8")				# 读取内容后解码
				htmlfile.write(content.encode("utf-8"))		# 写入文件前编码
			2)直接使用readlines()函数生成列表
		函数:
			getFolder()			# folderContentLines:每行组成的列表,获取文件夹下文件夹,返回字典{"folderName":"folderContent"}
			getLines()			# 获取文件夹中所有书签行的内容,返回{"title":"url"}
			formatLines()		# 清除title中的"xxx-xxx-xxx-xxx"格式
			simpleHTML()		# 简化".html"文件内容
"""

import os,shutil,re
import requests

# 修改一个bookmark,path:html文件路径,addext:生成的新html
def simpleHTML(oldfilepath,newfilepath,addext=str()):
	inputfile = oldfilepath
	outputfile = newfilepath
	with open(inputfile,"br") as bmrfile:
		with open(outputfile,"w",encoding="utf-8") as bmwfile:
			# 读取操作每行
			lineContent = bmrfile.read().decode("utf-8")						# 文本每行组成的列表
			# 删除ICON参数
			result = re.sub(pattern = r"ICON=\"(.*)\"", repl = '', string = lineContent)
			# 删除ADD_DATE参数
			result = re.sub(r"ADD_DATE=\"(.*)\"",'',result)
			# 删除第一个(count=1)"<DT><H3>书签栏</H3>"标签
			result = re.sub(r"<DT>(.*)书签栏</H3>", '', result , count = 1)
			# 删除about:blank标签
			result = re.sub(r"<DT>(.*)about:blank</A>",'',result)
			# 删除小括号说明
			result = re.sub(r"\((.*)\)","",result)
			# 删除画括号说明
			result = re.sub(r"\{(.*)\}","",result)
			# 写入输出文件
			bmwfile.write(result)
			print("simpleHTML finish----->",outputfile)

# 获取文件夹下文件夹,根据<DL><p>标签前"\t"的多少判断级别,只获取一层,不能获取直接放在,可已反复调用,一级一级获取文件夹
def getFolder(floderContentLines = list(),tabNum = 0):
	outputdict = dict()	#	返回的字典
	outputdict["tabNum"] = tabNum	# 标注当前字典的等级
	dircontent = list()	#	放在文件夹的书签行
	flag = False	# 判断书签行是否要添加到dircontent
	folderName =  str()
	for line in floderContentLines:
		head = re.match(r"{0}<DT><H3(.*)>(.*)</H3>(.*)".format(" "*4*(tabNum+1)),line)	#	目录开头
		end = re.match(r"{0}</DL><p>".format(" "*4*(tabNum+1)),line)	# 目录结尾
		if head!=None:	#	开始添加
			flag = True
			folderName = head.group(2)
		if end!=None:		#	添加结束,重置标识,清空变量
			flag = False
			outputdict[folderName] = dircontent
			dircontent = list()
		if flag == True:	#	添加标志为真
			dircontent.append(line)
	return outputdict

# 获取一个文件夹下的所有书签行,包括子目录的书签行
def getLines(folderName = list()):
	outputdict = dict()
	for line in folderName:
		linematch = re.match(r"(.*)<DT><A HREF=\"(.*)\"(.*)>(.*)</A>",line)
		if linematch!=None:
			url = linematch.group(2)
			title = linematch.group(4)
			outputdict[title] = url
	return outputdict

# 清除title中的"xxx-xxx-xxx-xxx"格式
def formatLines(linesList = dict(),bmLineFormat=str()):
	outputdict = dict()
	for title in list(linesList.keys()):
		url = linesList[title]	# 获取url
		newtitle = re.sub(r"%s"%bmLineFormat,"",title) # 修改title
		outputdict[newtitle] = url
	return outputdict

# 获取某格式的开头标签行,eg:"1.1.1tool-pic-"开头
def getFormatHeadLines(linesList = dict(),formatHead = str()):
	outputdict = dict()
	for title in list(linesList.keys()):
		if formatHead in title:
			url = linesList[title]	# 获取url
			outputdict[title] = url
	return outputdict


if __name__ == "__main__":
	# 写路径时必须用"/"
	filepath = "./bookmark_2021.09.17.html"					# 源文件
	simpleHTMLPath = "./bookmark_2021.09.17-simple.html"	# 简化后的源文件
	aimDirPath = "root/3node"	# 目标文件路径
	aimDirPathsplite = aimDirPath.split("/")	# 按照"/"分割,提取文件名
	bmLineFormat = "2node-proxy-clash-"	# 书签行title格式
	outputdict = dict()						# 输出字典

	# 生成简化书签
	simpleHTML(filepath,simpleHTMLPath)
	# 读取文件的每行并返回列表
	with open(simpleHTMLPath, encoding = "utf-8") as readfile:
		readcontent = [i for i in readfile.readlines()]
		getdic = ()
		for dirIndex in range(len(aimDirPathsplite)-1):
			dirName = aimDirPathsplite[dirIndex]
			if dirIndex == 0:
				# 获取mainFolder下的所有文件夹
				getdic = getFolder(floderContentLines=readcontent,tabNum = dirIndex+1)
			if dirIndex!=0 and dirIndex!=len(aimDirPathsplite)-1:
				# 获取下一级文件夹的所有子文件夹
				getdic = getFolder(floderContentLines=getdic[dirName], tabNum = dirIndex+1)
			print("getingDir------------------>{0}".format("\t"*dirIndex+dirName))
		# 获取书签行的{title:url}字典
		getlistdict = getLines(getdic[aimDirPathsplite[len(aimDirPathsplite)-1]])
		print("getingBmLine------------------>{0}".format(aimDirPathsplite[len(aimDirPathsplite)-1]))
		# 获取title格式为"xxx-xxx-xxx-"的bmLine
		getlistdict = getFormatHeadLines(getlistdict,bmLineFormat)
		print("getting the format bmLine------------------>{0}".format(bmLineFormat))
		# 清除title的"xxx-xxx-xxx-"格式
		getlistdict = formatLines(getlistdict,bmLineFormat)
		print("clear the format------------------>{0}".format(bmLineFormat))
		# 将字典赋值给输出字典
		outputdict = getlistdict
		k = outputdict
		# 输出字典转化为文本
		outputdict = str(outputdict)
		# 输出字典文本清除空格
		outputdict = re.sub(r" ","",outputdict)
		# 在":"后加空格
		outputdict = re.sub(r":",": ",outputdict)
		# 在","后加换行
		outputdict = re.sub(r",",",\n",outputdict)
		# print("outputdict------------->\n",outputdict)

	for title in list(k.keys()):
		url = k[title]
		if "raw.githubusercontent.com" in url:
			url = "https://ghproxy.com//" + url
		print(title,"\n",url,"\n\n")
		
