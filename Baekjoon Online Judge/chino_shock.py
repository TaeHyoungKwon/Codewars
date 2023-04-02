def solution(emoji: str) -> int:
    return len(emoji) + emoji.count(":") + emoji.count("_") * 5


if __name__ == "__main__":
    print(solution(emoji=input()))
