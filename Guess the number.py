import random
print("Hello, Welcome to the game")

print("Please print the range")
r1 = int(input("From which number "))
r2 = int(input("To which "))
num = random.randint(r1,r2)

print("Player 1 turns")
chance=1
for i in range(r1,r2):
    ans= int(input("Enter your answer "))
    if ans==num:
        print(f"Congratulations you guessed it \n The number is {num}\nIt took {chance} chances to guess")
        chance += 1
        break
    else:
        chance+=1

num = random.randint(r1,r2)
print("Player 2 turns")
chance2=1
for i in range(r1,r2):
    ans= int(input("Enter your answer "))
    if ans==num:
        print(f"Congratulations you guessed it \n The number is {num}\nIt took {chance2} chances to guess")
        chance2 += 1
        break
    else:
        chance2+=1


if chance>chance2:
    print("Player 2 wins the game")

elif chance2==chance:
    print("Tie")

else:
    print("Player 1 wins the game")