def solution(first_weight: int, second_weight: int, third_weight: int) -> int:
    return sorted([first_weight, second_weight, third_weight])[1]


if __name__ == "__main__":
    first_weight = int(input())
    second_weight = int(input())
    third_weight = int(input())
    print(solution(first_weight, second_weight, third_weight))
