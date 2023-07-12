from car import Car
from engine.sternman import Sternman
from battery.spindler import Spindler
from tire.octoprime import Octoprime

class Palindrome(Car):
    def __init__(self, warningIndicator, lastServiceDate, tireWearSensor):
        palindromeEngine = Sternman(warningIndicator)
        palindromeBattery = Spindler(lastServiceDate)
        palindromeTire = Octoprime(tireWearSensor)

        super().__init__(palindromeEngine, palindromeBattery, palindromeTire)

        self.engine = palindromeEngine
        self.battery = palindromeBattery
        self.tire = palindromeTire
    
    def needsService(self):
        return super().needsService()
