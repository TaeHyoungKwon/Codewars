def solution(burger_bread_count: int, patty_count: int) -> int:
    return min(burger_bread_count // 2, patty_count)


if __name__ == "__main__":
    print(solution(*map(int, input().split())))

