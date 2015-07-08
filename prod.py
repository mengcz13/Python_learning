def prod(x):
    def mul(x,y):
        return x*y
    return reduce(mul,x)
Max=input()
L=range(1,Max+1)
print prod(L)
