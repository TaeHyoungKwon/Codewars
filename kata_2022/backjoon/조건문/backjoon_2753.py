def is_lear_year(year: int) -> bool:
    return bool(year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0))


def solution():
    year = int(input())
    return int(is_lear_year(year))


if __name__ == "__main__":
    print(solution())