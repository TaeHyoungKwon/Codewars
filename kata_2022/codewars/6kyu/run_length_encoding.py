from itertools import groupby


def run_length_encoding(s):
    return [[sum(True for _ in group), key] for key, group in groupby(s)]


class TestRunLengthEncoding:
    def test_run_length_encoding(self):
        assert run_length_encoding(s="abc") == [[1, "a"], [1, "b"], [1, "c"]]
