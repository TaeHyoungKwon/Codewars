import unittest
from calendar import Calendar
from itertools import groupby
from operator import itemgetter


WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
c = Calendar()

def most_frequent_days(year):
    weekday_count = dict.fromkeys(range(7), 0)
    for i in range(1, 13):
        sorted_by_weekday = sorted([day for day in c.itermonthdays2(year, i) if day[0] != 0], key=itemgetter(1))
        for k, g in groupby(sorted_by_weekday, key=itemgetter(1)):
            weekday_count[k] += len(list(g))
    most_frequent_count = max(weekday_count.values())
    return [WEEKDAY_MAP[k] for k, v in weekday_count.items() if v == most_frequent_count]
    
    
class TestMostFrequentDays(unittest.TestCase):
    def test_most_frequent_days(self):
        self.assertEqual(most_frequent_days(year=2427), ["Friday"])
