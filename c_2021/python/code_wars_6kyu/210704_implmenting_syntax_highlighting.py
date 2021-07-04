from itertools import groupby
import unittest


HIGHLIGHT_MAP = {
    "F": '<span style="color: pink">',
    "L": '<span style="color: red">',
    "R": '<span style="color: green">',
    "NUM": '<span style="color: orange">'
}


def highlight(code):
    result = ""
    for _, group in groupby(code, key=lambda x: (x.isdigit(), x == "F", x == "R", x == "L")):
        group: str = "".join(group)
        first_ele = group[0]
        if first_ele.isdigit():
            result += f'{HIGHLIGHT_MAP["NUM"]}{group}</span>'
        elif first_ele in {"(", ")"}:
            result += group
        else:
            result += f'{HIGHLIGHT_MAP[first_ele]}{group}</span>'
    return result


class TestHighLight(unittest.TestCase):
    def test_highlight(self):
        self.assertEqual(
            highlight(code="F3RF5LF7"),
            '<span style="color: pink">F</span><span style="color: orange">3</span><span style="color: green">R</span><span style="color: pink">F</span><span style="color: orange">5</span><span style="color: red">L</span><span style="color: pink">F</span><span style="color: orange">7</span>',
        )

    def test_highlight_with_consecutive_element(self):
        self.assertEqual(
            highlight(code="FFFR345F2LL"),
            '<span style="color: pink">FFF</span><span style="color: green">R</span><span style="color: orange">345</span><span style="color: pink">F</span><span style="color: orange">2</span><span style="color: red">LL</span>'
        )

    def test_highlight_with_edge(self):
        self.assertEqual(
            highlight(code="RRRRR(F45L3)F2"),
            '<span style="color: green">RRRRR</span>(<span style="color: pink">F</span><span style="color: orange">45</span><span style="color: red">L</span><span style="color: orange">3</span>)<span style="color: pink">F</span><span style="color: orange">2</span>'
        )


"""
조건
1. F, L, R
    * F -> <span style="color: pink"> </span>
    * L -> <span style="color: red"> </span>
    * R -> <span style="color: green"> </span>
2. 0 - 9
    * <span sylte="color": orange"> </span>
3. ( , )
    * pass
"""