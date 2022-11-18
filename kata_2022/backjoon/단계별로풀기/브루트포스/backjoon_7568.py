def solution():
    cases_count = int(input())
    people_size_info_list = [list(map(int, input().split())) for _ in range(cases_count)]

    ranking_table = {}
    for index, people_size_info in enumerate(people_size_info_list):
        ranking_table[index] = 1
        weight, height = people_size_info
        for target_people_size_info in people_size_info_list:
            target_weight, target_height = target_people_size_info
            if target_weight > weight and target_height > height:
                ranking_table[index] += 1
    return " ".join(str(rank) for rank in ranking_table.values())


if __name__ == "__main__":
    print(solution())
