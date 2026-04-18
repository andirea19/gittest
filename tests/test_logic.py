# babies first unit test 

import unittest
import sys
import os

# Path muss passen

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic import get_zodiac

# Unit Test ist in Klasse TestLogic, die von unittest.TestCase erbt.

class TestLogic(unittest.TestCase):
    def test_zodiac_Zwilling(self):
        self.assertEqual(get_zodiac(10, 6), "Zwilling")

    def test_zodiac_Krebs(self):
        self.assertEqual(get_zodiac(16, 7), "Krebs")

if __name__ == '__main__':
    unittest.main() 

