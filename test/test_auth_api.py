# coding: utf-8

"""
    Combined FCSM EOS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import fcsm_eos_api_client
from fcsm_eos_api_client.api.auth_api import AuthApi  # noqa: E501
from fcsm_eos_api_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = fcsm_eos_api_client.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_external_provider(self):
        """Test case for add_external_provider

        """
        pass

    def test_delete_external_provider(self):
        """Test case for delete_external_provider

        """
        pass

    def test_get_external_provider(self):
        """Test case for get_external_provider

        """
        pass

    def test_get_external_providers(self):
        """Test case for get_external_providers

        """
        pass

    def test_login(self):
        """Test case for login

        """
        pass


if __name__ == '__main__':
    unittest.main()
