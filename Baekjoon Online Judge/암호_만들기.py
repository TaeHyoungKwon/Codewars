from itertools import combinations

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def solution(l: int, target_alphabets: list[str]):
    sorted_target_alphabets = sorted(target_alphabets)

    result = []

    for combination in combinations(sorted_target_alphabets, l):
        if not _validate_conditions(combination):
            continue
        result.append("".join(combination))

    return "\n".join(result)


def _validate_conditions(combination: list[str]) -> bool:
    return (
        len(set(combination) & set(VOWELS)) >= 1
        and len(set(combination) & set(CONSONANTS)) >= 2
    )


if __name__ == "__main__":
    l, _ = list(map(int, input().split()))
    target_alphabets = input().split()
    print(solution(l, target_alphabets))
