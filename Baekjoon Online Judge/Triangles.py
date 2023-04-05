def solution(height: int) -> str:
    return "\n".join("*" * i for i in range(1, height + 1))


if __name__ == "__main__":
    while (height := int(input())) != 0:
        print(solution(height))
