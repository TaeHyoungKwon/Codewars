from typing import Any

from kata_2022.refactoring.ch01.renderer import HtmlRenderer, PlainTextRenderer
from kata_2022.refactoring.ch01.statement_data import create_statement_data, get_usd


def statement(invoice: dict[str, Any], plays: dict[str, Any]) -> str:
    renderer = PlainTextRenderer(create_statement_data(invoice, plays))
    return renderer.render()


def html_statement(invoice: dict, plays: dict) -> str:
    renderer = HtmlRenderer(create_statement_data(invoice, plays))
    return renderer.render()
