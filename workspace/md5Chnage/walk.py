import os,re

src = "D://download//upload//hanime1.me"
for root,dirs,files in os.walk(src):
	for file in files:
		f = re.sub(r"\\","/",os.path.join(root,file))
		os.system("python md5Change.py "+f)
		print(f)