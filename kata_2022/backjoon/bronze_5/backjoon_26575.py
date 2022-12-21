def solution(d: float, f: float, p: float) -> str:
    return f"${d * f * p:.2f}"


if __name__ == "__main__":
    case_count = int(input())
    for _ in range(case_count):
        print(solution(*map(float, input().split())))
