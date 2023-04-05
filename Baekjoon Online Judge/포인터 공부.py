def solution(target: int) -> str:
    result = []
    result.append(f"int a;")
    second = "ptr"

    for idx in range(1, target + 1):
        if idx == 1:
            result.append(f"int *{second} = &a;")
            continue

        first = second
        second = "ptr"
        if idx == 2:
            expression = f"int {'*' * idx}{first}{idx} = &{second};"
        else:
            expression = f"int {'*' * idx}{first}{idx} = &{second}{idx-1};"
        result.append(expression)
    return "\n".join(result)


if __name__ == "__main__":
    target = int(input())
    print(solution(target))
