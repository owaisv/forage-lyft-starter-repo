import sys
sys.path.append('/Users/owais/OneDrive/Documents/forage-lyft-starter-repo')
from car import Car
from engine.capulet import Capulet
from battery.spindler import Spindler
from tire.octoprime import Octoprime

class Calliope(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate, tireWearSensor):
        calliopeEngine = Capulet(currentMileage, lastServiceMileage)
        calliopeBattery = Spindler(lastServiceDate)
        calliopeTire = Octoprime(tireWearSensor)

        super().__init__(calliopeEngine, calliopeBattery, calliopeTire)

        self.engine = calliopeEngine
        self.battery = calliopeBattery
        self.tire = calliopeTire
    
    def needsService(self):
        return super().needsService()
