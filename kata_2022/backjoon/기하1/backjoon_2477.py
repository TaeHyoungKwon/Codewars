COUNT = 6


def solution():
    melon_count = int(input())
    input_values = [input().split() for _ in range(COUNT)]
    directions = [int(v[0]) for v in input_values]
    lengths = [int(v[1]) for v in input_values]
    big_box_lengths, small_box_lengths = [], []

    for direction in directions:
        if directions.count(direction) == 1:
            big_box_lengths.append(lengths[directions.index(direction)])
            next_ = directions.index(direction) + 3
            if next_ >= 6:
                next_ -= 6
            small_box_lengths.append(lengths[next_])

    big_width, big_height = big_box_lengths
    small_width, small_height = small_box_lengths
    return melon_count * (big_width * big_height - small_width * small_height)


if __name__ == "__main__":
    print(solution())
