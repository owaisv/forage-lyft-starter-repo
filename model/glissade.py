from car import Car
from engine.willoughby import Willoughby
from battery.spindler import Spindler
from tire.carrigan import Carrigan

class Glissade(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate, tireWearSensor):
        glissadeEngine = Willoughby(currentMileage, lastServiceMileage)
        glissadeBattery = Spindler(lastServiceDate)
        glissadeTire = Carrigan(tireWearSensor)

        super().__init__(glissadeEngine, glissadeBattery, glissadeTire)

        self.engine = glissadeEngine
        self.battery = glissadeBattery
        self.tire = glissadeTire
    
    def needsService(self):
        return super().needsService()
