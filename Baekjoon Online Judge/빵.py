def solution(cases: list[int]) -> int:
    result = [b for a, b in cases if a <= b]
    return min(result) if result else -1


if __name__ == "__main__":
    print(solution(list(map(int, input().split()) for _ in range(int(input())))))
