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
from fcsm_eos_api_client.api.tag_api import TagApi  # noqa: E501
from fcsm_eos_api_client.rest import ApiException


class TestTagApi(unittest.TestCase):
    """TagApi unit test stubs"""

    def setUp(self):
        self.api = fcsm_eos_api_client.api.tag_api.TagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag(self):
        """Test case for create_tag

        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        """
        pass

    def test_get_tag(self):
        """Test case for get_tag

        Returns the specified tag  # noqa: E501
        """
        pass

    def test_get_tags(self):
        """Test case for get_tags

        """
        pass

    def test_update_tag(self):
        """Test case for update_tag

        """
        pass


if __name__ == '__main__':
    unittest.main()