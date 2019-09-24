from Tortilla import Tortilla


class TortillaHarina(Tortilla):

    def __init__(self, toast=None, temperature=None, toasting=20):
        self.toasted = toast
        self.temperature = temperature
        self.toasting = toasting
