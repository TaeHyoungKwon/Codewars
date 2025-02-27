loop = int(input())
targets = [input() for _ in range(loop)]
print(next(target for target in targets if "S" in target))
