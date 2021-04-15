import unittest


def grader(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
    
    
class TestGrader(unittest.TestCase):
    def test_grader_with_c(self):
        self.assertEqual(grader(score=0.7), "C")

    def test_grader_with_d(self):
        self.assertEqual(grader(score=0.6), "D")

    def test_grader_with_f(self):
        self.assertEqual(grader(score=0.5), "F")

    def test_grader_with_a(self):
        self.assertEqual(grader(score=0.9), "A")

    def test_grader_with_b(self):
        self.assertEqual(grader(score=0.8), "B")
