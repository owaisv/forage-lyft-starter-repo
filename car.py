import sys
sys.path.append('/Users/owais/OneDrive/Documents/forage-lyft-starter-repo')
from engines import Engine
from batteries import Battery
from tires import Tire

class Car(Engine, Battery, Tire):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
    
    def engineShouldBeServiced(self):
        return self.engine.engineShouldBeServiced()

    def batteryShouldBeServiced(self):
        return self.battery.batteryShouldBeServiced()
    
    def tireShouldBeServiced(self):
        return self.tire.tireShouldBeServiced()

    def needsService(self):
        return self.engineShouldBeServiced() or self.batteryShouldBeServiced() or self.tireShouldBeServiced
