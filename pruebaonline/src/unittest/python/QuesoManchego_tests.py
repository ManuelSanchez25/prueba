import unittest
from QuesoManchego import QuesoManchego 

class QuesoManchego_test(unittest.TestCase):

    def setUp(self):
        self.quesoManchego = QuesoManchego()

    
    def test_CurrentTemperature(self):
        self.quesoManchego.setCurrentTemperature(21)
        self.assertEqual(21,self.quesoManchego.getCurrentTemperature())
    
    
    def test_FalseMelt(self):
        self.quesoManchego.melt(False)
        self.assertFalse(self.quesoManchego.isMelted())
    
    
    def test_TrueMelt(self):
        self.quesoManchego.melt(True)
        self.assertTrue(self.quesoManchego.isMelted())
    
    
    def test_Melting(self):
        self.assertEqual(20,self.quesoManchego.getMeltingTemperature())