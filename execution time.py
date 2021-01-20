import time

def add(a,b):
    c=a+b
    return c

def mul(a,b):
    c=a*b
    return c

if __name__ == '__main__':
    print(add(5,6))
    initial= time.asctime(time.localtime(time.time()))
    print(initial)
    print(mul(5,7))
    time.sleep(2)
    executed=time.asctime(time.localtime(time.time()))
    print(executed)
    # final=time.asctime(time.localtime(time.time())-initial)