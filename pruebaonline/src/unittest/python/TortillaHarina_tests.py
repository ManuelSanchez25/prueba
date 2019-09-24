from ...main.python import TortillaHarina
from mockito import when, mock, verify, assertEquals, assertFalse, assertTrue
import unittest


class TortillaHarinaTest(unittest.TestCase):
    def __init__(self):
        self.tortillaHarina = TortillaHarina()

    def testCurrentTemperature(self):
        self.tortillaHarina.setCurrentTemperature(31)
        assertEquals(31, self.tortillaHarina.getCurrentTemperature())

    def testFalseToast(self):
        self.tortillaHarina.toast(False)
        assertFalse(self.tortillaHarina.isToasted())

    def testTrueToast(self):
        self.tortillaHarina.toast(True)
        assertTrue(self.tortillaHarina.isToasted())

    def testToasting(self):
        assertEquals(30, self.tortillaHarina.getToastTemperature())
