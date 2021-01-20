def calculator (a,b):
    """This function is used as a calculator"""
    print("Press 1 to add")
    print("Press 2 to subtract")
    print("Press 3 to multiply")
    print("Press 4 to divide")
    x= int(input())

    if x==1:
        c=a+b
        return c

    elif x==2:
        c=a-b
        return c

    elif x==3:
        c=a*b
        return c

    elif x==4:
        c=a/b
        return c

    else:
        print("You entered a wrong value")

f= calculator(5,7)
print(f)

"""print(calculator.__doc__)"""