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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
            # self,
            # nested_map: Dict,
            # path: Tuple[str],
            # exception: Exception,
            # ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


'''class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()'''
