t = int(input())

for _ in range(t):
    result = []

    vote = int(input())
    five_votes, one_vote = divmod(vote, 5)

    for _ in range(five_votes):
        result.append("++++")
    result.append("|" * one_vote)

    print(" ".join(result))
