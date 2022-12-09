def solution():
    return "S" if all(bit in "01" for bit in input().split()) else "F"


if __name__ == "__main__":
    print(solution())
