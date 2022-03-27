from copy import copy
import math
from typing import Union


class PerformanceCalculator:
    def __init__(self, performance):
        self.performance = performance


def create_statement_data(invoice: dict, plays: dict) -> dict:
    statement_data = {}
    statement_data["customer"] = invoice["customer"]
    statement_data["performances"] = [enrich_performance(performance, plays) for performance in invoice["performances"]]
    statement_data["total_amount"] = get_total_amount(statement_data)
    statement_data["total_volume_credits"] = get_total_volume_credits(statement_data)
    return statement_data


def enrich_performance(performance: dict, plays: dict) -> dict:
    calculator = PerformanceCalculator(performance)
    result = copy(performance)
    result["play"] = get_play_for(performance, plays)
    result["amount"] = get_amount_for(result)
    return result


def get_play_for(performance: dict[str, Union[str, int]], plays: dict) -> dict:
    return plays[performance["playID"]]


def get_amount_for(performance: dict[str, Union[str, int]]) -> int:
    result = 0
    if performance["play"]["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif performance["play"]["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(f'Unknown genre: {performance["play"]["type"]}')
    return result


def get_total_amount(data: dict) -> int:
    result = 0
    for performance in data["performances"]:
        result += get_amount_for(performance)
    return result


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
