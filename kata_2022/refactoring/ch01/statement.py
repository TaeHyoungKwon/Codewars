import math
from typing import Any, Union


def statement(invoice: dict[str, Any], plays: dict[str, Any]) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'Invoice (Customer: {invoice["customer"]})\n'

    for performance in invoice["performances"]:
        volume_credits += get_volume_credits_for(performance, plays)

        result += f'\t{get_play_for(performance, plays)["name"]}: {dollar_format(get_amount_for(performance, plays) / 100)} ({performance["audience"]} Seats)\n'
        total_amount += get_amount_for(performance, plays)

    result += f"Total Amount: {dollar_format(total_amount / 100)}\n"
    result += f"Volume Credits: {volume_credits}\n"
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
