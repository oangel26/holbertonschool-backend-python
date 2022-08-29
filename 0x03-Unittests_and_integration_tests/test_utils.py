#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """
    Class wich tests unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
