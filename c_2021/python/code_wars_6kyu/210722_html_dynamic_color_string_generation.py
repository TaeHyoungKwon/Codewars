import random
import unittest

html_rgb_colors = [hex(i)[2:].zfill(2) for i in range(256)]


def generate_color_rgb():
    return f"#{''.join(random.choice(html_rgb_colors) for _ in range(3))}"


class TestGenerateColorRgb(unittest.TestCase):
    def test_generate_color_rgb(self):
        self.assertEqual(len(generate_color_rgb()), 7)
        self.assertEqual(generate_color_rgb()[0], "#")
