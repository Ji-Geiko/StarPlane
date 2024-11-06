
class Sun:
    def __init__(self, name, mass, planet):

        self.name = name
        self.mass = mass
        self.planet = planet

        self.printData()
    
    def printData(self):
        print(str(self.name))
        print(str(self.mass) + ' kg')
        print(str(self.planet))