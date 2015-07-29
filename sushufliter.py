def ifsushu(x):
	if (x==1):
		return True
	else:
		for i in range(2,x):
			if (x%i==0):
				return True
		return False

print filter(ifsushu,range(1,101))