def solution(energy_wook: int, energy_je: int) -> float:
    return 1 / (1 + 10 ** ((energy_je - energy_wook) / 400))


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
