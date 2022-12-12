def solution():
    n = int(input())
    return "\n".join(f"Hello World, Judge {index_}!" for index_ in range(1, n + 1))


if __name__ == "__main__":
    print(solution())
