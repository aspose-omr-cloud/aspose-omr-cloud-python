"""
 * Copyright (c) 2023 Aspose Pty Ltd. All Rights Reserved.
 *
 * Licensed under the MIT (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://github.com/aspose-omr-cloud/aspose-omr-cloud-dotnet/blob/master/LICENSE
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

from __future__ import absolute_import

import os
import json
import unittest

from aspose_omr_cloud_sdk import Configuration


class Common():
    demoDataSubmoduleName = "aspose-omr-cloud-demo-data"
    configFileName = "test_config.json"
    basePath = ""
    DataFolderName = "Data"
    ResultFolderName = "Temp"
    Config = ''
    ulr = ""

    def __init__(self):
        curr_path = os.path.abspath(os.path.dirname(os.path.realpath(os.getcwd())))
        config_file_relative_path = os.path.join(self.demoDataSubmoduleName, self.configFileName)

        while curr_path != os.path.abspath(os.path.join(curr_path, os.pardir)) and not os.path.isfile(
                os.path.join(curr_path, config_file_relative_path)):
            curr_path = os.path.abspath(os.path.join(curr_path, os.pardir))
            if os.path.isfile(os.path.join(curr_path, config_file_relative_path)):
                config_file_path = os.path.join(curr_path, config_file_relative_path)
                with open(config_file_path) as f:
                    Config = json.loads(f.read())
            else:
                raise IOError("Can't find config file %s" % self.configFileName)
        self.basePath =os.path.join(curr_path,self.demoDataSubmoduleName)
        self.Config = Config

    def GetDataFolderDir(self):
        return os.path.join(self.basePath, self.DataFolderName)

    def GetResultFolderDir(self):
        return os.path.join(self.basePath, self.ResultFolderName)

    def GetURL(self):
        return self.Config["base_path"]