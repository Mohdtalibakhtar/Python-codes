from abc import ABCMeta, abstractmethod

class shape(metaclass=ABCMeta):
    @abstractmethod    #this method force the child class to import the defined function
    def printarea(self):
        return 0

class Rectangle(shape):
    def __init__(self):
        self.length= 6
        self.breadth= 7

    # def printarea(self):
    #      return self.length * self.breadth

rec= Rectangle()
# print(rec.printarea())