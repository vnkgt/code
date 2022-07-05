import os,re,random,argparse,hashlib,shutil

# 修改文件名,去掉" - H動漫裏番線上看 - Hanime1.me"
def simpleFileName(srcPath):
	counter = 1
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			filename = re.sub(r" ","",file).split("- H動漫")[0]
			print(filename,"\t---->",counter)
			counter+=1
			os.rename(os.path.join(root,file),os.path.join(root,filename))

# 改后缀名为".mp4"
def addMp4Ext(srcPath):
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			old = os.path.join(root,file)
			new = os.path.join(root,file+".mp4")
			os.rename(old,new)
			print("finish...--->",new)

# 去掉文件后缀名
def subMp4Ext(srcPath):
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			old = os.path.join(root,file)
			new = os.path.join(root,os.path.splitext(file)[1])
			os.rename(old,new)
			print("finish...--->",new)

# 去掉重复的内容文件
def removeSameFile(srcPath):
	standdict = dict()
	needtodel = list()
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			nowfilepath = re.sub(r"\\","/",os.path.join(root,file))
			if file in standdict.keys():
				# print(standdict[file])
				# print(nowfilepath)
				needtodel.append(standdict[file]+"-->"+nowfilepath)
			if file not in standdict.keys():
				standdict[file] = nowfilepath
	for i in needtodel:
		delfilename = i.split("-->")[1]
		os.remove(delfilename)
		print(delfilename)

# 修改md5
def changeAFileMd5(file, show_md5=False):
	def get_md5(file):
	    if os.path.exists(file):
	        with open(file, 'rb') as f:
	            md5 = hashlib.md5()
	            while True:
	                buffer = f.read(4096)
	                if not buffer:
	                    break
	                md5.update(buffer)
	            return md5.hexdigest()
	CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	random_str = ''.join(random.choice(CHARACTERS))
	if show_md5:
		print('before: {0}'.format(get_md5(file)))
	if os.path.exists(file):
	    with open(file, 'ab') as f:
	        f.write(random_str.encode('utf-8'))
	    print(file,'---->The md5 value has been changed.')
	else:
	    raise OSError('File does not exist!')
	if show_md5:
	    print('after: {0}'.format(get_md5(file)))

# 批量修改md5
def changeMd5(srcPath):
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			filepath = re.sub(r"\\","/",os.path.join(root,file))
			changeAFileMd5(file=filepath,show_md5=False)

def findSameAndKeepIt(srcPath,aimPath,aimDir):
	srcDic = dict()
	aimDic = dict()
	aimDir = aimDir
	counter = 1
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			srcDic[file] = root
	for root,dirs,files in os.walk(aimPath):
		for file in files:
			aimDic[file] = root
	for file in srcDic.keys():
		if file in aimDic.keys():
			aimoldpath = os.path.join(aimDic[file],file)
			aimnewpath = os.path.join(aimDir,file)
			shutil.move(aimoldpath,aimnewpath)
			print(counter)
			counter+=1


# 分配文件夹
def fen(srcPath):
	fileDict = dict()
	newfileDict = dict()
	for root,dirs,files in os.walk(srcPath):
		for file in files:
			fileDict[file] = root
	for i in range(len(fileDict.keys())//10+1):
		dirpath = os.path.join(srcPath,"%0.3d"%(i+1))
		if not os.path.exists(dirpath):
			os.mkdir(dirpath)
	
	dirdeep = 1
	dirname = "./{dir1}/{dir2}"
	counter = 0
	for file in fileDict.keys():
		if counter==10:
			counter=0
			dirdeep+=1
		oldfilepath = os.path.join(fileDict[file],file)
		newfilepath = os.path.join(dirname.format(dir1=srcPath,dir2="%0.3d"%dirdeep),file)
		counter+=1
		shutil.move(oldfilepath,newfilepath)
		print(newfilepath)

changeMd5("./HongKongDoll")