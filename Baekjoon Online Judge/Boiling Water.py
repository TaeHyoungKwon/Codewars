def solution(b: int) -> str:
    p = 5 * b - 400

    if p == 100:
        result = 0
    elif p > 100:
        result = -1
    else:
        result = 1

    return f"{p}\n{result}"


if __name__ == "__main__":
    print(solution(int(input())))
