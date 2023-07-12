from engines import Engine

class Capulet(Engine):
    def __init__(self, currentMileage, lastServiceMileage):
        super().__init__(currentMileage, lastServiceMileage)
        self.currentMileage = currentMileage
        self.lastServiceMileage = lastServiceMileage

    def engineShouldBeServiced(self):
        return self.currentMileage - self.lastServiceMileage > 30000

