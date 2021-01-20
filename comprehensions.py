list=[]
for i in range(100):
    if i %3==0:
        list.append(i)

print(list)

print("Same program in one line ")

ls= [i for i in range(100) if i%3==0 ]
print(ls)

dict1={i:f"Item{i}" for i in range(1000) if i%100==0}
print(dict1)

print("Just reverse the printing technique")

dict2={value:key for key,value in dict1.items()}
print(dict2)


evens=(i for i in range(100) if i %2==0)
for item in evens:
    print(item)

print(type(evens))