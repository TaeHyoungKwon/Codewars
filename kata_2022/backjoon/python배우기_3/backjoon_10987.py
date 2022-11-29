from collections import Counter


def solution():
    word_counter = Counter(input())
    return sum(value for key, value in word_counter.items() if key in "aeiou")


if __name__ == "__main__":
    print(solution())
