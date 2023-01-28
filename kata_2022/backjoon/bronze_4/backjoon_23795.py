def solution(result: list[int]) -> int:
    return sum(result)


if __name__ == "__main__":
    result = []
    while (money := int(input())) != -1:
        result.append(money)
    print(solution(result))
