import unittest


class Block:
    def __init__(self, block_info):
        self.width, self.length, self.height = block_info

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def get_volume(self):
        return self.length * self.height * self.width

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)


class TestBuildingBlock(unittest.TestCase):
    def test_building_block_with_get_width(self):
        self.assertEqual(Block([10, 10, 10]).get_width(), 10)

    def test_building_block_with_get_height(self):
        self.assertEqual(Block([10, 10, 10]).get_height(), 10)

    def test_building_block_with_get_length(self):
        self.assertEqual(Block([10, 10, 10]).get_length(), 10)

    def test_building_block_with_get_volume(self):
        self.assertEqual(Block([10, 10, 10]).get_volume(), 1000)

    def test_building_block_with_get_surface(self):
        self.assertEqual(Block([10, 10, 10]).get_surface_area(), 600)
