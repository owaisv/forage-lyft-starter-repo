from car import Car
from engine.capulet import Capulet
from battery.nubbin import Nubbin

class Thovex(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate):
        thovexEngine = Capulet(currentMileage, lastServiceMileage)
        thovexBattery = Nubbin(lastServiceDate)

        super().__init__(thovexEngine, thovexBattery)

        self.engine = thovexEngine
        self.battery = thovexBattery
    
    def needsService(self):
        return super().needsService()
