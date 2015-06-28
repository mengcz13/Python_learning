print 'Please input 2 numbers'
a=input()
b=input()
if a<b:
	(a,b)=(b,a)
#print a,' ',b
while (a%b!=0):
	(a,b)=(b,a%b)
print b