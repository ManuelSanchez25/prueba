class Quesadilla:

    def __init__(self, queso=None, tortilla=None, tortilla2=None, heatLevel=0):
        self.queso = queso
        self.tortilla = tortilla
        self.tortilla2 = tortilla2
        self.heatLevel = heatLevel

    def getQueso(self):
        return self.queso

    def setQueso(self, queso):
        self.queso = queso

    def getTortilla(self):
        return self.tortilla

    def setTortilla(self, tortilla):
        self.tortilla = tortilla

    def getTortilla2(self):
        return self.tortilla2

    def setTortilla2(self, tortilla):
        self.tortilla2 = tortilla

    def getHeatLevel(self):
        return self.heatLevel

    def setHeatLevel(self, heatLevel):
        self.heatLevel = heatLevel

    def prepareSingle(self):
        while (self.getQueso().getCurrentTemperature() < self.getQueso().getMeltingTemperature() and
               self.getTortilla().getCurrentTemperature() < self.getTortilla().getToastTemperature()):
            self.getTortilla().setCurrentTemperature(self.getTortilla().getCurrentTemperature() + self.getHeatLevel())
            self.getQueso().setCurrentTemperature(self.getQueso().getCurrentTemperature() + self.getHeatLevel())
            if (self.getTortilla().getCurrentTemperature() >= self.getTortilla().getToastTemperature()):
                self.getTortilla().toast(True)
            if (self.getQueso().getCurrentTemperature() >= self.getQueso().getMeltingTemperature()):
                self.getQueso().melt(True)
        if (self.getQueso().isMelted() and self.getTortilla().isToasted()):
            return "Perfect quesadilla"
        if (self.getQueso().isMelted() and not self.getTortilla().isToasted()):
            return "Good quesadilla"
        if (not self.getQueso().isMelted() and self.getTortilla().isToasted()):
            return "Terrible quesadilla"
        else:
            return "You ran out of gas"

    def prepareDouble(self):
        while (self.getQueso().getCurrentTemperature() < self.getQueso().getMeltingTemperature() and
               self.getTortilla().getCurrentTemperature() < self.getTortilla().getToastTemperature() and
               self.getTortilla2().getCurrentTemperature() < self.getTortilla2().getToastTemperature()):
            self.getTortilla().setCurrentTemperature(self.getTortilla().getCurrentTemperature() + self.getHeatLevel())
            self.getTortilla2().setCurrentTemperature(self.getTortilla2().getCurrentTemperature() + self.getHeatLevel())
            self.getQueso().setCurrentTemperature(self.getQueso().getCurrentTemperature() + self.getHeatLevel())
            if (self.getTortilla().getCurrentTemperature() >= self.getTortilla().getToastTemperature()):
                self.getTortilla().toast(True)
            if (self.getTortilla2().getCurrentTemperature() >= self.getTortilla2().getToastTemperature()):
                self.getTortilla2().toast(True)
            if (self.getQueso().getCurrentTemperature() >= self.getQueso().getMeltingTemperature()):
                self.getQueso().melt(True)

        if (self.getQueso().isMelted() and self.getTortilla().isToasted() and self.getTortilla2().isToasted()):
            return "Perfect quesadilla"
        if ((self.getQueso().isMelted() and not self.getTortilla().isToasted() and self.getTortilla2().isToasted()) or
           self.getQueso().isMelted() and self.getTortilla().isToasted() and not self.getTortilla2().isToasted()):
            return "Good quesadilla"
        if (self.getQueso().isMelted() and not self.getTortilla().isToasted() and not self.getTortilla2().isToasted()):
            return "Regular quesadilla"
        if (not self.getQueso().isMelted() and self.getTortilla().isToasted() and self.getTortilla2().isToasted()):
            return "Bad quesadilla"
        if ((not self.getQueso().isMelted() and not self.getTortilla().isToasted() and self.getTortilla2().isToasted()) or
           (not self.getQueso().isMelted() and self.getTortilla().isToasted() and not self.getTortilla2().isToasted())):
            return "Terrible quesadilla"
        else:
            return "You ran out of gas"
