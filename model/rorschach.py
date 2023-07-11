from car import Car
from engine.willoughby import Willoughby
from battery.nubbin import Nubbin

class Rorschach(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate):
        rorschachEngine = Willoughby(currentMileage, lastServiceMileage)
        rorschachBattery = Nubbin(lastServiceDate)

        super().__init__(rorschachEngine, rorschachBattery)

        self.engine = rorschachEngine
        self.battery = rorschachBattery
    
    def needsService(self):
        return super().needsService()
