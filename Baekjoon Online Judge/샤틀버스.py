def solution(x: int, y: int):
    if x == y:
        return x

    if x > y:
        return x + y
    else:
        return y - x


if __name__ == "__main__":
    print(solution(*map(int, (input().split()))))
