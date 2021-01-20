class Employee():
    no_of_employess=6
    def __init__(self,aname,salary,post):
        self.name=aname
        self.salary=salary
        self.post=post

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, post is {self.post}"

talib=Employee("Talib",5000,"Developer")
print(talib.printdetails())

class Programmar(Employee):

    def __init__(self, progname, progsal, progrole, languages):
        self.name = progname
        self.salary = progsal
        self.role = progrole
        self.language=languages

    def prog(self):
        return f"Programmar name is {self.name}. Salary is {self.salary} and role is {self.role}, languages known {self.language}"

saif = Programmar("Saif", 799, "Programmar", ["python", "C"])
print(saif.prog())


