from engine import Engine
from battery import Battery

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def engineShouldBeServiced(self):
        return self.engine.engineShouldBeServiced()

    def batteryShouldBeServiced(self):
        return self.battery.batteryShouldBeServiced()

    def needsService(self):
        pass
