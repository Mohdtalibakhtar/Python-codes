# a= open("file.txt")
# print(a.read())


# f= open("talib.text","w")
# f.write("Hello")
# f.write("\n My name is Talib")

file = open("talib.text","r+")
print(file.readline())
# file.write("\n Im a python developer")
print(file.tell())
print(file.readline())
print(file.tell())
file.seek(34)
print(file.readline())