# -*- coding: utf-8 -*-
"""Test Suite module for configs"""


import pytest


SKIP_CONFIG = False
SKIP_CONFIG_MSG = "Test suite for config is SKIPPED"


class TestConfig(object):
    """Test suite for check configuration files"""

    # Test constants
    PATH_SETTINGS = "bdocguildmanager/configs/settings.json"

    def test_config_exist(self):
        """Test : test_000_config_exist"""
        return True

    @pytest.mark.parametrize("key_name", [])
    def test_config_keys(self, key_name):
        """TODO: doc method"""
        if SKIP_CONFIG:
            pytest.skip(msg=SKIP_CONFIG_MSG)
        # key validation stuff here
        return True
