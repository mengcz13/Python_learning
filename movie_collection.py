# -*- coding: utf-8 -*-

#找出F盘BYRPT北邮人下载文件夹里的所有mkv和mp4文件，输出到MovieList.txt，目前不支持中文
#20150629

import os
import re
		
def CmpIgnoreCase(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1<u2:
		return -1
	elif u1>u2:
		return 1
	else:
		return 0

def GetMkvFiles(s,namelist):
	for x in os.listdir(s):
		whole=os.path.join(s,x)
		if os.path.isfile(whole) and os.path.splitext(x)[1] in ['.mkv','.mp4'] :
			namelist.append(x)
		elif os.path.isdir(whole):
			GetMkvFiles(whole,namelist)
			
MkvNameList=[]
GetMkvFiles('F:\\BYRPT',MkvNameList)
MkvNameList.sort(CmpIgnoreCase)
with open('F:\\BYRPT\\MovieList.txt','w') as f:
	for x in MkvNameList:
		f.write(x)
		f.write('\n')
		
print MkvNameList
print u'请输入您要查询的电影名称：'
target=raw_input()
target.decode('utf-8').encode('utf-8')
pattern='(.*)'+target+'(.*)'
for x in MkvNameList:
	if re.search(pattern,x):
		print x