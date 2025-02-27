def solution(input_word: str) -> str:
    return {
        "SONGDO": "HIGHSCHOOL",
        "CODE": "MASTER",
        "2023": "0611",
        "ALGORITHM": "CONTEST",
    }[input_word]


print(solution(input()))
