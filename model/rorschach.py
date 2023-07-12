from car import Car
from engine.willoughby import Willoughby
from battery.nubbin import Nubbin
from tire.octoprime import Octoprime

class Rorschach(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate, tireWearSensor):
        rorschachEngine = Willoughby(currentMileage, lastServiceMileage)
        rorschachBattery = Nubbin(lastServiceDate)
        rorschachTire = Octoprime(tireWearSensor)

        super().__init__(rorschachEngine, rorschachBattery, rorschachTire)

        self.engine = rorschachEngine
        self.battery = rorschachBattery
        self.tire = rorschachTire
    
    def needsService(self):
        return super().needsService()
