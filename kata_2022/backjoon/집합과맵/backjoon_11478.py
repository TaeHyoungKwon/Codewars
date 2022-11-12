def solution():
    target_strings = input()
    return len(
        {
            target_strings[i : j + 1]
            for i in range(len(target_strings))
            for j in range(i, len(target_strings))
        }
    )


if __name__ == "__main__":
    print(solution())
