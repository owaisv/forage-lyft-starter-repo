from datetime import datetime
from batteries import Battery

class Nubbin(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def batteryShouldBeServiced(self):
        newServiceDate = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        if newServiceDate < datetime.today().date():
            return True
        else:
            return False