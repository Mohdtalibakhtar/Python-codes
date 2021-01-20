class A():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname= lname
        # self.email= f"Email is {self.fname}{self.lname}@gmail.com"

    def details(self):
        return f"Name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname ==  None or self.lname == None:
            return "Email not Available"
        return f"Email is {self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname= None
        self.lname= None

a= A("Mohd", "Talib")
print(a.details())
print(a.email)
a.lname="Saif"
print(a.email)

a.email = "mohd.uzaif@gmail.com"
print(a.fname)

del a.email
print(a.email)

