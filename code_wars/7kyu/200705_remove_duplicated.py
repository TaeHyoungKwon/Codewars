def unique(integers):
    temp = []
    for ele in integers:
        if ele not in temp:
            temp.append(ele)
    return temp


def test_unique_should_return_empty_list_when_given_integers_is_empty_list():
    assert unique(integers=[]) == []


def test_unique_with_not_any_duplicated_element():
    assert unique(integers=[5, 2, 1, 3]) == [5, 2, 1, 3]


def test_unique_with_duplicated_element():
    assert unique(integers=[1, 5, 2, 0, 2, -3, 1, 10]) == [1, 5, 2, 0, -3, 10]
