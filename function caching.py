import time
from  functools import lru_cache

@lru_cache(3)          #It stores the function to avoid the time
def somework(n):
    # print("Print")
    time.sleep(3)
    print(n)

if __name__ == '__main__':
    print("Now running")
    somework(3)
    print("after func")
    somework(3)
    somework(3)
