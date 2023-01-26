from typing import Final

CYCLE: Final = 8


def solution(target_number: int) -> int:
    remainder = target_number % CYCLE

    if remainder == 1:
        return 1
    elif remainder in {2, 0}:
        return 2
    elif remainder in {3, 7}:
        return 3
    elif remainder in {4, 6}:
        return 4
    else:
        return 5


if __name__ == "__main__":
    print(solution(int(input())))
