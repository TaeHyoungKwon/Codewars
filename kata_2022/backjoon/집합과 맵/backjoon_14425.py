def get_string_set_list_by_count(input_count: int) -> list[str]:
    return [input() for _ in range(input_count)]


def solution() -> int:
    string_set_count, target_set_count = map(int, input().split())

    string_set = get_string_set_list_by_count(input_count=string_set_count)
    target_set = get_string_set_list_by_count(input_count=target_set_count)

    return sum(target in string_set for target in target_set)


if __name__ == "__main__":
    print(solution())
