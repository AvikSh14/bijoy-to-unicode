# coding=utf8

import unittest
from bijoy2unicode import bijoy2unicode

class TestBijoy2UnicodeConverter(unittest.TestCase):

    def test_number_conversion(self):
        self.assertEqual(bijoy2unicode('2'), '২')

    def test_vowel_conversion(self):
        self.assertEqual(bijoy2unicode('Av'), 'আ')
        self.assertEqual(bijoy2unicode('A'), 'অ')
        self.assertEqual(bijoy2unicode('B'), 'ই')
        self.assertEqual(bijoy2unicode('C'), 'ঈ')
        self.assertEqual(bijoy2unicode('I'), 'ও')


if __name__ == '__main__':
    unittest.main()