def solution(result: list[str]) -> int:
    win_count = result.count("W")

    if win_count == 0:
        return -1

    if win_count >= 5:
        return 1
    elif win_count >= 3:
        return 2
    else:
        return 3


if __name__ == "__main__":
    print(solution([input() for _ in range(6)]))
