def solution(first: int, second: int) -> str:
    return f"{first + second} {first * second}"


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        lines = int(input())
        for _ in range(lines):
            print(solution(*map(int, input().split())))
