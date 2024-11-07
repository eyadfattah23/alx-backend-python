#!/usr/bin/env python3
'''
Create unittests for utils file
'''

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize

from typing import (
    Mapping,
    Callable,
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


class TestGetJson(TestCase):
    """test that utils.get_json returns the expected result."""

    @patch('requests.get')
    def test_get_json(self, mock_get_json: Callable):
        """test that utils.get_json returns the expected result.

        Args:
            url (_type_): _description_
            mock_get_json (_type_): _description_
        """
        mock_response = Mock()
        test_url = "http://example.com"
        test_payload = {"payload": True}

        mock_response.json.return_value = test_payload
        mock_get_json.return_value = mock_response

        data = get_json(test_url)
        mock_get_json.assert_called_with(test_url)

        self.assertEqual(data, test_payload)

        test_url = "http://holberton.io"
        test_payload = {"payload": False}

        mock_response.json.return_value = test_payload
        mock_get_json.return_value = mock_response

        data = get_json(test_url)
        mock_get_json.assert_called_with(test_url)

        self.assertEqual(data, test_payload)


class TestMemoize(TestCase):
    """test that utils.memoize returns the expected results."""

    def test_memoize(self):
        """test that memoize returns the expected results."""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            inst = TestClass()

            one = inst.a_property
            two = inst.a_property
            # no () because memoize returns a property

            mock_a_method.assert_called_once()
