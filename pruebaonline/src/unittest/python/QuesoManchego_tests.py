from ...main.python import QuesoManchego
from mockito import when, mock, verify, assertEquals, assertFalse, assertTrue
import unittest


class QuesoManchegoTest(unittest.TestCase):
    def __init__(self):
        self.quesoManchego = QuesoManchego()

    def testCurrentTemperature(self):
        self.quesoManchego.setCurrentTemperature(26)
        assertEquals(26, self.quesoManchego.getCurrentTemperature())

    def testFalseMelt(self):
        self.quesoManchego.melt(False)
        assertFalse(self.quesoManchego.isMelted())

    def testTrueMelt(self):
        self.quesoManchego.melt(True)
        assertTrue(self.quesoManchego.isMelted())

    def testMelting(self):
        assertEquals(21, self.quesoManchego.getMeltingTemperature())
