def solution(numbers: list[int]) -> int:
    max_count = sorted(numbers).pop()
    return sum(max_count - number for number in numbers)


if __name__ == "__main__":
    print(solution(list(map(int, input().split()))))
