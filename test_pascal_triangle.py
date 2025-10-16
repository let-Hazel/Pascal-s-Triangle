import unittest
from pascal_triangle import generate_row

class TestPascalTriangle(unittest.TestCase):
    
    def test_first_row(self):
        """Test that the first row of Pascal's Triangle is [1]"""
        result = generate_row(0)
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()