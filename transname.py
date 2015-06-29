# -*- coding: utf-8 -*-
#输入姓名转换为首字母大写的规范形式
def normalize(s):
	s1=s.lower()
	s1[0].upper()
	return s1
L=['adam', 'LISA', 'barT']
L=map(normalize,L)
print L