#!/usr/bin/env python3
'''Unittests for client file'''
from parameterized import parameterized, parameterized_class
from unittest import TestCase, main
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from utils import get_json
from typing import (Callable, Dict)
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient class
    """
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')  # where it's used not where it's defined
    def test_org(self, org: str, mock_org: Callable):
        """test org property/method in GithubOrgClient.

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
    def test_public_repos(self, mock_get_json: Callable):
        """Test that the list of repos is what's expected.
            by testing public_repos method.
        """
        mock_get_json.return_value = [{'id': 193671, 'name': 'truth',
                                      'url':
                                          "api.github.com/repos/test/truth"},
                                      {'id': 123, 'name': 'lie',
                                      'url':
                                          "api.github.com/repos/test/lie"}]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = "api.github.com/orgs/test/repos"

            inst = GithubOrgClient('google')

            self.assertListEqual(["truth", "lie"], inst.public_repos())
            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool):
        """unit-test GithubOrgClient.has_license.
        """

        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"),
                     TEST_PAYLOAD
                     )
class TestIntegrationGithubOrgClient(TestCase):
    """test the GithubOrgClient.public_repos method in an integration test.
    """
    @classmethod
    def setUpClass(cls):
        """method called once before executing all tests.
            to Patch requests.get to use mock data.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """method called once after executing all tests.
        to stop patching requests.get.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public_repos method in an integration test.
                            (no external requests)
                        """
        client = GithubOrgClient('blablabla')

        # Check org payload
        self.assertEqual(client.org, self.org_payload)

        # Check repos payload
        self.assertEqual(client.repos_payload, self.repos_payload)

        # Test public_repos without a license filter
        self.assertListEqual(client.public_repos(), self.expected_repos)

        # Test public_repos with 'apache-2.0' license filter
        self.assertListEqual(client.public_repos(
            "apache-2.0"), self.apache2_repos)

        self.assertNotEqual(client.public_repos(
            "bsl-1.0"), self.apache2_repos)
        # print(client.public_repos('bsl-1.0')) -> ['cpp-netlib']
        self.assertEqual(client.public_repos(
            "eyad"), [])

        self.mock_get.assert_called()


if __name__ == "__main__":
    main()
