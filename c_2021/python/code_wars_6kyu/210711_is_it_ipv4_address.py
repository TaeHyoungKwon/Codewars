import unittest


def ipv4_address(address):
    split_address = address.split(".")
    if len(split_address) != 4:
        return False
    for part in split_address:
        if not part.isdigit():
            return False
        if part != str(int(part)):
            return False
        if not (0 <= int(part) <= 255):
            return False
    return True


class TestAddress(unittest.TestCase):
    def test_ipv2_address_on_true(self):
        self.assertTrue(ipv4_address(address="127.0.0.1"))

    def test_ipv2_address_on_false(self):
        self.assertFalse(ipv4_address(address="257.0.0.1"))

    def test_ipv2_address_on_edge(self):
        self.assertFalse(ipv4_address(address="10.20.030.40"))

    def test_ipv2_address_on_edge_2(self):
        self.assertTrue(ipv4_address(address="0.0.0.0"))

    def test_ipv2_address_on_edge_3(self):
        self.assertFalse(ipv4_address(address="127.0.0.0.1"))

    def test_ipv2_address_on_edge_4(self):
        self.assertFalse(ipv4_address(address="127.0.0.1 "))

    def test_ipv2_address_on_edge_5(self):
        self.assertFalse(ipv4_address(address="221.146.249.302"))
