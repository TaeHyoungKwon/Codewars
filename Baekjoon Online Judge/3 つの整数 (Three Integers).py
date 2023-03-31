def solution(numbers: list[int]) -> int:
    return 2 if numbers.count(2) > numbers.count(1) else 1


if __name__ == "__main__":
    print(solution([int(ele) for ele in input().split()]))
