VOWELS = "aeiou"


def solution(input_word: str) -> int:
    return sum(character in VOWELS for character in input_word)


if __name__ == "__main__":
    _ = int(input())
    print(solution(input()))
