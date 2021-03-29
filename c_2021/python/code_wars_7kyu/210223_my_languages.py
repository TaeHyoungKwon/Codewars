import unittest


def my_languages(results):
    my_languages = [(language, score) for language, score in results.items() if score >= 60]
    sorted_by_score = sorted(my_languages, key=lambda x: x[1], reverse=True)
    return [language for language, _ in sorted_by_score]


# def my_languages(results):
#     return sorted([lang for lang, score in results.items() if score >= 60], key=results.get, reverse=True)
#
    
class TestMyLanguages(unittest.TestCase):
    def test_my_languages(self):
        self.assertEqual(my_languages(results={"Java": 10, "Ruby": 80, "Python": 65}), ["Ruby", "Python"])
