def solution(x: int, k: int) -> int:
    case_1 = 7 * 1000 * k
    case_2 = (7 / 2) * 1000 * k
    case_3 = (7 / 4) * 1000 * k

    return next((int(case) for case in [case_1, case_2, case_3] if case <= x * 1000), 0)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
