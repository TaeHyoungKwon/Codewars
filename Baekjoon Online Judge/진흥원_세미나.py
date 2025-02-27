SEMINAR = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}


def solution(key: str) -> str:
    return SEMINAR[key]


loop = int(input())
for _ in range(loop):
    key = input()
    print(solution(key))
