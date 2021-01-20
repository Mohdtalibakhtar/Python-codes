# import datetime
# def gettime():
#     return datetime.datetime.now()
#
#
#
# print("Enter your name")
# name = input()
# if name == "talib":
#     print("Hello " +name+ "\n What you want to know \n press 1 for diet plan and press 2 for exercise plan")
#     a= int(input())
#     if a==1:
#         gettime()
#         f= open("talib diet.txt", "r")
#         print(f.readline())
#     elif a==2:
#            gettime()
#            f= open("talibexercise.txt")
#            print(f.readline())

#     a =int(input())
# if a==1:
#     gettime()
#     f= open("talib diet.txt", "r")
#     print(f.readline())
# elif a==2:
#        gettime()
#        f= open("talibexercise.txt")
#        print(f.readline())
#
# if name == "saif":
#     print("Hello Saif\n What you want to know \n press 1 for diet plan and press 2 for exercise plan")
#     b =int(input())
# elif b==1:
#     gettime()
#     f= open("saif diet.txt", "r")
#     print(f.readline())
# elif b==2:
#     gettime()
#     f= open("saifexercise.txt")
#     print(f.readline())
#
# if name == "uzaif":
#     print("Hello Uzaif \n What you want to know \n press 1 for diet plan and press 2 for exercise plan")
#     c =int(input())
# elif c==1:
#     gettime()
#     f= open("uzaifdiet.txt", "r")
#     print(f.readline())
# elif c==2:
#     gettime()
#     f= open("uzaifexercise.txt")
#     print(f.readline())


client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
lock_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Lock")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in lock_list.items():
            print("Press", key, "to lock", value, "\n", end="")
        lock_name = int(input())
        print("Selected Job : ", lock_list[lock_name])
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
        k = 'y'
        while (k is not "n"):
            print("Enter", lock_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()
    elif op is 2:
        for key, value in lock_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")