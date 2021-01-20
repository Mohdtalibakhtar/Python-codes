number = 23
print("You have 5 guesses")

print("Start")
i=1
while (i<=9):
    b= int(input())
    if (b<23):
        print("Number is Greater than the exact number")
        i = i + 1
        print("Number of guesses used", i)
        if (i == 9):
            print("No guesses left, you've lost")
            break
    elif(b>23):
        print("Number is lesser than the exact number")
        i = i + 1
        print("Number of guesses used", i)
        if (i == 9):
            print("No guesses left,you've lost ")
            break
    else:
        print("You won")
        break
