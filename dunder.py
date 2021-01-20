class Employee():
    def __init__(self, name, sal , role):
        self.name= name
        self.salary= sal
        self.role = role

    def printdetails(self):
        return f"Employee name is {self.name}, salary is {self.salary},  and role is {self.role}"

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Name ('{self.name}', {self.salary}, '{self.role}')"


emp= Employee("Talib", 323434, "Developer")
emp2= Employee("Saif", 56582, "Engineer")
print(emp + emp2)
print(emp.__repr__())