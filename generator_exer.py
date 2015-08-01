# -*- coding: utf-8 -*-
def fib(x):
	n,a,b=0,0,1
	while n<x:
		yield b
		a,b=b,a+b
		n=n+1

print u'输入最大下标'
maxn=input()
L=[]
for num in fib(maxn) :
	L.append(num)

# 倒序
# def cmpf(x,y):
# 	if (x>y):
# 		return -1
# 	else:
# 		return 1

print L