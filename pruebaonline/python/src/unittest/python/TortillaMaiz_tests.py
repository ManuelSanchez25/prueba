import unittest
from TortillaMaiz import TortillaMaiz 

class TortillaMaiz_test(unittest.TestCase):

    def setUp(self):
        self.tortillaMaiz = TortillaMaiz()

    
    def test_CurrentTemperature(self):
        self.tortillaMaiz.setCurrentTemperature(21)
        self.assertEqual(21,self.tortillaMaiz.getCurrentTemperature())
    
    
    def test_FalseToast(self):
        self.tortillaMaiz.toast(False)
        self.assertFalse(self.tortillaMaiz.isToasted())
    
    
    def test_TrueToast(self):
        self.tortillaMaiz.toast(True)
        self.assertTrue(self.tortillaMaiz.isToasted())
    
    
    def test_Toasting(self):
        self.assertEqual(20,self.tortillaMaiz.getToastTemperature())