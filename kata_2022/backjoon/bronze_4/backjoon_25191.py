def solution(chicken_count: int, coke_count: int, beer_count: int) -> int:
    total_chicken_count_to_eat = coke_count // 2 + beer_count
    return (
        total_chicken_count_to_eat
        if total_chicken_count_to_eat < chicken_count
        else chicken_count
    )


if __name__ == "__main__":
    chicken_count = int(input())
    coke_count, beer_count = map(int, input().split())
    print(solution(chicken_count, coke_count, beer_count))
