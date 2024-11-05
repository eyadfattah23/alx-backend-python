#!/usr/bin/env python3
'''
Create a TestAccessNestedMap unit test for utils.access_nested_map
'''

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map

from typing import (
    Mapping,
    Sequence
)


class TestAccessNestedMap(TestCase):
    """test that the method returns what it is supposed to.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)]
    )
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int):
        """test if access_nested_map returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a,")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """ test that a KeyError is raised with prev inputs

        Args:
            nested_map (Mapping)
            path (Sequence)
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
