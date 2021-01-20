# def fun1(a,b,c):
#     print(a,b,c)
# d=fun1("Talib", "Saif", "Uzaif")

# def fun(*args):
#     print(args[1])
# list= ["talib","saif","uzaif"]
# fun(*list)

def fun(normal, *args, **kwargs):
    print(normal)
    print("args funtioning")
    for i in args:
        print(i)
    print("Kwargs functioning")
    for key, value in kwargs.items():
        print(key, value)


list=["talib", "saif", "uzaif"]
normal="Hello"
list2={"dominos":"pizza", "mcd": "Burger", "al bake": "shawarma"}
fun(normal, *list, **list2)