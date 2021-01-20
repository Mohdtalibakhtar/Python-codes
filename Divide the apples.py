print("Enter the number of apples student got")
apples=int(input())
mn= int(input("Enter the minimum no "))
mx= int(input("Enter the maximum no "))

for i in range (mn,mx+1):
    if apples%i==0:
        print(i, "is a divisor of", apples)
        i+=1

    elif apples%i !=0:
        print(i, "is not the divisor of", apples)
        i+=1