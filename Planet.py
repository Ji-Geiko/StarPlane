
class Planet:
    def __init__(self, name, mass, distanceFromSun):
        self.name = name
        self.mass = mass
        self.distanceFromSun = distanceFromSun
        self.printData()    

    def printData(self):
        print(str(self.name))
        print(str(self.mass))
        print(str(self.distanceFromSun))