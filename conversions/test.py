
from util import conv
import unittest

class UnitTest(unittest.TestCase):
    def test_invalid(self):
        self.assertRaises(ValueError, conv, -200, 'C', 'F')
    
    def test_valid(self):
        test_cases = [((-40, 'F',), (-60, 'C')),
                      ((5, 'F'), (100, 'F')),
                      ((70, 'F'), (21.1, 'C'))]

        for test_case in test_cases:
            ((from_val, from_unit), (to_val, to_unit)) = test_case
            print("re")
            result = conv(from_val, from_unit, to_unit)
            self.assertAlmostEqual(to_val, result)
        
    def test_equal(self):
        temp = 32
        result = conv(temp, 'F', 'F')
        self.assertTrue(result is temp)
    
    def test_unit_error(self):
        self.assertRaises(ValueError, conv, 0, 'F', 'H')
        self.assertRaises(ValueError, conv, 0, 'D', 'A')

unittest.main()