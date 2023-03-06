from typing import Annotated

USTon = Annotated[int, "Unit of weight used in the United States"]


def solution():
    all_apples = int(input())
    apple_count_that_klaudia_have_more_than_natalia = int(input())
    apple_count_of_klaudia = (
        all_apples + apple_count_that_klaudia_have_more_than_natalia
    ) // 2
    return f"{apple_count_of_klaudia}\n{all_apples - apple_count_of_klaudia}"


if __name__ == "__main__":
    print(solution())
