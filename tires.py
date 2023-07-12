from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tireWearSensor):
        self.tireWearSensor = tireWearSensor

    @abstractmethod
    def tireShouldBeServiced(self):
        pass