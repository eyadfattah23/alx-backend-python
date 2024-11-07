#!/usr/bin/env python3
'''Unittests for client file'''
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self):
        """test _public_repos_url property in GithubOrgClient.
        """

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "mock.github.com/repos",
                "login": "google",
                "id": 1342004,
                "is_verified": True
            }
            inst = GithubOrgClient('google')
            self.assertEqual("mock.github.com/repos", inst._public_repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what's expected.
            by testing public_repos method.
        """
        mock_get_json.return_value = [{'id': 193671, 'name': 'truth',
                                      'url':
                                          "api.github.com/repos/test/truth"},
                                      {'id': 123, 'name': 'lie',
                                      'url':
                                          "api.github.com/repos/test/lie"},]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = "api.github.com/orgs/test/repos"

            inst = GithubOrgClient('google')

            self.assertListEqual(["truth", "lie"], inst.public_repos())
            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once()
