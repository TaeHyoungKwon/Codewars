def solution(num1: int, num2: int, num3: int) -> int:
    case1 = num1 * num2 / num3
    case2 = num1 / num2 * num3
    return int(max(case1, case2))


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
