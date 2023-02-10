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

from aspose_omr_cloud_sdk import ApiClient, GenerateTemplateApi, PageSettings, OmrGenerateTask, Configuration, \
    OMRResponse
from test.common import Common


class GenerateTemplateApiTests(unittest.TestCase):
    """GenerateTemplateApi unit test stubs"""

    def tearDown(self):
        pass


    def test_generate_template(self):
        common = Common();
        url = common.GetURL();
        configuration = Configuration(hostUrl=url)
        apiClient = ApiClient(configuration=configuration);
        # Create an instance of GenerateTemplateApi class
        instance = GenerateTemplateApi(apiClient);
        templateLogosImagesNames = ["logo1.jpg", "logo2.png"];
        # Read the template source code
        with open(os.path.join(common.GetDataFolderDir(),"Aspose_test.txt"), 'r+b') as f:
            image = base64.b64encode(f.read()).decode('utf-8')

        # Configure the page layout
        settings = PageSettings(font_size=12, font_family="Segoe UI", font_style="Regular", paper_size="A4",
                                bubble_color="Black", page_margin_left=210, orientation="Vertical",
                                bubble_size="Normal", output_format="Png")

        # Load images used in the template
        # images = dict()
        if templateLogosImagesNames is not None:
            case_list = {}
            for logo_name in templateLogosImagesNames:
                with open(os.path.join(common.GetDataFolderDir(), logo_name), 'r+b') as f:
                    logo = base64.b64encode(f.read()).decode('utf-8')
                    name = ntpath.basename(logo_name)
                    item = {name, logo}
                case_list[name] = logo
        # images.update(case_list)
        # Build request
        task = OmrGenerateTask(image, settings, case_list)
        kwargs = {"body": task};
        # Put the request into queue
        templateId = instance.post_generate_template(**kwargs)
        self.assertTrue(templateId != "")

        generationResult = OMRResponse()
        while True:
            kwargs = {"id": templateId};
            generationResult = instance.get_generate_template(**kwargs)
            if generationResult.response_status_code == "Ok":
                break
            elif generationResult.response_status_code == "Error":
                raise Exception("Something went wrong ...", generationResult.Error)
            else:
                print("Please wait while we are processing your request...")
                time.sleep(5)


        self.assertEqual(generationResult.response_status_code,"Ok");
        self.assertTrue(generationResult.error == None);
        self.assertTrue(len(generationResult.results) > 1);
        """Test case for get_generate_template

        """
        pass



if __name__ == '__main__':
    unittest.main()
