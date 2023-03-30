def solution(positions: list[int], x: int, y: int, r: int) -> int:
    try:
        return positions.index(x) + 1
    except ValueError:
        return 0


if __name__ == "__main__":
    positions = list(map(int, input().split()))
    apple_info = list(map(int, input().split()))
    print(solution(positions, *apple_info))
