class grandfather():
    basketball=4

class father(grandfather):
    guitar = 3

class son (father):
    guitar = 5
    def guit(self):
        return f"Hey Im Awesome, I play {self.guitar} no of tunes"

harry=son()
print(harry.guit())

