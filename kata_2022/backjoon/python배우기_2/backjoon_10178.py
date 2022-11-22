def solution():
    case_count = int(input())

    result = []
    for _ in range(case_count):
        candy_count, brother_count = map(int, input().split())
        quotient, remainder = divmod(candy_count, brother_count)
        result.append(
            f"You get {quotient} piece(s) and your dad gets {remainder} piece(s)."
        )
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
