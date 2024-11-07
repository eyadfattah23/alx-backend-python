#!/usr/bin/env python3
'''Unittests for client file'''
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import Mock, patch
from client import GithubOrgClient
from utils import get_json
from typing import (Callable)


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient class
    """
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')  # where it's used not where it's defined
    def test_org(self, org: str, mock_org: Callable):
        """_summary_

        Args:
            mock_org (_type_): _description_
        """

        mock_resp = Mock()

        mock_resp.return_value = {'login': 'google', 'id': 1342004,
                                  'node_id':
                                      'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
                                  'url': 'https://api.github.com/orgs/google'}

        mock_org.return_value = mock_resp()
        client = GithubOrgClient(org)

        self.assertDictEqual({'login': 'google', 'id': 1342004,
                              'node_id': 'MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=',
                              'url': 'https://api.github.com/orgs/google'},
                             client.org)
        mock_org.assert_called_once_with(
            ''"https://api.github.com/orgs/{}".format(org))
