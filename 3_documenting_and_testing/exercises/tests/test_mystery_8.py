import unittest

from .. mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_8([], ''), [])


    def test_unordered_numbers(self):

        self.assertEqual(mystery_8([4,6,2,9,1],6), [6])
    
    def test_characters(self):
        
        self.assertEqual(mystery_8(['k','h','a','d','i','j','a'],'d'), ['d'])
    
    def test_characters2(self):
        
        self.assertEqual(mystery_8(['k','h','a','d','d','i','j','a'],'d'), ['d','d'])
    
    def test_characters3(self):
        
        self.assertEqual(mystery_8(['k','h','a','d','d','i','j','a'],''), ['k', 'h', 'a', 'd', 'd', 'i', 'j', 'a'])
        
    def test_characters4(self):
        
        self.assertEqual(mystery_8(['c','a','t'],'t'), ['t'])
        
    def test_words(self):
        
        self.assertEqual(mystery_8(['bird','cat','dog'],'cat'), ['cat'])
