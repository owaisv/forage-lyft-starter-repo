from tires import Tire

class Octoprime(Tire):
    def __init__(self, tireWearSensor):
        super().__init__(tireWearSensor)
        self.tireWearSensor = tireWearSensor

    def tireShouldBeServiced(self):
        return sum(self.tireWearSensor) >= 3.0