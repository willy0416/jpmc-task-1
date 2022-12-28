import unittest
from client import getRatio

class TestGetRatio(unittest.TestCase):
    def test_normal(self):
        """Tests that getRatio divides numbers properly"""
        self.assertEqual(getRatio(6, 3), 2, "Should be 2")

    def test_div_by_zero(self):
        """Tests that getRatio avoids division by zero, as desired"""
        self.assertEqual(getRatio(4, 0), None, "Should avoid throwing an error")
    
if __name__ == '__main__':
    unittest.main()