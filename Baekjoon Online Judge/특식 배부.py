def solution(maximum_count: int, soldiers_count: list[int]) -> int:
    return sum(
        soldier_count if soldier_count <= maximum_count else maximum_count
        for soldier_count in soldiers_count
    )


if __name__ == "__main__":
    print(
        solution(
            maximum_count=int(input()),
            soldiers_count=[int(soldier_count) for soldier_count in input().split()],
        )
    )
