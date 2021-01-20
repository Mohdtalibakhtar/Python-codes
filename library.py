class lib():
  def read(self):
      print("Books Available are", list)

  def lend(self):
      print("Book you want to lend")
      b=input()
      list.remove(b)
      print("Books available are", list)
      return


  def donate(self):
      print("Book you want to donate")
      c=input()
      list.append(c)
      print(list)
      return "Thanks for donation"


  def ret(self):
      print("Which book you want to return")
      d=input()
      list.append(d)
      print("Books Available are", list)
      return



print("Welcome to Library")
list = ["Python"]
talib = lib()
i=1
while i==1:
    print("Press 1 to see books \nPress 2 to Lend a book\nPress 3 to donate a book\nPress 4 to return the book ")
    a = int(input())
    if a == 1:
        talib.read()
        print("Do you want to continue 0/1\nPress 1 to continue and 0 to exit")
        user= int(input())
        if user==1:
            i=1
        elif user==0:
            i=0

    elif a == 2:
        print(talib.lend())
        print("Do you want to continue 0/1\nPress 1 to continue and 0 to exit")
        user = int(input())
        if user == 1:
            i = 1
        elif user == 0:
            i = 0

    elif a == 3:
        print(talib.donate())
        print("Do you want to continue 0/1\nPress 1 to continue and 0 to exit")
        user = int(input())
        if user == 1:
            i = 1
        elif user == 0:
            i = 0

    elif a == 4:
        print(talib.ret())
        print("Do you want to continue 0/1\nPress 1 to continue and 0 to exit")
        user = int(input())
        if user == 1:
            i = 1
        elif user == 0:
            i = 0






#     def read(self):
#         f= open("file.txt")
#         print(f.read())
#         f.close()
#
#     def lend(self):
#         f= open("file.txt", "a+")
#         print("Which book you want to lend")
#         b=input()
#         f.write(b)
#         print(f.read())
#         f.close()
#
#     def donate(self):
#         print("Which book you want to donate")
#         f= open("file.txt", "a+")
#         c=input()
#         f.write(c)
#         f.close()
#         return "Thank you for donation"
#
#     def ret(self):
#         print("Which book you want to return")
#         f=open("file.txt", "a+")
#         d= input()
#         f.write(d)
#         f.close()
#
# print("Welcome to Library")
# talib= lib()
# print("Press 1 to see books \nPress 2 to Lend a book\nPress 3 to donate a book\nPress 4 to return the book ")
# a=int(input())
# if a==1:
#     print(talib.read())
#
# elif a==2:
#     print(talib.lend())
#
# elif a==3:
#     print(talib.donate())
#
# elif a==4:
#     print(talib.ret())