print("Press 1 to add")
print("Press 2 to subtract")
print("Press 3 to multiply")
print("Press 4 to divide")

x = int(input())

a = int (input())
b = int (input())

if x==1:
  if a==56 and b==9 or a==9 and b==56:
      print("77")
  else:
      c=a+b
      print(c)

elif x==2:
    c=a-b
    print(c)

elif x==3:
    if a==45 and b==3 or a==3 and b==45:
        print("555")

    else:
        c=a*b
        print(c)

else:
    if a==56 and b==6 or a==6 and b==56:
        print("4")
    else:
        c=a/b
        print(c)