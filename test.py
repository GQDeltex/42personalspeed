import unittest
from utils import days_to_workhours, workhours_to_days


class TestDayToWorkhour(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(days_to_workhours(-1), -8)

    def test_zero(self):
        self.assertEqual(days_to_workhours(0), 0)

    def test_week(self):
        self.assertEqual(days_to_workhours(1), 8)
        self.assertEqual(days_to_workhours(2), 16)
        self.assertEqual(days_to_workhours(3), 24)
        self.assertEqual(days_to_workhours(4), 32)
        self.assertEqual(days_to_workhours(5), 40)
        self.assertEqual(days_to_workhours(6), 40)
        self.assertEqual(days_to_workhours(7), 40)

    def test_week2(self):
        self.assertEqual(days_to_workhours(8), 48)
        self.assertEqual(days_to_workhours(9), 56)
        self.assertEqual(days_to_workhours(10), 64)
        self.assertEqual(days_to_workhours(11), 72)
        self.assertEqual(days_to_workhours(12), 80)
        self.assertEqual(days_to_workhours(13), 80)
        self.assertEqual(days_to_workhours(14), 80)


class TestWorkhourToDay(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(workhours_to_days(-8), -1)

    def test_zero(self):
        self.assertEqual(workhours_to_days(0), 0)

    def test_week(self):
        self.assertEqual(workhours_to_days(8), 1)
        self.assertEqual(workhours_to_days(16), 2)
        self.assertEqual(workhours_to_days(24), 3)
        self.assertEqual(workhours_to_days(32), 4)
        self.assertEqual(workhours_to_days(40), 5)

    def test_week2(self):
        self.assertEqual(workhours_to_days(48), 8)
        self.assertEqual(workhours_to_days(56), 9)
        self.assertEqual(workhours_to_days(64), 10)
        self.assertEqual(workhours_to_days(72), 11)
        self.assertEqual(workhours_to_days(80), 12)

    def test_edge(self):
        self.assertEqual(workhours_to_days(40), 5)
        self.assertEqual(workhours_to_days(41), 5)
        self.assertEqual(workhours_to_days(42), 5)
        self.assertEqual(workhours_to_days(43), 5)
        self.assertEqual(workhours_to_days(44), 8)
        self.assertEqual(workhours_to_days(45), 8)
        self.assertEqual(workhours_to_days(46), 8)
        self.assertEqual(workhours_to_days(47), 8)
        self.assertEqual(workhours_to_days(48), 8)


if __name__ == '__main__':
    unittest.main()
