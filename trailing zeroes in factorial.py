def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)

def no_of_zeroes(number):
    count=0
    i=5
    while(number//i !=0):
        count+=int(number/i)
        i=i*5
    return count


if __name__ == '__main__':
    number=int(input("Enter the number: "))
    fac=factorial(number)
    # print(f"Factorial of the number is {fac}")
    print(no_of_zeroes(number))

