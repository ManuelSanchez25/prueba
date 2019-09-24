from mockito import mock, verify, when
import unittest

from Quesadilla import *
from Queso import *
from Tortilla import *

class Quesadilla_test(unittest.TestCase):

    def setUp(self):
        self.quesadilla = Quesadilla()
        self.mockedQueso = mock(Queso, strict=False)
        self.mockedTortilla = mock(Tortilla, strict=False)
        self.mockedTortilla2 = mock(Tortilla, strict=False)
        self.quesadilla.setQueso(self.mockedQueso)
        self.quesadilla.setTortilla(self.mockedTortilla)
        self.quesadilla.setTortilla2(self.mockedTortilla2)

    def test_quesadillaPerfecta(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Perfect quesadilla",self.quesadilla.prepareSingle())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def test_quesadillaBuena(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(20)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Good quesadilla", self.quesadilla.prepareSingle())
        verify(self.mockedTortilla, times=0).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def test_quesadillaTerrible(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(20)
        self.assertEquals("Terrible quesadilla",self.quesadilla.prepareSingle())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedQueso, times=0).melt(True)

    def test_noHayGas(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("You ran out of gas",self.quesadilla.prepareSingle())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def test_quesadillaDoblePerfecta(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Perfect quesadilla",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
    
    def test_quesadillaDobleBuena(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Good quesadilla",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
    
    def test_quesadillaDobleRegular(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(False)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Regular quesadilla",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
    
    def test_quesadillaDobleMala(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Bad quesadilla",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
    
    def test_quesadillaDobleTerrible(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Terrible quesadilla",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
    
    def test_quesadillaDobleNoHayGas(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(False)
        when(self.mockedTortilla).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla2).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(self.mockedQueso).getCurrentTemperature().thenReturn(2, 8, 8, 8, 14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("You ran out of gas",self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)