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
from fcsm_eos_api_client.api.analytics_api import AnalyticsApi  # noqa: E501
from fcsm_eos_api_client.rest import ApiException


class TestAnalyticsApi(unittest.TestCase):
    """AnalyticsApi unit test stubs"""

    def setUp(self):
        self.api = fcsm_eos_api_client.api.analytics_api.AnalyticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metrics(self):
        """Test case for get_metrics

        """
        pass

    def test_get_operating_systems(self):
        """Test case for get_operating_systems

        """
        pass

    def test_get_platform_metrics(self):
        """Test case for get_platform_metrics

        """
        pass

    def test_get_platforms_usage(self):
        """Test case for get_platforms_usage

        """
        pass

    def test_get_summary(self):
        """Test case for get_summary

        """
        pass

    def test_get_summary_usage(self):
        """Test case for get_summary_usage

        """
        pass


if __name__ == '__main__':
    unittest.main()