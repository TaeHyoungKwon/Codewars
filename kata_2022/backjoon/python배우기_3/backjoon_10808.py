import string


def solution():
    word = input()
    alphabet_map = dict.fromkeys(string.ascii_lowercase, 0)
    for char in word:
        alphabet_map[char] += 1
    return " ".join(map(str, alphabet_map.values()))


if __name__ == "__main__":
    print(solution())
