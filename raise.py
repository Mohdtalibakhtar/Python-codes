a= input(" Whats your name")
b=int(input())
if b==0:
    raise ZeroDivisionError("0 is not allowed")
if a.isnumeric():
    raise Exception("Enter a valid name")


print(f"Hello {a}")