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

    def test_time_delta(self):
        date1 = "12/14/1987"
        date2 = "12/14/1988"
        result = task.time_delta(date1,date2)
        self.assertEqual(366, result) #88 was a leap year


if __name__ == '__main__':
    unittest.main()
