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

    def test_first_last(self):
        my_arr = [1, 2, 3]
        result = task.first_last(my_arr)
        expected_1 = 1
        expected_2 = 3
        self.assertEqual(expected_1, result[0])
        self.assertEqual(expected_2, result[1])

        my_arr = [4, -1, 0, "Ryan"]
        result = task.first_last(my_arr)
        expected_1 = 4
        expected_2 = "Ryan"
        self.assertEqual(expected_1, result[0])
        self.assertEqual(expected_2, result[1])


if __name__ == '__main__':
    unittest.main()
