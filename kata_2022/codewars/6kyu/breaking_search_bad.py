from typing import List


def search(titles: List[str], term: str) -> List[str]:
    return [title for title in titles if term.lower() in title.lower()]


class TestSearch:
    SAMPLES = [
        "The Big Bang Theory",
        "How I Met Your Mother",
        "Dexter",
        "Breaking Bad",
        "Doctor Who",
        "The Hobbit",
        "Pacific Rim",
        "Pulp Fiction",
        "The Avengers",
        "Shining",
    ]

    def test_search_on_success(self):
        assert search(titles=self.SAMPLES, term="ho") == [
            "How I Met Your Mother",
            "Doctor Who",
            "The Hobbit",
        ]

        assert search(titles=self.SAMPLES, term="exte") == ["Dexter"]


"""
문제
    - titles 중에 term에 match 되는 요소가 있다면, sequence 형태로 리턴해라
해결
    - list 내에서 term에 match 되는 요소가 있는지 확인하여 sequence를 리턴한다
테스트
1. 성공
    - 일반적인 케이스
2. 실패
    - 없음
"""