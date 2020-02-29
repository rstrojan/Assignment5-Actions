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
        self.assertEqual(28.27, task.radius_to_area(3))
        self.assertEqual(50.27, task.radius_to_area(4))

    def first_last_test(self):
        list_1 = [1, 2, 3]
        result = task.first_last(list_1)
        expected_1 = 1
        expected_2 = 2
        self.assertEqual(expected_1, result[0])
        self.assertEqual(expected_2, result[1])

        list_2 = [4, -1, 0, "Ryan"]
        result = task.first_last(list_2)
        expected_1 = 4
        expected_2 = "Ryan"
        self.assertEqual(expected_1, result[0])
        self.assertEqual(expected_2, result[1])


if __name__ == '__main__':
    unittest.main()
