try:
    f1=open("talib.text")
    f=open("king.txt")

except IOError as e:
    print("IO error occur",e)

else:
    print("This will execute only if exception is not run")  #Either this will execute or Exception

finally:                                                     #this will execute for sure either exeption will occur or not
    f1.close()
    print("This will always run")

print("Hello")