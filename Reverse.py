print("Enter number of elements in the list")
list=[]                         #create an empty list
n= int(input())
print("Enter elements")
for i in range (0,n):
    num=int(input())
    list.append(num)            #adding numbers in the list
print(list)


list.reverse()                  #using reverse function
print(list)


a=list[::-1]                    #using string slicing
print(a)


for i in range(len(list)//2):    #using swapping
    list[i], list[len(list) -i -1]= list[len(list) -i -1], list[i]
print(list)