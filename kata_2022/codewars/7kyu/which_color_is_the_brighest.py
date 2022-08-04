"""
# Best Practices

def brightest(colors):
    return max(colors, key=lambda c:max(c[1:3], c[3:5], c[5:]))
"""


def brightest(colors):
    brightest_value = 0
    brightest_color = ""

    for color in colors:
        v = max(map(lambda x: int(x, 16), chunks(color[1:], 2)))
        if v > brightest_value:
            brightest_color = color
            brightest_value = v

    return brightest_color


def chunks(target, n):
    for i in range(0, len(target), n):
        yield target[i: i + n]


class TestBrightest:
    def test_brightest(self):
        assert brightest(colors=["#001000", "#000000"]) == "#001000"
        assert brightest(colors=["#ABCDEF", "#123456"]) == "#ABCDEF"
        assert brightest(colors=["#00FF00", "#FFFF00"]) == "#00FF00"
        assert brightest(colors=["#FFFFFF", "#1234FF"]) == "#FFFFFF"
        assert brightest(colors=["#FFFFFF", "#123456", "#000000"]) == "#FFFFFF"
