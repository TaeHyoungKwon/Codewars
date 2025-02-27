"""
빨간색: 620nm 이상 780nm 이하
주황색: 590nm 이상 620nm 미만
노란색: 570nm 이상 590nm 미만
초록색: 495nm 이상 570nm 미만
파란색: 450nm 이상 495nm 미만
남색: 425nm 이상 450nm 미만
보라색: 380nm 이상 425nm 미만
"""


def solution(wavelength: int) -> str:
    if 620 <= wavelength <= 780:
        return "Red"
    elif 590 <= wavelength < 620:
        return "Orange"
    elif 570 <= wavelength < 590:
        return "Yellow"
    elif 495 <= wavelength < 570:
        return "Green"
    elif 450 <= wavelength < 495:
        return "Blue"
    elif 425 <= wavelength < 450:
        return "Indigo"
    elif 380 <= wavelength < 425:
        return "Violet"
    else:
        return "Invalid"


wavelength = int(input())
print(solution(wavelength))
