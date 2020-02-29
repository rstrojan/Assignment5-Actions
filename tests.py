import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def Radius_to_Area_test(self):
        self.assertEqual(28.27, task.Radius_to_Area(3))
        self.assertEqual(50.27, task.Radius_to_Area(4))


if __name__ == '__main__':
    unittest.main()
