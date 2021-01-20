def next_palindrome(test_cases):
    test_cases+=1
    while not is_palindrome(test_cases) :
        test_cases+=1
    return test_cases


def is_palindrome(test_cases):
    return str(test_cases)==str(test_cases)[::-1]


if __name__ == '__main__':
    print("Enter the number of test cases you want to generate")
    test_cases = int(input())
    list = []
    for i in range(test_cases):
        num = int(input("Enter the number"))
        list.append(num)

for i in range(test_cases):
    print(f"Next palindrome for {list[i]} is {next_palindrome(list[i])}")


