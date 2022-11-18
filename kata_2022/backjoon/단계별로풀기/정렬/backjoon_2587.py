def solution():
    temp = []
    for _ in range(5):
        temp.append(int(input()))

    print(sum(temp) // len(temp))
    print(sorted(temp)[2])


if __name__ == "__main__":
    solution()
