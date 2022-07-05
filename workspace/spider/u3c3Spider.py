"""
	爬取磁力网站u3c3.com
		1.根据keyword获取搜索结果
			爬取磁力
				磁力标题：btTitle
				磁力链接：btLink
		3.根据第二、第三关键词对结果进行筛选
			第二关键词：secKw		列表中的所有关键字必须要同时满足
			第三关键词：thrKw	 	列表中的关键字必须满足至少一个
		4.保存结果
"""
import os,re,requests

class u3c3Spider():
	def __init__(self,url=str(),keyword=str(),secKw=list(),thrKw=list()):
		self.url = url 		# 要爬取url的地址，字符串中需要用{keyward}、{pagenum}将关键字、页码的参数位置给出
		self.keyword = keyword 		# 第一关键字(搜索关键字)
		self.secKw = secKw  		# 第二关键字(过滤关键字)
		self.thrKw = thrKw 			# 第三关键字(过滤关键字)

	def run(self):
		print("start....")
		btdict = self.getbt()
		btdict = self.filerKw(btdict)
		btdictKw = list(btdict.keys())
		btdictKw.sort()
		outputfile = "./return-"+self.keyword+".txt"
		with open(outputfile,"w",encoding="utf-8") as wf:
			s = str()
			for k in btdictKw:
				s+=k+"\n"+btdict[k]
			wf.write(s)
		print("finish....")
	
	def getbt(self):
		# 获取页面html内容
		url = self.url.format(keyword=self.keyword,pagenum=1)
		requestHeader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0","Connection":"close"}
		response = requests.get(url=url,headers=requestHeader,params={})
		content = response.text
		content = re.sub(r"<a href=\"","",content)
		content = re.sub(r'<[^>]+>','', content)
		content = re.sub(r"\".*>","",content)
		content = re.sub(r"/torrent/.*\.torrent","",content).split()
		btdict = dict()
		nowtitle = str()
		for index in range(len(content)-1):
			if "magnet:?xt=urn:btih:" in content[index+1]:
				nowtitle = content[index]
			if "magnet:?xt=urn:btih:" in content[index]:
				btdict[nowtitle] = content[index]
		return btdict

	# 第二第三关键字过滤
	def filerKw(self,btdict):
		if not self.secKw:
			return self.btdict
		# 按第二关键字过滤,必须要有的关键字，必须同时满足
		secdict = dict()
		print("filter the second keyword...",self.secKw)
		for title in list(btdict.keys()):
			flag = True 		# 用来标记是否包含所有的关键字，True:包含
			for secondkw in self.secKw:
				if secondkw not in title:
					flag = False
					break
			if flag==True:
				secdict[title] = btdict[title]
		if not self.thrKw:
			return secdict
		thrdict = dict()
		# 按照第三关键字进行筛选，至少要满足一个，不需要同时满足
		print("filter the third keyword...",self.thrKw)
		for title in list(secdict.keys()):
			flag = False  	# 用来标记是否含有至少一个关键字
			for thirdkw in self.thrKw:
				if thirdkw in title:
					flag = True
					break
			if flag==True:
				thrdict[title] = secdict[title]
		return thrdict



if __name__ == "__main__":
	u3c3Spider = u3c3Spider()
	u3c3Spider.url = "https://u3c3.com/?search={keyword}"
	u3c3Spider.keyword = "夜桜"
	u3c3Spider.secKw = ["夜桜"]
	u3c3Spider.thrKw = ["2021","2020","2019","2018","2017","2016","2015"]
	u3c3Spider.run()