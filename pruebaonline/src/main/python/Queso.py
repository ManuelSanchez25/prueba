class Queso:

    def __init__(self, melted=None, temperature=None, melting=20):
        self.melted = melted
        self.temperature = temperature
        self.melting = melting

    def isMelted(self):
        return self.melted

    def getCurrentTemperature(self):
        return self.temperature

    def getMeltingTemperature(self):
        return self.melting

    def setCurrentTemperature(self, temp):
        self.temperature = temp

    def melt(self, melted):
        self.melted = melted
