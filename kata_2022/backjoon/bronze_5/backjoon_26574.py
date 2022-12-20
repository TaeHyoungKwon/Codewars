def solution(number: int) -> str:
    return f"{number} {number}"


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        print(solution(int(input())))
