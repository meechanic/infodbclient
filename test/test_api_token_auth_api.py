# coding: utf-8

"""
    Snippets API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import infodbclient
from infodbclient.api.api_token_auth_api import ApiTokenAuthApi  # noqa: E501
from infodbclient.rest import ApiException


class TestApiTokenAuthApi(unittest.TestCase):
    """ApiTokenAuthApi unit test stubs"""

    def setUp(self):
        self.api = infodbclient.api.api_token_auth_api.ApiTokenAuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_token_auth_create(self):
        """Test case for api_token_auth_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
