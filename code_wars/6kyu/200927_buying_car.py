import unittest


def nbMonths(old, new, saving, loss):
    count = 0

    while True:
        additional = (100 - loss) / 100 + 0.5 * (count // 2)
        available = saving + (old * additional)
        result = available - (new * additional)

        if result > 0:
            return [count, round(result)]

        count += 1
        saving += saving
    
    
class TestNbMonths(unittest.TestCase):
    def test_nbmonths(self):
        startPriceOld, startPriceNew, savingperMonth, percentLossByMonth = 2000, 8000, 1000, 1.5
        actual = nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth)
        self.assertEqual(actual, [6, 766])
