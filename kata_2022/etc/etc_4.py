from typing import Optional


class TextOptions:
    def __init__(self, font: str, font_size: Optional[float] = None):
        self._font = font
        self._font_size = font_size

    def get_font(self) -> str:
        return self._font

    def get_font_size(self) -> Optional[float]:
        return self._font_size


class TextOptionsBuilder:
    def __init__(self, font: str):
        self._font = font
        self._font_size = None

    def set_font_size(self, font_size: float):
        self._font_size = font_size
        return self

    def build(self) -> TextOptions:
        return TextOptions(self._font, self._font_size)


class TextOptionsForCopyNWrite:
    def __init__(self, font: str, font_size: Optional[float] = None):
        self._font = font
        self._font_size = font_size

    def get_font(self) -> str:
        return self._font

    def get_font_size(self) -> Optional[float]:
        return self._font_size

    def with_font(self, new_font: str) -> TextOptions:
        return TextOptions(font=new_font, font_size=self._font_size)

    def with_font_size(self, new_font_size: int) -> TextOptions:
        return TextOptions(font=self._font, font_size=new_font_size)


if __name__ == "__main__":
    text_options = TextOptions(font="FiraCode", font_size=20)
    assert text_options.get_font() == "FiraCode"
    assert text_options.get_font_size() == 20

    text_options_for_builder = (
        TextOptionsBuilder(font="FiraCode").set_font_size(font_size=20).build()
    )
    assert text_options_for_builder.get_font() == "FiraCode"
    assert text_options_for_builder.get_font_size() == 20

    text_options_for_conpy_n_write = TextOptionsForCopyNWrite(
        font="FiraCode"
    ).with_font_size(20)
    assert text_options_for_conpy_n_write.get_font() == "FiraCode"
    assert text_options_for_conpy_n_write.get_font_size() == 20
