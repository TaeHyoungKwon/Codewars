STANDARD_VALUE = 44031


def solution(number: int) -> str:
    return chr(STANDARD_VALUE + number)


if __name__ == "__main__":
    print(solution(int(input())))
