def solution(jinho_mbti: str, friend_mbtis: list[str]):
    return friend_mbtis.count(jinho_mbti)


if __name__ == "__main__":
    jinho_mbti = input()
    friend_count = int(input())
    friend_mbtis = [input() for _ in range(friend_count)]

    print(solution(jinho_mbti, friend_mbtis))
