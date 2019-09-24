from ...main.python import Quesadilla, QuesoManchego, TortillaHarina
from mockito import when, mock, verify, assertEquals, never, times
import unittest


class QuesadillaTest(unittest.TestCase):
    def _init_(self):
        self.quesadilla = Quesadilla()
        self.mockedQueso = mock(QuesoManchego)
        self.mockedTortilla = mock(TortillaHarina)
        self.quesadilla.setQueso = self.mockedQueso
        self.quesadilla.setTortilla = self.mockedTortilla

    def quesadillaPerfecta(self):
        when(self.mockedQueso.isMelted()).thenReturn(True)
        when(self.mockedQueso.isToasted()).thenReturn(True)
        when(self.mockedTortilla.getCurrentTemperature()
             ).thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla.getToastTemperature()).thenReturn(10)
        when(
            self.mockedQueso.getCurrentTemperature()).thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso.getMeltingTemperature()).thenReturn(10)
        assertEquals("Perfect quesadilla", quesadilla.prepareSingle())
        verify(self.mockedTortilla, times(1)).toast(True)
        verify(self.mockedQueso, times(1)).melt(True)

    def quesadillaBuena(self):
        when(self.mockedQueso.isMelted()).thenReturn(True)
        when(self.mockedQueso.isToasted()).thenReturn(False)
        when(self.mockedTortilla.getCurrentTemperature()
             ).thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla.getToastTemperature()).thenReturn(20)
        when(
            self.mockedQueso.getCurrentTemperature()).thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso.getMeltingTemperature()).thenReturn(10)
        assertEquals("Good quesadilla", quesadilla.prepareSingle())
        verify(self.mockedTortilla, never()).toast(True)
        verify(self.mockedQueso, times(1)).melt(True)

    def quesadillaTerrible(self):
        when(self.mockedQueso.isMelted()).thenReturn(False)
        when(self.mockedQueso.isToasted()).thenReturn(True)
        when(self.mockedTortilla.getCurrentTemperature()
             ).thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla.getToastTemperature()).thenReturn(10)
        when(
            self.mockedQueso.getCurrentTemperature()).thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso.getMeltingTemperature()).thenReturn(10)
        assertEquals("Terrible quesadilla", quesadilla.prepareSingle())
        verify(self.mockedTortilla, never()).toast(True)
        verify(self.mockedQueso, times(1)).melt(True)

    def noHayGas(self):
        when(self.mockedQueso.isMelted()).thenReturn(False)
        when(self.mockedQueso.isToasted()).thenReturn(False)
        when(self.mockedTortilla.getCurrentTemperature()
             ).thenReturn(2, 8, 8, 8, 14)
        when(self.mockedTortilla.getToastTemperature()).thenReturn(0)
        when(
            self.mockedQueso.getCurrentTemperature()).thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso.getMeltingTemperature()).thenReturn(0)
        assertEquals("You ran out of gas", quesadilla.prepareSingle())
        verify(self.mockedTortilla, never()).toast(True)
        verify(self.mockedQueso, times(1)).melt(True)

    # Quesadilla doble tests

    def quesadillaDoblePerfecta(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals(
            "Perfect quesadilla",
            self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def quesadillaDobleBuena(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Good quesadilla", self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def quesadillaDobleRegular(self):
        when(self.mockedQueso).isMelted().thenReturn(True)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(False)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals(
            "Regular quesadilla",
            self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def quesadillaDobleMala(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(True)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals("Bad quesadilla", self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def quesadillaDobleTerrible(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(True)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals(
            "Terrible quesadilla",
            self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)

    def quesadillaDobleNoHayGas(self):
        when(self.mockedQueso).isMelted().thenReturn(False)
        when(self.mockedTortilla).isToasted().thenReturn(False)
        when(self.mockedTortilla2).isToasted().thenReturn(False)
        when(
            self.mockedTortilla).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(
            self.mockedTortilla2).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedTortilla).getToastTemperature().thenReturn(10)
        when(self.mockedTortilla2).getToastTemperature().thenReturn(10)
        when(
            self.mockedQueso).getCurrentTemperature().thenReturn(
            2,
            8,
            8,
            8,
            14)
        when(self.mockedQueso).getMeltingTemperature().thenReturn(10)
        self.assertEquals(
            "You ran out of gas",
            self.quesadilla.prepareDouble())
        verify(self.mockedTortilla, times=1).toast(True)
        verify(self.mockedTortilla2, times=1).toast(True)
        verify(self.mockedQueso, times=1).melt(True)
