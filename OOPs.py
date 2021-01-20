class student():
    pass

talib = student()

talib.std= 4
talib.sec= "B"
talib.subjects = ["Maths", "C", "Python"]

print(talib.sec,talib.std, talib.subjects)

class Employee():
    no_of_employees= 5

emp1= Employee()
admin= Employee()

emp1.name="Python"
emp1.salary=50000
admin.name="Talib"
admin.salary=100000

print(emp1.name,emp1.salary,admin.salary,admin.name)
print(emp1.no_of_employees)
print(admin.no_of_employees)
Employee.no_of_employees=8                 #here we change the value of no of employees
print(admin.no_of_employees)               #here we print and it changes
admin.no_of_employees=9                    #here we again try to change its value but it didnt change although it creates an instance variable of that name
print(emp1.no_of_employees)
print(admin.__dict__)                      #dict funtion used to extract the variables of admin object it returns in dictionary format