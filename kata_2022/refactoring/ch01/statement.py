from copy import copy
import math
from typing import Any, Union


def statement(invoice: dict[str, Any], plays: dict[str, Any]) -> str:
    statement_data = {}
    statement_data["customer"] = invoice["customer"]
    statement_data["performances"] = [enrich_performance(performance) for performance in invoice["performances"]]
    return render_plain_text(statement_data, plays)


def enrich_performance(performance: dict) -> dict:
    result = copy(performance)
    return result


def render_plain_text(data: dict, plays: dict) -> str:
    result = f'Invoice (Customer: {data["customer"]})\n'
    for performance in data["performances"]:
        result += f'\t{get_play_for(performance, plays)["name"]}: {dollar_format(get_amount_for(performance, plays) / 100)} ({performance["audience"]} Seats)\n'
    result += f"Total Amount: {dollar_format(get_total_amount(data, plays) / 100)}\n"
    result += f"Volume Credits: {get_total_volume_credits(data, plays)}\n"
    return result


def get_total_amount(data: dict, plays: dict) -> int:
    result = 0
    for performance in data["performances"]:
        result += get_amount_for(performance, plays)
    return result


def get_total_volume_credits(data: dict, plays: dict) -> int:
    result = 0
    for performance in data["performances"]:
        result += get_volume_credits_for(performance, plays)
    return result


def dollar_format(num: float) -> str:
    return "${:,.2f}".format(num)


def get_volume_credits_for(performance: dict[str, Union[str, int]], plays: dict) -> int:
    result = max(performance["audience"] - 30, 0)
    if get_play_for(performance, plays)["type"] == "comedy":
        result += math.floor(performance["audience"] / 5)
    return result


def get_play_for(performance: dict[str, Union[str, int]], plays: dict) -> dict:
    return plays[performance["playID"]]


def get_amount_for(performance: dict[str, Union[str, int]], plays: dict) -> int:
    result = 0
    if get_play_for(performance, plays)["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif get_play_for(performance, plays)["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(f'Unknown genre: {get_play_for(performance, plays)["type"]}')
    return result
