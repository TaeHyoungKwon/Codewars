def solution(numbers: list[int]) -> int:
    return sum(sorted(numbers, reverse=True)[:2])


if __name__ == "__main__":
    print(solution([int(ele) for ele in input().split()]))
