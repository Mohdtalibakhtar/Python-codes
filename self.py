class Employee():
    no_of_employess=6
    def __init__(self,aname,salary,post):
        self.name=aname
        self.salary=salary
        self.post=post

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, post is {self.post}"

    @staticmethod
    def printgood(string):
        print(string, "is good boy")
        return


talib=Employee("Talib",5000,"Developer")
Employee.printgood("Talib")

# saif=Employee()

# talib.name="Talib"
# talib.salary=40000
# talib.post="Developer"
# saif.name="Saif"
# saif.salary=40000
# saif.post="Developer"


print(talib.name)
print(talib.printdetails())