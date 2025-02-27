n, _ = map(int, input().split())
print(sum(1 for problem in [input() for _ in range(n)] if problem.count("O") > problem.count("X")))
