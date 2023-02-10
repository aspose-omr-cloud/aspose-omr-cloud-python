# coding: utf-8

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


import base64
import ntpath
import unittest
import os
import time

from aspose_omr_cloud_sdk import ApiClient, PageSettings, OmrGenerateTask, Configuration, \
    OMRResponse, RecognizeTemplateApi, OmrRecognizeTask, FileExtension
from test.common import Common


class TestRecognizeTemplateApi(unittest.TestCase):
    """RecognizeTemplateApi unit test stubs"""

    def tearDown(self):
        pass

    def test_recognize_template(self):
        common = Common();
        url = common.GetURL();
        configuration = Configuration(hostUrl=url)
        apiClient = ApiClient(configuration=configuration);
        # Create an instance of GenerateTemplateApi class
        instance = RecognizeTemplateApi(apiClient);
        # Read the recognition pattern file
        with open(os.path.join(common.GetResultFolderDir(),"Aspose_test.omr"), 'r+b') as f:
            omrFile = base64.b64encode(f.read()).decode('utf-8')

        # Set the recognition accuracy
        # Lower value allow even the lightest marks to be recognized
        # Higher value require a more solid fill and may cause pencil marks to be ignored
        recognitionThreshold = 30

        # Read the filled form
        with open(os.path.join(common.GetDataFolderDir(),"Aspose_test.jpg"), 'r+b') as f:
            image = base64.b64encode(f.read()).decode('utf-8')
        images = [image]

        # Build request
        task = OmrRecognizeTask(images, omrFile, FileExtension.CSV, recognitionThreshold)

        # Put the request into queue
        kwargs = {"body": task}
        templateId = instance.post_recognize_template(**kwargs)
        self.assertTrue(templateId != "")

        recognitionResult = OMRResponse()
        while True:
            kwargs = {"id": templateId};
            recognitionResult = instance.get_recognize_template(**kwargs)
            if recognitionResult.response_status_code == "Ok":
                break
            elif recognitionResult.response_status_code == "Error":
                raise Exception("Something went wrong ...", recognitionResult.Error)
            else:
                print("Please wait while we are processing your request...")
                time.sleep(5)

        self.assertEqual(recognitionResult.response_status_code, "Ok");
        self.assertTrue(recognitionResult.error == None);
        self.assertTrue(len(recognitionResult.results) > 0);
        """Test case for get_recognize_template

        """
        pass



if __name__ == '__main__':
    unittest.main()
