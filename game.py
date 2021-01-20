import random
# global user
# global comp
user=0
comp=0
print("Welcome to the game")
i=1
while i<=5:
    print("Round", i)
    list = ["Snake","Water", "Gun"]
    print("Press 1 for Snake")
    print("Press 2 for Water")
    print("Press 3 for Gun")
    c= str(input())
    choice= random.choice(list)
    print("Computer Selects", choice)
    if c=="Snake" and choice=="Water" or c=="Water" and choice=="Gun" or c=="Gun" and choice=="Snake":
        print("You won")
        user = user+1
        # print(user)

    elif c=="Snake" and choice=="Gun" or c=="Water" and choice=="Snake"  or c=="Gun" and choice=="Water":
        print("Computer won")
        comp = comp+1
        # print(comp)

    elif c==choice:
        print("tie")
    i=i+1

else:
    print("Game Over")
print("Your Score", user)
print("Computer Score", comp)
