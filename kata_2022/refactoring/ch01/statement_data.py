from copy import copy
from functools import reduce
import math
from typing import Union


class PerformanceCalculator:
    def __init__(self, performance: dict, play: dict):
        self.performance = performance
        self.play = play

    def get_amount(self) -> int:
        raise Exception("Use subclass")

    def get_volume_credits(self) -> int:
        return max(self.performance["audience"] - 30, 0)


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


class TragedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result = 40000
        if self.performance["audience"] > 30:
            result += 1000 * (self.performance["audience"] - 30)
        return result

    def get_volume_credits(self) -> int:
        result = super().get_volume_credits()
        result += math.floor(self.performance["audience"] / 5)
        return result


class ComedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result = 30000
        if self.performance["audience"] > 20:
            result += 10000 + 500 * (self.performance["audience"] - 20)
        result += 300 * self.performance["audience"]
        return result


def create_performance_calculator(performance: dict, play: dict) -> PerformanceCalculator:
    if play["type"] == "tragedy":
        return TragedyCalculator(performance, play)
    elif play["type"] == "comedy":
        return ComedyCalculator(performance, play)
    else:
        raise ValueError(f"Unknown genre: {play['type']}")


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
