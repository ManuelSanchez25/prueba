class Tortilla:

    def __init__(self, toast=None, temperature=None, toasting=20):
        self.toasted = toast
        self.temperature = temperature
        self.toasting = toasting

    def isToasted(self):
        return self.toasted

    def getToastTemperature(self):
        return self.toasting

    def getCurrentTemperature(self):
        return self.temperature

    def setCurrentTemperature(self, temp):
        self.temperature = temp

    def toast(self, toasted):
        self.toasted = toasted
