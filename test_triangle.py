"""
unit testcases for triangle
"""
import unittest

from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """
    methods for the testriangle
    """

    def testset_1(self):
        """
        testcase 1
        """
        self.assertEqual(classify_triangle(5,5,5),True,'Equilateral triangle')
        print("Test Set 1 passed")

    def testset_2(self):
        """
        testcase 2
        """
        self.assertNotEqual(classify_triangle(4,5,4),False,'Isosceles')
        self.assertNotEqual(classify_triangle(3,4,3),False,'Scalene : should be Isosceles')
        self.assertNotEqual(classify_triangle(6,7,5),False,'Scalene : should be Isosceles')
        print("Test Set 2 passed")

    def testset_3(self):
        """
        testcase 3
        """
        self.assertNotEqual(classify_triangle(7,6,5),False,'Isosceles')
        self.assertNotEqual(classify_triangle(5,6,6),False,'Isosceles : should be Scalene')
        self.assertNotEqual(classify_triangle(8,9,5),False,'Isosceles : should be Scalene')
        print("Test Set 3 passed")

    def testset_4(self):
        """
        testcase 4
        """
        self.assertEqual(classify_triangle(3,4,5),True,'Isosceles : should be Scalene test')
        print("Test Set 4 passed")

if __name__ == '__main__':
    unittest.main()
