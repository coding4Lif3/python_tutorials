import unittest 
from codewars import is_valid_walk

class TakeaTenMinuteWalkTests(unittest.TestCase):

    def test_is_valid_walk(self):
        self.assertEqual(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True)
    
    def test_is_not_valid_walk(self):
        self.assertEqual(is_valid_walk(['n','s','n','s','n','s','n','s','n','n']), False)