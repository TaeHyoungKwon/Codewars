from typing import Any

from kata_2022.refactoring.ch01.statement_data import create_statement_data, get_amount_for, get_usd


def statement(invoice: dict[str, Any], plays: dict[str, Any]) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data: dict) -> str:
    result = f'Invoice (Customer: {data["customer"]})\n'
    for performance in data["performances"]:
        result += (
            f'\t{performance["play"]["name"]}: '
            f"{get_usd(get_amount_for(performance) / 100)} "
            f'({performance["audience"]} Seats)\n'
        )
    result += f"Total Amount: {get_usd(data['total_amount'] / 100)}\n"
    result += f"Volume Credits: {data['total_volume_credits']}\n"
    return result
