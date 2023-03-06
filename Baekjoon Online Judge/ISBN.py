# 6810


def solution(isbn: str) -> str:
    result = sum(
        digit * 3 if index_ % 2 else digit * 1
        for index_, digit in enumerate(list(map(int, isbn)))
    )
    return f"The 1-3-sum is {result}"


if __name__ == "__main__":
    last_three_digits = "".join(input() for _ in range(3))
    isbn = f"9780921418{last_three_digits}"

    print(solution(isbn))
