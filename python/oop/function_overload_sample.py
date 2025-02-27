from typing import Union

DATA_FORMAT_NORMAL = "normal"
DATA_FORMAT_NUMBER = "number"


class Cell:
    def set_data_format(self, data_format: str):
        ...

    def set_data(self, data: str):
        ...


def write(cell: Cell, data: Union[str, int]):
    if isinstance(data, str):
        cell.set_data_format(DATA_FORMAT_NORMAL)
    elif isinstance(data, int):
        cell.set_data_format(DATA_FORMAT_NUMBER)
    else:
        raise TypeError(f"지원하지 않는 타입입니다: {type(data)}")

    cell.set_data(data)


# 사용 예시:
# cell = Cell()
# write(cell, "Hello")  # 문자열 처리
# write(cell, 42)       # 숫자 처리
