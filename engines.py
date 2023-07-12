
from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, lastServiceMileage, currentMileage, warningIndicator=False):
        self.lastServiceMileage = lastServiceMileage
        self.currentMileage = currentMileage
        self.warningIndicator = warningIndicator
    
    @abstractmethod
    def engineShouldBeServiced(self):
        pass
