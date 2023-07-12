import sys
sys.path.append('/Users/owais/OneDrive/Documents/forage-lyft-starter-repo')
from car import Car
from engine.capulet import Capulet
from battery.spindler import Spindler

class Calliope(Car):
    def __init__(self, currentMileage, lastServiceMileage, lastServiceDate):
        calliopeEngine = Capulet(currentMileage, lastServiceMileage)
        calliopeBattery = Spindler(lastServiceDate)

        super().__init__(calliopeEngine, calliopeBattery)

        self.engine = calliopeEngine
        self.battery = calliopeBattery
    
    def needsService(self):
        return super().needsService()
