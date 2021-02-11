import unittest
from urllib.parse import urlparse


def domain_name(url):
    grouped_url = urlparse(url)
    if not grouped_url.netloc:
        return grouped_url.path.split('.')[1]
    return grouped_url.netloc.split('.')[0]
    
    
class TestDomainName(unittest.TestCase):
    def test_domain_name(self):
        url = "www.xakep.ru"
        actual = domain_name(url)
        self.assertEqual(actual, 'xakep')
