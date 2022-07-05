"""
	多个srt字幕文件按时间顺序整合
"""
import os

def srtSort(srcfile=list()):
	srcfile = srcfile
	srtlist = list()	# 读取的所有文件的每一行
	# 读取所有字幕文件并放进同一个列表
	for file in srcfile:
		with open(file,"r",encoding="utf-8") as rf:
			srtlist += rf.read().split()
	# 整合同一个时间段的字幕,以“-->”为标识符
	srtdict = dict() # 字幕字典,字典结构{timeline:contentline}
	timeline = str() # 时间段
	contentline = str() # 字幕内容，整合分段字幕字典的内容
	contentlinetemplist = list() # 字幕分段的字典
	index = 0
	while index<len(srtlist):
		if srtlist[index]=="-->":
			for i in range(2,len(contentlinetemplist)-2):
				contentline+=contentlinetemplist[i]
			if contentline:
				srtdict[timeline] = contentline
			timeline = srtlist[index-1]+"-->"+srtlist[index+1] # 时间行
			contentline = str()
			contentlinetemplist = list()
		contentlinetemplist.append(srtlist[index])
		index+=1
	for i in range(2,len(contentlinetemplist)-2):
		contentline+=contentlinetemplist[i]
	srtdict[timeline] = contentline
	# 按时间顺序整理
	sortkeylist = list(srtdict.keys())
	sortkeylist.sort()	# 排序整理
	outputsrt = str()	# 输出所有字幕字符串
	for index in range(len(sortkeylist)):
		timeline = sortkeylist[index]
		contentline = srtdict[timeline]
		outputsrt += str(index+1)+"\n"+timeline+"\n"+contentline+"\n\n"
	return outputsrt

if __name__=="__main__":
	# 要整合的srt字幕文件
	files = ["./语音.srt","./文字.srt",]
	sortSrt = srtSort(srcfile = files)
	with open("./output.srt","w",encoding="utf-8") as wf:
		wf.write(sortSrt)
	print("finish...sort--->",files)




