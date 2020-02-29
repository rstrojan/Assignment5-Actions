import unittest
import task

class TestCase(unittest.TestCase) :
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(selfs):
        expected = "failure"
        self.assertEqual(expected, task.firstrun())

if __name__ == '__main__':
    unittest.main()