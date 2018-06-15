#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import platform
import shutil

FPath = "C:\Downloads\\"         # 要做检查的源根目录
TargetPath = 'd:\\WJ'            # 目标文件目录  
copyFlag = True                  # True要拷贝文件，False不拷贝文件

if platform.system() == "Windows":
	windowsOrLinux = "\\" 
else:
	windowsOrLinux = "/"

def fCopyFile(srcFile,destFile):
	shutil.copy(srcFile,destFile)

def findFile(oldPath,fileName):
	fold = open(oldPath + windowsOrLinux + fileName)
	fTarget = open(TargetPath + windowsOrLinux + "ErrorShift.txt","a+") 
	fTarget.write(oldPath+windowsOrLinux+fileName +"        --- File List:" +"\n")
	while True:
		line = fold.readline()
		if line:
			re = line.split('\t')
			if len(re) < 4:
				print("Tip File Error:"+oldPath+windowsOrLinux+fileName+"\t"+line)
				continue
			number = float(re[3])
			if number < float(8.00000):
				fTarget.write(line)
				if copyFlag:
					if os.path.isfile(oldPath + windowsOrLinux + re[0]):
						fCopyFile(oldPath + windowsOrLinux + re[0],TargetPath+ windowsOrLinux + re[0])
					else:
						print("Warning No file:"+oldPath + windowsOrLinux + re[0])
		else:
			break
	fold.close()
	fTarget.close()
						
def fTargetFile(path):
	fileList = []
	for NowPath,ChildPathName,Files in os.walk(path):
		for file in Files:
			if file.endswith('.nsi'):
				fileList.append((file,NowPath))
	fileList.sort(key=lambda x:x[1])
	for (Lfile,LnowPath) in fileList:
		findFile(LnowPath,Lfile)				
fTargetFile(FPath)		