from kata_2022.refactoring.ch01.statement_data import get_usd


class Renderer:
    def __init__(self, statement_data):
        self.statement_data = statement_data

    def render(self):
        raise Exception("Use Subclass")


class PlainTextRenderer(Renderer):
    def __init__(self, data):
        super().__init__(data)

    def render(self) -> str:
        result = f'Invoice (Customer: {self.statement_data["customer"]})\n'
        for performance in self.statement_data["performances"]:
            result += (
                f'\t{performance["play"]["name"]}: '
                f"{get_usd(performance['amount'])} "
                f'({performance["audience"]} Seats)\n'
            )
        result += f"Total Amount: {get_usd(self.statement_data['total_amount'])}\n"
        result += f"Volume Credits: {self.statement_data['total_volume_credits']}\n"
        return result


class HtmlRenderer(Renderer):
    def __init__(self, data):
        super().__init__(data)

    def render(self) -> str:
        result = f"<h1>Invoice (Customer: {self.statement_data['customer']})</h1>\n"
        result += "<table>\n"
        result += "<tr><th>Play</th><th>Seats</th><th>Price</th></tr>\n"

        for perf in self.statement_data["performances"]:
            result += (
                f"\t<tr><td>{perf['play']['name']}</td>"
                f"<td>({perf['audience']} Seats)</td>"
                f"<td>{get_usd(perf['amount'])}</td></tr>\n"
            )

        result += "</table>\n"
        result += f"<p>Total Amount: <em>{get_usd(self.statement_data['total_amount'])}</em></p>\n"
        result += f"<p>Volume Credits: <em>{self.statement_data['total_volume_credits']}</em></p>\n"
        return result
