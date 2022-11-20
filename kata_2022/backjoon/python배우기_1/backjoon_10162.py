from enum import Enum


class ButtonSeconds(int, Enum):
    A = 300
    B = 60
    C = 10


def solution():
    target_seconds = int(input())

    if target_seconds % 10 != 0:
        return -1

    result = []
    for index, button in enumerate(ButtonSeconds):
        button_seconds = button.value
        if target_seconds >= button_seconds:
            quotient, remainder = divmod(target_seconds, button_seconds)
            result.append(quotient)
            target_seconds = remainder
        else:
            result.append(0)

    return " ".join(map(str, result))


if __name__ == "__main__":
    print(solution())
