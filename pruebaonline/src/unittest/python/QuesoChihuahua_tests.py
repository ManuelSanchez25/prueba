from ...main.python import QuesoChihuahua
from mockito import when, mock, verify, assertEquals, assertFalse, assertTrue
import unittest


class QuesoChihuahuaTest(unittest.TestCase):
    def __init__(self):
        self.quesoChihuahua = QuesoChihuahua()

    def testCurrentTemperature(self):
        self.quesoChihuahua.setCurrentTemperature(21)
        assertEquals(21, self.quesoChihuahua.getCurrentTemperature())

    def testCurrentTemperature(self):
        self.quesoChihuahua.setCurrentTemperature(21)
        assertEquals(21, self.quesoChihuahua.getCurrentTemperature())

    def testFalseMelt(self):
        self.quesoChihuahua.melt(False)
        assertFalse(self.quesoChihuahua.isMelted())

    def testTrueMelt(self):
        self.quesoChihuahua.melt(True)
        assertTrue(self.quesoChihuahua.isMelted())

    def testMelting(self):
        assertEquals(20, self.quesoChihuahua.getMeltingTemperature())
