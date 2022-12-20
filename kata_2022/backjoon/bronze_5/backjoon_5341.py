def solution(number: int) -> int:
    return sum(range(number + 1))


if __name__ == "__main__":
    while (number := int(input())) != 0:
        print(solution(number))
