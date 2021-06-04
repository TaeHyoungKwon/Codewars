import unittest
from typing import Dict, List, Optional, Union


def populate_dict(key: List[Union[str, int]], default: Optional[Union[str, int]]) -> Dict[str, int]:
    return dict.fromkeys(key, default)
    
    
class TestPopulateDict(unittest.TestCase):
    def test_populate_dict(self):
        self.assertEqual(populate_dict(key=["draft", "completed"], default=0), {"completed": 0, "draft": 0})
        