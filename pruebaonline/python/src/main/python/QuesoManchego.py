from Queso import Queso


class QuesoManchego(Queso):

    def __init__(self, melted=None, temperature=None, melting=20):
        self.melted = melted
        self.temperature = temperature
        self.melting = melting
