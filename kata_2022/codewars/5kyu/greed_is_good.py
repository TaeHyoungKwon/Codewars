from collections import Counter


def score(dice):
    result = 0
    for key, value in Counter(dice).items():
        if value >= 3:
            result = _value_is_more_than_equal_3(key, result, value)
        else:
            result = _value_is_less_than_equal_3(key, result, value)
    return result


def _value_is_more_than_equal_3(key, result, value):
    if key == 1:
        result += 1000
        if value != 3:
            result += (value % 3) * 100

    if key != 1:
        result += key * 100

    if key == 5:
        result += (value % 3) * 50

    return result


def _value_is_less_than_equal_3(key, result, value):
    score = {1: value * 100, 5: value * 50}.get(key)
    if score:
        result += score
    return result


class TestGreedIsGood:
    def test_greed_is_good(self):
        assert score([2, 3, 4, 6, 2]) == 0
        assert score([4, 4, 4, 3, 3]) == 400
        assert score([2, 4, 4, 5, 4]) == 450
        assert score([3, 3, 3, 3, 3]) == 300
        assert score([1, 1, 1, 1, 5]) == 1150
