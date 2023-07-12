from datetime import datetime
from batteries import Battery

class Spindler(Battery):
    def __init__(self, lastServiceDate):
        super().__init__(lastServiceDate)
        self.lastServiceDate = lastServiceDate

    def batteryShouldBeServiced(self):
        newServiceDate = self.lastServiceDate.replace(year=self.lastServiceDate.year + 3)
        
        if newServiceDate < datetime.today().date():
            return True
        else:
            return False