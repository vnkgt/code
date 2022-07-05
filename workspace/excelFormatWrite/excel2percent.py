"""
	*.xlsx文件----->对应比例人数字典,返回的是具体的人数
	注:
		txt2excel.py中使用的是"修正比例后的字典"
"""
"""
项目所需的库:
	openpyxl
	os
	re
excel表格的结构:
	table--->sheet--->content
	content内容:
			column01  column02  column03  column04  column05
				q01		q02		q03			q04			q05
	row01		
	row02
	row03
	row04
	row05
	row06
"""
import os,re,openpyxl
# 读取表格获取各个答案的比例,返回字典{"q01":{"ans01":perc01,"ans02":perc02,...},"q02":{}...}
def excelGetPercDict(filePath,sheetName,ansSplitFlag=";",startcolumn=1,startrow=1):
	outputdict = dict()			# 输出字典
	columnindex = startcolumn 	# 列标记
	rowindex = startrow 		# 行标记
	workbook = openpyxl.load_workbook(filename = filePath)	# 读取文件
	worksheet = workbook[sheetName]							# 读取表格
	while worksheet.cell(column=columnindex,row=startrow).value:	# 能匹配到列
		nowquest = None
		while worksheet.cell(column=columnindex,row=rowindex).value:# 能匹配到行
			cellvalue = worksheet.cell(column=columnindex,row=rowindex).value
			ansList =	cellvalue.split(ansSplitFlag)			# 长度为1则是单选,否则为多选
			if rowindex == startrow:				# 如果是问题
				outputdict[cellvalue] = dict()		# 初始化问题的答案字典
				nowquest = cellvalue				# 当前的问题
			else:
				for i in range(len(ansList)): 		# 遍历答案字典
					ans = ansList[i]
					questdict = outputdict[nowquest]
					if ans not in questdict:		# 如果答案不在字典中
						questdict[ans] = 1
					else:							# 如果答案已经在字典中
						questdict[ans] = questdict[ans] + 1
			rowindex += 1
		rowindex = startrow							# 重置行标记
		columnindex += 1
	workbook.close()								# 关闭excel文件
	totalnum = 0 									# 总人数
	for quest in list(outputdict.keys()):			# 找出总人数
		quest = outputdict[quest]
		questnum = 0 								# 每个问题的答案总人数
		for ans in list(quest.keys()):
			questnum += quest[ans]
		if totalnum==0:
			totalnum = questnum
		if totalnum!=0 and totalnum>=questnum:
			totalnum = questnum
	for quest in list(outputdict.keys()):			# 将答案的人数转换为比例
		quest = outputdict[quest]
		for ans in list(quest.keys()):
			quest[ans] = quest[ans]/totalnum		# 转换为比例
	return outputdict								# 返回字典

# 对单选问题的比例进行修正:若每个单选题的每个答案均有比例,则将最后一个答案的比例修改为0
# 并把比例转换为对应的人数
def percFix(questDict,peopleNum):
	for quest in list(questDict.keys()):	# 修正单选题的比例
		quest = questDict[quest]	# 问题的答案字典
		questTotalPerc = 0 			# 问题每个答案和起来的比例
		lastans = None 				# 单选题的最后一个答案
		for ans in list(quest.keys()):
			ansperc = quest[ans]		# 答案的比例
			questTotalPerc += ansperc
			lastans = ans
		if questTotalPerc == 1:
			quest[ans] = 0
		questTotalPerc = 0 			# 重置问题每个答案和起来的比例
		lastans = None 				# 重置单选题的最后一个答案
	for quest in list(questDict.keys()):	# 将比例转换为人数
		quest = questDict[quest]	# 问题的答案字典
		questTotalPeopel = 0 		# 当前问题的总人数
		lastans = None 				# 当前问题的额最后一个答案
		for ans in list(quest.keys()):
			ansperc = quest[ans]	# 答案的比例
			quest[ans] = int(peopleNum*ansperc)				# 比例转换为人数
			questTotalPeopel += quest[ans]
			lastans = ans
		if questTotalPeopel<peopleNum:
			quest[lastans] = peopleNum - questTotalPeopel	# 单选题最后一个答案的人数
		questTotalPeopel = 0 		# 重置当前问题的人数
		lastans = None				# 重置当前问题的最后一个答案
	return questDict



if __name__ == "__main__":
	get = excelGetPercDict("./excel2percent-test.xlsx","mainsheet")# 获取表格各个问题选项的比例
	fixget = percFix(get,137)	# 将比例转换为具体的人数
	for quest in list(fixget.keys()):
		quest = fixget[quest]
		print(quest)

	