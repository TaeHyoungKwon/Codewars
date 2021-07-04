import unittest


class Converter:
    @staticmethod
    def to_ascii(h):
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i : i + n]

        return "".join(chr(int(ele, 16)) for ele in list(chunks(h, 2)))

    @staticmethod
    def to_hext(s):
        return "".join(map(hex, map(ord, s))).replace("0x", "")


class TestConverter(unittest.TestCase):
    def test_converter_to_ascii(self):
        self.assertEqual(Converter.to_ascii(h="4c6f6f6b206d6f6d2c206e6f2068616e6473"), "Look mom, no hands")

    def test_converter_to_hex(self):
        self.assertEqual(Converter.to_hext(s="Look mom, no hands"), "4c6f6f6b206d6f6d2c206e6f2068616e6473")
