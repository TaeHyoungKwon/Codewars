def get_pocket_monster_map(poket_monsters_count: int) -> dict:
    pocket_monster_map = {}
    for index in range(1, poket_monsters_count + 1):
        pocket_monster = input()
        str_index = str(index)
        pocket_monster_map[str_index] = pocket_monster
        pocket_monster_map[pocket_monster] = str_index
    return pocket_monster_map


def solution():
    poket_monsters_count, my_poket_monsters_count = map(int, input().split())

    pocket_monster_map = get_pocket_monster_map(poket_monsters_count)
    my_pocket_monsters = [input() for _ in range(my_poket_monsters_count)]

    return "\n".join(pocket_monster_map[my_pocket_monster] for my_pocket_monster in my_pocket_monsters)


if __name__ == "__main__":
    print(solution())
