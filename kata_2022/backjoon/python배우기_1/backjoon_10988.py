def solution():
    target_word = input()
    return int(target_word == target_word[::-1])


if __name__ == "__main__":
    print(solution())
