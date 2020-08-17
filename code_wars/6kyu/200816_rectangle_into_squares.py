import pytest


def sqInRect(lng, width):
    if lng == width:
        return None
    if lng < width:
        width, lng = lng, width
    res = []
    while lng != width:
        res.append(width)
        lng = lng - width
        if lng < width:
            width, lng = lng, width
    res.append(width)
    return res


@pytest.mark.parametrize("lng, width, expected", [(5, 5, None), [5, 3, [3, 2, 1, 1]]])
def test_sq_in_rect(lng, width, expected):
    sqInRect(lng, width) == expected
