# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

"""
A class wrapping the Azure App Configuration client to get configurations
for each instance of the API.
"""
import logging
import os

from server_api_config import APP_CONFIG_CONNECTION_STR, API_INSTANCE_NAME

from azure.appconfiguration import AzureAppConfigurationClient


log = logging.getLogger(os.environ['FLASK_APP'])


class AppConfig:
    """Wrapper around the Azure App Configuration client"""

    def __init__(self):
        self.client = AzureAppConfigurationClient.from_connection_string(APP_CONFIG_CONNECTION_STR)

        self.api_instance = API_INSTANCE_NAME

    def get_allowlist(self):
        return ['camelotproject.org']
