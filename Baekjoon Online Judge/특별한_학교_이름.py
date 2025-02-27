NLCS = "North London Collegiate School"
BHA = "Branksome Hall Asia"
KIS = "Korea International School"
SJA = "St. Johnsbury Academy"


def solution(input_word: str) -> str:
    if input_word == "NLCS":
        return NLCS
    elif input_word == "BHA":
        return BHA
    elif input_word == "KIS":
        return KIS
    else:
        return SJA


input_word = input()
print(solution(input_word))
