def solution():
    result = []
    while True:
        first, second = map(int, input().split())
        if (first, second) == (0, 0):
            break

        result.append("Yes" if first > second else "No")

    return "\n".join(element for element in result)


if __name__ == "__main__":
    print(solution())
