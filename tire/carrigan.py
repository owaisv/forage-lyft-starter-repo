from tires import Tire

class Carrigan(Tire):
    def __init__(self, tireWearSensor):
        super().__init__(tireWearSensor)
        self.tireWearSensor = tireWearSensor

    def tireShouldBeServiced(self):
        return any(map(lambda current_tire: current_tire >= 0.9, self.tireWearSensor))