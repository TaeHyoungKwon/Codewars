from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_curency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_curency, amount) -> float:
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_curency, amount) -> float:
        return amount * 1.2


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        return self.converter.convert("EUR", "USD", 100)


if __name__ == "__main__":
    converter = AlphaConverter()
    app = App(converter=converter)
    print(app.start())
    print("KwonTaeHyoung")