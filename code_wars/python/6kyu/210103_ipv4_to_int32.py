import unittest


def ip_to_int32(ip: str) -> int:
    return int(''.join(bin(int(octet))[2:].zfill(8) for octet in ip.split('.')), 2)


class TestIPToInt32(unittest.TestCase):
    def test_ip_to_int32(self):
        self.assertEqual(ip_to_int32("128.32.10.1"), 2149583361)
