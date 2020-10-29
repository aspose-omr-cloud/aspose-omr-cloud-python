# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_omr.py">
# Copyright (c) 2020 Aspose.OMR for Cloud
# </copyright>
# <summary>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from __future__ import absolute_import

import unittest

import os
import json

from test.test_helper import TestHelper
from asposeomrcloud.configuration import Configuration
from asposeomrcloud.apis.omr_api import OmrApi
from asposeomrcloud.apis.storage_api import StorageApi
import demo.omr_demo as omr_demo


class TestOmr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.helper = TestHelper
        cls.configuration = Configuration(
            apiKey=cls.helper.get_app_key(),
            appSid=cls.helper.get_app_sid())
        cls.omr_api = OmrApi(cls.configuration)
        cls.storage_api = StorageApi(cls.configuration)
        cls.path = TestHelper.path_to_output
        cls.image_path = TestHelper.template_image_path
        cls.data_dir = TestHelper.data_dir
        cls.template_dst_name = TestHelper.template_dst_name
        cls.folder = TestHelper.logos_folder_name
        cls.user_images = TestHelper.template_user_images_names

    ###############################################################
    #                          All Tests                          #
    ###############################################################

    def test_1_generate_template(self):
        # Upload logo images used during template generation in a separate folder on cloud storage
        omr_demo.upload_demo_files(self.storage_api, self.data_dir)

        # Generate new template based on provided text description
        path = os.path.join(self.data_dir, self.template_dst_name)
        res_gen = omr_demo.generate_template(self.omr_api, self.storage_api, path, self.folder)

        self.assertTrue(res_gen.error_code == 0, "Template was not generated")
        self.assertTrue(res_gen.payload != '', "Template was not generated")

        res_des = omr_demo.deserialize_files(res_gen.payload.result.response_files, self.path)

        self.assertTrue(res_des != '', 'File is non deserialized')

    def test_2_correct_template(self):
        corrected_template_path = ''
        # Run template correction
        res_cr = omr_demo.correct_template(self.omr_api, self.storage_api, self.image_path, self.path)

        self.assertTrue(res_cr.error_code == 0, "Image was not corrected")
        self.assertTrue(res_cr.payload != '', "Image was not corrected")

        for file_info in res_cr.payload.result.response_files:
            response_file_local_path = omr_demo.deserialize_file(file_info, self.path)

            self.assertTrue(response_file_local_path != '', 'File is non deserialized')

            if file_info.name.lower().endswith('.omrcr'):
                corrected_template_path = response_file_local_path

        data = {'corrected_template_path': corrected_template_path,
                'template_id': res_cr.payload.result.template_id}

        json_string = json.dumps(data)
        f = open("temp_file.txt", "w")
        f.write(json_string)
        f.close()

    def test_3_finalize_template(self):
        f = open("temp_file.txt", "r")
        tmp = f.read()
        var = json.loads(tmp)
        f.close()
        # Run template finalization
        res_fin = omr_demo.finalize_template(self.omr_api, self.storage_api, var['template_id'],
                                             var['corrected_template_path'])

        self.assertTrue(res_fin.error_code == 0, "Template was not finalization")
        self.assertTrue(res_fin.payload != '', "Template was not finalization")

    def test_4_recognize_image(self):
        f = open("temp_file.txt", "r")
        tmp = f.read()
        var = json.loads(tmp)
        f.close()
        # Runs mark recognition on image
        for user_image in self.user_images:
            res_rec = omr_demo.recognize_image(self.omr_api, self.storage_api,
                                               var['template_id'], os.path.join(self.data_dir, user_image))

            res_des = omr_demo.deserialize_files(res_rec.payload.result.response_files, self.path)

            self.assertTrue(res_des != '', 'File is non deserialized')

        self.assertTrue(res_rec.error_code == 0, "Image was not corrected")
        self.assertTrue(res_rec.payload != '', "Image was not corrected")

        os.remove("temp_file.txt")






