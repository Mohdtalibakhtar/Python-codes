user = int(input("Enter Your Age or Birth year "))

current_year=int(input("Enter the current year "))

a=current_year - user

try:
    if user <= 100:
        print("Your age is", user)
        a += 100
        print("Your age will be 100 years in the year", a)
        print("you want to know your age in specific year ?")
        print("Yes or No")
        b = input()
        if b == 'Yes':
            print("Enter the year in which you want to know your age ")
            check = int(input())
            c = check-current_year
            user+=c
            print("Your age in", check, "is", user)
        elif b == 'No':
            print("Ok")

    elif user > 1900 & user < 2100:
        print("It is Your birth year", user)
        futureage = user + 100
        print("Your age will be 100 years in the year", futureage)
        print("you want to know your age in specific year ?")
        print("Yes or No")
        b = input()
        if b == 'Yes':
            print("Enter the year in which you want to know your age ")
            check = int(input())
            c = check - user
            print("Your age in", check, "is", c)
        elif b == 'No':
            print("Ok")

except Exception as f:
    print(f)

    print("Thank you")

