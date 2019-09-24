class Quesadilla:
    def __init__(queso, tortilla, heatLevel):
        self.queso = queso
        self.tortilla = tortilla
        self.heatLevel = heatLevel

    def getQueso():
        return self.queso

    def setQueso(queso):
        self.queso = queso

    def getTortilla():
        return self.tortilla

    def setTortilla(tortilla):
        self.tortilla = tortilla

    def getHeatLevel():
        return self.heatLevel

    def setHeatLevel(heatLevel):
        self.heatLevel = heatLevel

    def prepareSingle():
        while(getQueso().getCurrentTemperature()
              < getQueso().getMeltingTemperature()
              and getTortilla().getCurrentTemperature()
              < getTortilla().getToastTemperature()):

            getTortilla().setCurrentTemperature(
                getTortilla().getCurrentTemperature() + getHeatLevel())
            getQueso().setCurrentTemperature(
                getQueso().getCurrentTemperature() + getHeatLevel())
            if (getTortilla().getCurrentTemperature()
                    >= getTortilla().getToastTemperature()):
                getTortilla().toast(True)
            if (getQueso().getCurrentTemperature()
                    >= getQueso().getMeltingTemperature()):
                getQueso().melt(True)

        if(getQueso().isMelted() and getTortilla().isToasted()):
            return "Perfect quesadilla"
        if(getQueso().isMelted() and not getTortilla().isToasted()):
            return "Good quesadilla"
        if(not getQueso().isMelted() and getTortilla().isToasted()):
            return "Terrible quesadilla"
        else:
            return "You ran out of gas"

    def prepareDouble(self):
        while (self.getQueso().getCurrentTemperature()
                < self.getQueso().getMeltingTemperature()
                and self.getTortilla().getCurrentTemperature()
                < self.getTortilla().getToastTemperature()
                and self.getTortilla2().getCurrentTemperature()
                < self.getTortilla2().getToastTemperature()):

            self.getTortilla().setCurrentTemperature(
                self.getTortilla().getCurrentTemperature()
                + self.getHeatLevel())

            self.getTortilla2().setCurrentTemperature(
                self.getTortilla2().getCurrentTemperature()
                + self.getHeatLevel())

            self.getQueso().setCurrentTemperature(
                self.getQueso().getCurrentTemperature()
                + self.getHeatLevel())

            if (self.getTortilla().getCurrentTemperature()
                    >= self.getTortilla().getToastTemperature()):
                self.getTortilla().toast(True)

            if (self.getTortilla2().getCurrentTemperature()
                    >= self.getTortilla2().getToastTemperature()):
                self.getTortilla2().toast(True)

            if (self.getQueso().getCurrentTemperature()
                    >= self.getQueso().getMeltingTemperature()):
                self.getQueso().melt(True)

        if (self.getQueso().isMelted()
            and self.getTortilla().isToasted()
                and self.getTortilla2().isToasted()):
            return "Perfect quesadilla"

        if ((self.getQueso().isMelted()
             and not self.getTortilla().isToasted()
             and self.getTortilla2().isToasted())
            or
            (self.getQueso().isMelted()
             and self.getTortilla().isToasted()
                and not self.getTortilla2().isToasted())):
            return "Good quesadilla"

        if (self.getQueso().isMelted()
            and not self.getTortilla().isToasted()
                and not self.getTortilla2().isToasted()):
            return "Regular quesadilla"

        if (not self.getQueso().isMelted()
            and self.getTortilla().isToasted()
                and self.getTortilla2().isToasted()):
            return "Bad quesadilla"

        if ((not self.getQueso().isMelted()
             and not self.getTortilla().isToasted()
             and self.getTortilla2().isToasted())
            or
            (not self.getQueso().isMelted()
             and self.getTortilla().isToasted()
             and not self.getTortilla2().isToasted())):
            return "Terrible quesadilla"

        else:
            return "You ran out of gas"
