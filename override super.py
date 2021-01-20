class A():
    special = "Outside contructor"
    def __init__(self):
        self.cons= "Class A constructor" #instance variable, compiler gives the priority to instance variable and print it first
        self.special = "Special A"

class B(A):
    def __init__(self):
        super().__init__()               #It takes the compiler to the upper class constructor and then compiler comes to this class constructor
        self.cons= "Class B constructor"
        self.special = "Class B"

talib=B()
saif = A()
print(talib.special)
print(saif.special)