#coding:utf-8
"""
	1.搜索关键字(sreachKeyword)
	2.文章标题(articleTitle)、文章链接(articleUrl)、总共有多少页(totalPage)
	3.访问文章链接(articleUrl)
	4.获取标题(articleTitle)
		获取文章内容(articleContent)
			获取磁力链接(以数字或字母开头的那一行)(btLink)
"""
import requests 	# 用于网络请求
import os
import re
import time
import json

class LiuliSpider():
	# urlformat：网址格式(包含页码参数pageNum和关键字参数keyword)
	# keyword：关键字，搜索框里写的
	# secondkeyword：第二关键字列表，所有关键字必须同时满足
	# thirdkeyword：第三关键字，至少要满足一个
	# article：文章url列表格式{title01:url01,title02:url02...},getTitleAndLink函数的返回值
	# totalPage：爬取的页数
	def __init__(self,urlformat=str(),keyword=str(),secondkeyword=list(),
		thirdkeyword=list(),article=dict(),totalPage=0):
		self.urlformat = urlformat 			# urlformat中的两个参数：页码(pageNum),关键字(keyword)
		self.keyword = keyword				# 第一关键字		
		self.secondkeyword = secondkeyword 	# 第二关键字列表	
		self.thirdkeyword = thirdkeyword	# 第三关键字列表
		self.totalPage = totalPage 			# 由关键字返回，共有多少页
		self.article = article				# 文章字典，格式{articleTitle:url}
		self.bt = dict()					# 最后返回的字典，格式{articleTitle:[btLink1,btLink2,btLink3]}
		self.requestHeader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0","Connection":"close"}    #浏览器标识
		

	def run(self):
		# 获取对应关键字的总页数
		if self.totalPage==0:	#没有传入要爬取几页
			self.totalPage = self.getPageTotalNum()
		# 获取每页的文章标题及其链接
		if not self.article:	#如果是空字典
			self.article =self.getTitleAndLink(self.totalPage)	
		# 第二、第三关键字过滤
		self.article = self.filterkw(self.article)
		print(self.article)
		# 获取每个文章链接下的bt链接
		self.bt = self.getBtLink(self.article)
		# 保存数据
		self.savedata(self.bt)
		print("run finish...")

	# 获取总页数
	def getPageTotalNum(self):
		print("getPageTotalNum......\n")
		# 从第一页获取总共的页数
		# 1)发送请求
		url = self.urlformat.format(pageNum=1,keyword=self.keyword)
		response = requests.get(url=url,headers=self.requestHeader,params={})
		# 2)将获取获取的文本按行分割，按行匹配
		contentlist = response.text.split("\n")
		for linecontent in contentlist:
			matchpage = re.match(r"(.*)第 (\d*) 页，共 (\d*) 页(.*)",linecontent)
			if matchpage:
				num = int(matchpage.group(3))
		return num
		
	# 获取每页的所有文章及其链接,pageNum：页数
	def getTitleAndLink(self,num):
		artic = dict()
		print("getTitleAndLink.....\n")
		for pageN in range(num):
			# 按页请求
			pageUrl = self.urlformat.format(pageNum=pageN+1,keyword=self.keyword)
			pageResponse = requests.get(url=pageUrl,headers=self.requestHeader,params={})
			# 按行分割每页内容，匹配文章标题及其链接地址
			pageContentList = pageResponse.text.split("\n")
			for linecontent in pageContentList:
				# <a href="https://www.hacg.cat/wp/81409.html" rel="bookmark">[夜桜字幕组/yozakura.sub] 2021年1月3D作品合集</a>
				matcharticle = re.match(r'(.*)<a href="https://www.hacg.cat/wp/(\d*).html"(.*)>(.*)</a>(.*)',linecontent)
				if matcharticle:
					title = matcharticle.group(4)
					url = "https://www.hacg.cat/wp/{0}.html".format(matcharticle.group(2))
					if title not in list(artic.keys()):
						artic[title] = url
			print("getTitleAndLink finish page--------->",pageN+1)
		return artic

	# 获取bt链接,articleDict文章的标题及链接
	def getBtLink(self,articleDict):
		btdict = dict()		# 输出文本
		print("getBtLink......\n")
		for title in list(articleDict.keys()):
			url = articleDict[title]
			# 请求文章
			articleResponse = requests.post(url=url,headers=self.requestHeader,params={})
			print(title,"--->",url)
			# 去除不必要的干扰元素
			article = articleResponse.text
			# article = re.sub(r"<.*style.*>.*<.*style.*>","",article)
			article = re.sub(r'<[^>]+>','', article)	# 去除html标签
			article = re.sub(r"\[.*\]","",article)
			article = re.sub(r"目录","",article)
			article = re.sub(r" ","",article)
			if title not in list(btdict.keys()):	# 为相应的标题创建一个列表
				btdict[title] = list()
			for linecontent in list(article.split("\n")):
				matchBtLink = re.match(r"([0-9a-fA-F]{30,})",linecontent)
				if matchBtLink:
					btLink = str(matchBtLink.group())
					btdict[title].append(btLink)
					print(btLink)
		return btdict

	# 过滤文章与链接字典，第二、第三关键字过滤
	def filterkw(self,article):
		if not self.secondkeyword:
			return self.article
		# 按第二关键字过滤,必须要有的关键字，必须同时满足
		secdict = dict()
		print("filter the second keyword...",self.secondkeyword)
		for title in list(article.keys()):
			flag = True 		# 用来标记是否包含所有的关键字，True:包含
			for secondkw in self.secondkeyword:
				if secondkw not in title:
					flag = False
					break
			if flag==True:
				secdict[title] = article[title]
		if not self.thirdkeyword:
			return secdict
		thrdict = dict()
		# 按照第三关键字进行筛选，至少要满足一个，不需要同时满足
		print("filter the third keyword...",self.thirdkeyword)
		for title in list(secdict.keys()):
			flag = False  	# 用来标记是否含有至少一个关键字
			for thirdkw in self.thirdkeyword:
				if thirdkw in title:
					flag = True
					break
			if flag==True:
				thrdict[title] = secdict[title]
		return thrdict

	# 保存数据
	def savedata(self,btdict):
		t = time.localtime(time.time())
		t = "{year}.{mon}.{day}".format(year=t.tm_year,mon=t.tm_mon,day=t.tm_mday)
		outputfile = "./result-"+self.keyword+"-"+t+".txt"	# 输出文件
		outStringList = list()
		for title in list(btdict.keys()):
			url = str(self.article[title])
			bt = str()
			for i in btdict[title]:
				bt+=i+"\n"
			outStringList.append(title+"---->"+url+"\n"+bt+"\n")
		outStringList.sort()	# 排序函数进行排序
		with open(outputfile,"w",encoding="utf-8") as outf:
			for i in outStringList:
				outf.write(i)

if __name__ == "__main__":
	# 创建LiuliSpider实例对象
	llspd = LiuliSpider()
	llspd.urlformat = "https://www.hacg.cat/wp/page/{pageNum}?s={keyword}" 		# 爬取的url地址
	llspd.keyword = "夜桜" 	# 第一关键字，获取所有搜索结果
	llspd.secondkeyword = ["夜桜"]	# 第二关键字，筛选时需要同时满足
	llspd.thirdkeyword = ["2021","2020","2019","2018","2017","2016","2015"] 	# 第三关键字，筛选时必须至少满足一个
	llspd.totalPage = 0 		# 要爬取多少页，0表示爬取所有页
	llspd.run()					# 程序运行

	