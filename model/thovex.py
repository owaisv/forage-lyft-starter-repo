from car import Car
from engine.capulet import Capulet
from battery.nubbin import Nubbin
from tire.carrigan import Carrigan

class Thovex(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate, tireWearSensor):
        thovexEngine = Capulet(currentMileage, lastServiceMileage)
        thovexBattery = Nubbin(lastServiceDate)
        thovexTire = Carrigan(tireWearSensor)

        super().__init__(thovexEngine, thovexBattery, thovexTire)

        self.engine = thovexEngine
        self.battery = thovexBattery
        self.tire = thovexTire
    
    def needsService(self):
        return super().needsService()
