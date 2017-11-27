import os
import sys
path = "C:\\Users\\qq122\\Documents\\Tencent Files\\1720936836\\Image\\PhotoWall"
for (path,dirs,files) in os.walk(path):
	for filename in files:
		newname = filename+'.jpg'
		os.rename(path+"\\"+filename , path+"\\"+newname)