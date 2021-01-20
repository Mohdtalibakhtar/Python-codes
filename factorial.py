def fact1(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac


def fact2(n):
    if n==1:
        return 1
    else:
        return n*fact2(n-1)


def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number = int(input("Enter the number\n"))
print("Factorial using iterative method", fact1(number))
print("Factorial using recursive method", fact2(number))
print("fibonacci series", fibonacci(number))

