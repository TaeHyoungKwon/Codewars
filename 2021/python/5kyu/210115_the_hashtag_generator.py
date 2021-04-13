import unittest

MAX_LENGTH = 140


def generate_hashtag(s):
    if not s:
        return False

    hash_tag = f"#{''.join(word.capitalize() for word in s.strip().split())}"
    if len(hash_tag) > MAX_LENGTH:
        return False

    return hash_tag


class TestGenerateHashTag(unittest.TestCase):
    def test_generate_hashtag_with_empty_string(self):
        self.assertFalse(generate_hashtag(s=""))

    def test_generate_hashtag_with_common_case(self):
        self.assertEqual(generate_hashtag(s="Codewars Is Nice"), "#CodewarsIsNice")

    def test_generate_hashtag_with_too_long(self):
        self.assertFalse(generate_hashtag(s="TooLong" * 100))
