def solution():
    bowls = input()

    height = 10
    prev = bowls[0]
    for bowl in bowls[1:]:
        if prev == "(":
            height += 5 if bowl == "(" else 10
        else:
            height += 10 if bowl == "(" else 5
        prev = bowl
    return height


if __name__ == "__main__":
    print(solution())
