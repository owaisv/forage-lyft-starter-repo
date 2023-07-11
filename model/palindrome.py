from car import Car
from engine.sternman import Sternman
from battery.spindler import Spindler

class Palindrome(Car):
    def __init__(self, warningIndicator, lastServiceDate):
        palindromeEngine = Sternman(warningIndicator)
        palindromeBattery = Spindler(lastServiceDate)

        super().__init__(palindromeEngine, palindromeBattery)

        self.engine = palindromeEngine
        self.battery = palindromeBattery
    
    def needsService(self):
        return super().needsService()
