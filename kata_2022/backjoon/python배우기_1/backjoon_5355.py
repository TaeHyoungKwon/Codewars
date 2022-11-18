def solution():
    case_count = int(input())
    expressions = [input().split() for _ in range(case_count)]

    result = []
    for expression in expressions:
        number = 0
        for index, char in enumerate(expression):
            if index == 0:
                number = float(char)

            if char == "@":
                number *= 3
            elif char == "%":
                number += 5
            elif char == "#":
                number -= 7
        result.append(f"{number:.2f}")
    return "\n".join(str(value) for value in result)


if __name__ == "__main__":
    print(solution())
