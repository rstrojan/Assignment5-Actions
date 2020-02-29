import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())


class Test(TestCase):
    def test_radius_to_area(self):
        self.assertEqual(28.27, task.radius_to_area(3))
        self.assertEqual(50.27, task.radius_to_area(4))


if __name__ == '__main__':
    unittest.main()
