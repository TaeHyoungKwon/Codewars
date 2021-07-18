import unittest
from typing import Generator


class Plubboard:
    def __init__(self, wires=None):
        self.wires = {}
        if wires is None:
            return

        if len(wires) > 20:
            raise

        for chunk in self._chunks(wires, 2):
            first, second = chunk
            self.wires[first] = second
            self.wires[second] = first

    def process(self, c):
        return self.wires.get(c, c)

    def _chunks(self, string: str, n: int) -> Generator:
        """https://stackoverflow.com/a/312464"""
        for i in range(0, len(string), n):
            yield string[i : i + n]


class TestPlubboard(unittest.TestCase):
    def test_process(self):
        plugboard = Plubboard("AB")
        self.assertEqual(plugboard.process("A"), "B")

    def test_process_with_empty_wires(self):
        plugboard = Plubboard({})
        self.assertEqual(plugboard.process("A"), "B")
