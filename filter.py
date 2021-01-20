numbers=[5,8,2,5,54,43,7,4,24,60]

def fun(num):
    return num>10

c=list(filter(fun,numbers))
print(c)

from functools import reduce

a=[1,2,3,4]
red = reduce(lambda x,y:x+y, a)
print(red)