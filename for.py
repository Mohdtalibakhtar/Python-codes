"""a=int(input())
for i in range (1,10,2):
    c=a*i
    print(c)
else:
        print("loop finished")

item = [ ["talib", 1],["python", 2], ["saquib", 3] ]
for name,number in item:
     print(number) """

items = ["king", "talib", "saquib", 4,6,34,654,23,56]
for num in items:
    if str(num).isnumeric() and num>6:
        print(num)