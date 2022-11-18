def solution():
    song_count, avg = map(int, input().split())
    return song_count * (avg - 1) + 1


if __name__ == "__main__":
    print(solution())
