import unittest


def strip_url_params(url, params_to_strip=None):
    temp = {}
    split_url = url.split("?")
    print(split_url)
    if len(split_url) == 1:
        return split_url[0]

    uri, query_params = split_url

    for query_param in query_params.split("&"):
        k, v = query_param.split("=")
        if k not in temp:
            temp[k] = v

    if params_to_strip:
        for k in params_to_strip:
            temp.pop(k)
    if len(temp) == 0:
        return uri
    return uri + "?" + "&".join(f"{k}={v}" for k, v in temp.items())


class TestStripUrlParams(unittest.TestCase):
    def test_strip_url_params_no_params_to_strip_with_duplicated(self):
        self.assertEqual(strip_url_params(url="www.codewars.com?a=1&b=2&b=3"), "www.codewars.com?a=1&b=2")

    def test_strip_url_params_no_params_to_strip_with_no_duplicated(self):
        self.assertEqual(strip_url_params(url="www.codewars.com?a=1&b=2&c=3"), "www.codewars.com?a=1&b=2&c=3")

    def test_strip_url_params_params_to_strip_with_duplicated(self):
        self.assertEqual(
            strip_url_params(url="www.codewars.com?a=1&b=2&c=3&c=4", params_to_strip=["b"]), "www.codewars.com?a=1&c=3"
        )

    def test_strip_url_params_params_to_strip_with_no_duplicated(self):
        self.assertEqual(
            strip_url_params(url="www.codewars.com?a=1&b=2&c=3", params_to_strip=["b", "c"]), "www.codewars.com?a=1"
        )

    def test_strip_url_params_params_to_strip_with_no_duplicated(self):
        self.assertEqual(
            strip_url_params(url="www.codewars.com?b=2&c=3", params_to_strip=["b", "c"]), "www.codewars.com"
        )

    def test_strip_url_params_params_with_no_query_params(self):
        self.assertEqual(strip_url_params(url="www.codewars.com", params_to_strip=["b", "c"]), "www.codewars.com")


"""
문제
- url로 부터 겹치는 query string param을 삭제해라
해결
- ?를 기준으로 query string param 부분을 추출하고, 정규표현식으로 해당패턴을 필터링 하여서, 겹치는 부분은 제외하고 겹치는 문자는 삭제하고 다시 문자열을 만든다
조건
절차
1. url을 받아서, ?를 기준으로 query string param 부분을 추출한다
2. & 기준으로 split 하여서, query string과 값을 가진 리스트를 만든다
3. 2번의 리턴된 값을 받아서, dict를 만든다, 이미 키가 존재하면 무시한다
4. {"a": 1, "b": 2} 처럼 값을 가질 것인데, 
    option param이 없는 경우는 이 dict로 query param string 형태로 만든다
    option param이 있는 경우는 for loop를 돌면서, dict의 key를 삭제 해준 후, query param string 형태로 만든다 
테스트
option param이 없는 경우
    1. 중복된 경우
    2. 중복이 없는 경우
3. option param이 있는 경우
    1. 중복이 존재하는 경우
    2. 중복이 없는 경우
"""
