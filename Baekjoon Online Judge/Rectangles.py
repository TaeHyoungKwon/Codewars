def solution(row: int, column: int) -> str:
    return "\n".join("*" * column for _ in range(row))


if __name__ == "__main__":
    print(solution(row=int(input()), column=int(input())))
