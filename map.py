numbers=["43", "43","76"]

numbers= list(map(int,numbers))
# for i in range (len(numbers)):
#     numbers[i]= int(numbers[i])

numbers[2] = numbers[2]+1
print(numbers[2])


def sq(x):
    return x*x

def cube(x):
    return x*x*x

func=[sq,cube]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)