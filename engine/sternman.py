from engines import Engine

class Sternman(Engine):
    def __init__(self, warningIndicator):
        super().__init__(0, 0, warningIndicator)
        self.warningIndicator = warningIndicator

    def engineShouldBeServiced(self):
        return self.warningIndicator
