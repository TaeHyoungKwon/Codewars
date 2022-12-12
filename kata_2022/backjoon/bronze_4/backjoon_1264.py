VOWELS = "aeiouAEIOU"


def solution():
    result = []
    while (target_strings := input()) != "#":
        result.append(sum(char in VOWELS for char in target_strings))
    return "\n".join(map(str, result))


if __name__ == "__main__":
    print(solution())
