def solution(character: str) -> str:
    if character == "M":
        return "MatKor"
    elif character == "W":
        return "WiCys"
    elif character == "C":
        return "CyKor"
    elif character == "A":
        return "AlKor"
    else:
        return "$clear"


character = input()
print(solution(character))
