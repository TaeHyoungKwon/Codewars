from collections import Counter
from enum import Enum


class Result(str, Enum):
    BALANCE = "Balance"
    LEFT = "Left"
    RIGHT = "Right"


def balance(left: str, right: str) -> Result:
    left_result = total_weight_calculator(left)
    right_result = total_weight_calculator(right)

    if left_result == right_result:
        return Result.BALANCE
    elif left_result > right_result:
        return Result.LEFT
    else:
        return Result.RIGHT


def total_weight_calculator(value):
    return value.count("!") * 2 + value.count("?") * 3


def test_balance():
    assert balance("", "") == "Balance"
    assert balance("!!", "??") == "Right"
    assert balance("!??", "?!!") == "Left"
    assert balance("!?!!", "?!?") == "Left"
    assert balance("!!???!????", "??!!?!!!!!!!") == "Balance"
