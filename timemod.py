import time
# c=time.time()
# print("For loop starts at", c)
# for i in range(1050):
#     print("Hello Guys")
# a=time.time()-c
# print("For loop end in ", a, "Seconds")

#
# initial=time.time()
# print("While Loop starts at", initial, "Seconds")
# j=0
# while j<=1000:
#     print("Im python")
#     j+=1
# print("While Loop ends in ", time.time()-initial, "Seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
time.sleep(3)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)