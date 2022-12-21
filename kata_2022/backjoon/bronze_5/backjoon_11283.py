STANDARD_INDEX = 44031


def solution(korean: str):
    return ord(korean) - STANDARD_INDEX


if __name__ == "__main__":
    korean = input()
    print(solution(korean))
