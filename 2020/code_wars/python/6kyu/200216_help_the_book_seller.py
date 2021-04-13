import unittest
from collections import OrderedDict, Counter


def calc_all_of_book_by_category(listOfArt, listOfCat):
    temp = []
    cat_dict = OrderedDict.fromkeys(listOfCat, 0)
    for cat in listOfCat:
        for art in listOfArt:
            if cat == art.split()[0][0]:
                cat_dict[cat] += int(art.split()[1])
        temp.append('({} : {})'.format(cat, cat_dict[cat]))
    return temp


def stock_list(arts, cats):
    cnt = Counter()
    for art in (cats and arts):
        x, c = art.split()
        cnt[x[0]] += int(c)
    return ' - '.join('({} : {})'.format(c, cnt[c]) for c in (arts and cats))

    
class TestStockList(unittest.TestCase):
    def test_should_return_empty_string_when_list_of_art_or_list_of_cat_is_empty(self):
        listOfArt = []
        listOfCat = ["A", "B"]
        actual = stock_list(listOfArt, listOfCat)
        self.assertEqual(actual, '')

    def test_stock_list(self):
        listOfArt = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        listOfCat = ["A", "B"]
        actual = stock_list(listOfArt, listOfCat)
        self.assertEqual(actual, "(A : 200) - (B : 1140)")
