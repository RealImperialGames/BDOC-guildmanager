# -*- coding: utf-8 -*-
"""Test Suite module for configs"""


from bdocguildmanager.files import settings

import pytest


SKIP_CONFIG = False
SKIP_CONFIG_MSG = "Test suite for config is SKIPPED"


class TestConfig(object):
    """Test suite for check configuration files"""

    def setup_method(self, test_method):
        """TODO: doc method"""
        super(TestConfig, self).setup_method(
            test_method,
            config=settings(file_path="bdocguildmanager/configs/"))

    # Test constants
    PATH_SETTINGS = "bdocguildmanager/configs/settings.json"

    def test_config_exist(self):
        """Test : test_000_config_exist"""
        self.assert_path_exist(self.PATH_SETTINGS, is_dir=False)

    @pytest.mark.parametrize("key_name", [])
    def test_config_keys(self, key_name):
        """TODO: doc method"""
        if SKIP_CONFIG:
            pytest.skip(msg=SKIP_CONFIG_MSG)
        # key validation stuff here
