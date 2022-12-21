def solution(case_count: int) -> int:
    return sum(int(input()) for _ in range(case_count))


if __name__ == "__main__":
    case_count = int(input())
    print(solution(case_count))
