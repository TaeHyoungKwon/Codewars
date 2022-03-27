from copy import copy
from functools import reduce
import math
from typing import Union

from kata_2022.refactoring.ch01.performance_calculator import create_performance_calculator


def create_statement_data(invoice: dict, plays: dict) -> dict:
    statement_data = {}
    statement_data["customer"] = invoice["customer"]
    statement_data["performances"] = [enrich_performance(performance, plays) for performance in invoice["performances"]]
    statement_data["total_amount"] = get_total_amount(statement_data)
    statement_data["total_volume_credits"] = get_total_volume_credits(statement_data)
    return statement_data


def enrich_performance(performance: dict, plays: dict) -> dict:
    calculator = create_performance_calculator(performance, get_play_for(performance, plays))
    result = copy(performance)
    result["play"] = calculator.play
    result["amount"] = calculator.get_amount()
    return result


def get_play_for(performance: dict[str, Union[str, int]], plays: dict) -> dict:
    return plays[performance["playID"]]


def get_total_amount(data: dict) -> int:
    return reduce(lambda total, p: total + p["amount"], data["performances"], 0)


def get_total_volume_credits(data: dict) -> int:
    result = 0
    for performance in data["performances"]:
        result += get_volume_credits_for(performance)
    return result


def get_usd(num: float) -> str:
    return "${:,.2f}".format(num / 100)


def get_volume_credits_for(performance: dict[str, Union[str, int]]) -> int:
    result = max(performance["audience"] - 30, 0)
    if performance["play"]["type"] == "comedy":
        result += math.floor(performance["audience"] / 5)
    return result
