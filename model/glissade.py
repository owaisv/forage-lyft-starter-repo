from car import Car
from engine.willoughby import Willoughby
from battery.spindler import Spindler

class Glissade(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate):
        glissadeEngine = Willoughby(currentMileage, lastServiceMileage)
        glissadeBattery = Spindler(lastServiceDate)

        super().__init__(glissadeEngine, glissadeBattery)

        self.engine = glissadeEngine
        self.battery = glissadeBattery
    
    def needsService(self):
        return super().needsService()
