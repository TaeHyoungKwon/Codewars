def curve(chars: str, generations: int):
    if generations == 0:
        print(chars)
        return

    for char in chars:
        if char == "X":
            curve("X+YF", generations - 1)
        elif char == "Y":
            curve("X+YF", generations - 1)
        else:
            print(char)


if __name__ == "__main__":
    t = "FX+YF"
    length = len(t)
    print(curve("FX+YF", 1))
