import sys
sys.path.append('/Users/owais/OneDrive/Documents/forage-lyft-starter-repo')
from engines import Engine
from batteries import Battery

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def engineShouldBeServiced(self):
        return self.engine.engineShouldBeServiced()

    def batteryShouldBeServiced(self):
        return self.battery.batteryShouldBeServiced()

    def needsService(self):
        return self.engineShouldBeServiced() or self.batteryShouldBeServiced()
