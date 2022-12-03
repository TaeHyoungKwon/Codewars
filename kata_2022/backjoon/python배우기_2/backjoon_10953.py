def solution():
    case_count = int(input())
    return "\n".join(
        map(
            str,
            [
                sum(int(number) for number in input().split(","))
                for _ in range(case_count)
            ],
        )
    )


if __name__ == "__main__":
    print(solution())
