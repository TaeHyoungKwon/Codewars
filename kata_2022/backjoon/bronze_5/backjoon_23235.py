def solution():
    result = []
    index = 1
    while numbers := [int(number) for number in input().split()]:
        if len(numbers) == 1 and numbers[0] == 0:
            break
        result.append(f"Case {index}: Sorting... done!")
        index += 1
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
