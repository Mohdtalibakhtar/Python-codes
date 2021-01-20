def palindrome(n):
    if n>10:
        n+=1
    while not is_palindrome:
        n+=1
    else:
        print(f"{n} is less than 10")
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]


if __name__ == '__main__':
    n=int(input("Enter the number of test cases you want to generate"))
    numbers=[]
    for i in range(n):
        number=int(input("Enter the number "))
        numbers.append(number)

for i in range(n):
    print(f"The palindrome of {numbers[i]} is {palindrome(numbers[i])} ")