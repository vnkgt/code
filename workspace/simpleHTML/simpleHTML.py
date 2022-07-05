import os,shutil,re,sys

# 修改一个bookmark,path:html文件路径,addext:生成的新html
def subAFile(oldfilepath,newfilepath,addext=str()):
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
			# 清除about:blank空白标签
			result = re.sub(r"<DT>(.*)about:blank</A>",'',result)
			# 删除小括号说明
			# result = re.sub(r"\((.*)\)","",result)
			bmwfile.write(result)
			print("finish----->",outputfile)


if __name__ == "__main__":
	print(sys.argv)
	srcfile = sys.argv[1]
	outputfile = os.path.splitext(srcfile)[0]+"-simple"+os.path.splitext(srcfile)[1]
	subAFile(srcfile,outputfile)
	# print(outputfile)