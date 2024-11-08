#!/usr/bin/env python3
"""A module for testing the utility functions in the `utils` module.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function,
    which accesses nested dictionary values
    using a specified path (tuple of keys).
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """Tests that `access_nested_map`
        correctly accesses values in a nested dictionary."""

        # Assert that the function returns the
        # expected value when accessing the path
        self.assertEqual(access_nested_map(nested_map,
                                           path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        """Tests that `access_nested_map` raises the correct
        exception when the path is invalid."""

        # Assert that the expected exception is raised
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function, which fetches
    JSON data from a URL."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict) -> None:
        """Tests that `get_json` correctly returns the
        JSON data fetched from the URL."""

        # Mock the requests.get method to
        # return a predefined payload
        attrs = {'json.return_value': test_payload}
        with patch("requests.get",
                   return_value=Mock(**attrs)) as req_get:

            # Assert that `get_json` returns the correct payload
            self.assertEqual(get_json(test_url), test_payload)

            # Ensure that the requests.get method
            # was called with the correct URL
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` decorator function,
    which caches the return value of a method
    to avoid redundant calculations.
    """

    def test_memoize(self) -> None:
        """Tests that the `memoize` decorator
        correctly caches method results."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock the `a_method` to return 42,
        # but ensure it is only called once
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as memo_fxn:
            test_class = TestClass()

            self.assertEqual(test_class.a_property(), 42)

            self.assertEqual(test_class.a_property(), 42)

            # Assert that `a_method` was only called once
            memo_fxn.assert_called_once()
