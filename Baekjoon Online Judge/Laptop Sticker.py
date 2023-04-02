def solution(laptop_w, laptop_h, sticker_w, sticker_h) -> int:
    return 1 if laptop_w - sticker_w >= 2 and laptop_h - sticker_h >= 2 else 0


if __name__ == "__main__":
    print(solution(*map(int, input().split())))
