class Employee():
    var =8
    no_of_employess=6
    def __init__(self,aname,salary,post):
        self.name=aname
        self.salary=salary
        self.post=post

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, post is {self.post}"


class Player():
    var= 10
    def __init__(self, name, game):
        self.name=name
        self.game= game

    def printplayer(self):
         return f"Player name is {self.name} and Player Playes {self.game}"

class both(Employee, Player):
    pass

saif=both("saif", 5000, "Both")
print(saif.printdetails())
print(saif.var)                         # Here it prints the vale of Employee class var because we inherit it first
mazhar = Player("Mazhar", ["Football", "Cricket"])
print(mazhar.printplayer())