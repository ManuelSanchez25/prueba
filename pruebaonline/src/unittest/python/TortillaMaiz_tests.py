from ...main.python import TortillaMaiz
from mockito import when, mock, verify, assertEquals, assertFalse, assertTrue
import unittest


class TortillaMaizTest(unittest.TestCase):
    def __init__(self):
        self.tortillaMaiz = TortillaMaiz()

    def testCurrentTemperature(self):
        self.tortillaMaiz.setCurrentTemperature(36)
        assertEquals(36, self.tortillaMaiz.getCurrentTemperature())

    def testFalseToast(self):
        self.tortillaMaiz.toast(False)
        assertFalse(self.tortillaMaiz.isToasted())

    def testTrueToast(self):
        self.tortillaMaiz.toast(True)
        assertTrue(self.tortillaMaiz.isToasted())

    def testToasting(self):
        assertEquals(35, self.tortillaMaiz.getToastTemperature())
