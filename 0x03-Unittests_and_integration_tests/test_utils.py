#!/usr/bin/env python3
"""
A module for testing the utils module.
"""
import unittest
#from typing import Dict, Tuple, Union
#from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map #(
    #access_nested_map,
    #get_json,
    #memoize,
#)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    
    """Decorator that lets us run the test with different inputs and expected outputs."""
    @parameterized.expand([
        (nested_map := {"a": 1}, path := ("a",), expected := 1),
        (nested_map := {"a": {"b": 2}}, path := ("a",), expected := {"b": 2}),
        (nested_map := {"a": {"b": 2}}, path := ("a", "b"), expected := 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
            # self,
            # nested_map: '''Dict''',
            # path: '''Tuple[str]''',
            # expected: '''Union[Dict, int]''',
            # ):'''-> None:'''
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)