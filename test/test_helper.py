# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_helper.py">
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

import os
import json


class TestHelper(object):

    data_dir = os.path.abspath("Data")
    path_to_output = '.\\Temp'
    logos_folder_name = 'Logos'
    template_name = 'Aspose_test'
    template_dst_name = template_name + '.txt'
    template_image_name = template_name + '.png'
    template_image_path = os.path.join(path_to_output, template_image_name)
    template_user_images_names = ['photo.jpg', 'scan.jpg']
    template_logos_images_names = ['logo1.jpg', 'logo2.png']

    @classmethod
    def get_app_key(cls):
        f = open("test_config.json", "r")
        tmp = f.read()
        var = json.loads(tmp)
        return var['app_key']

    @classmethod
    def get_app_sid(cls):
        f = open("test_config.json", "r")
        tmp = f.read()
        var = json.loads(tmp)
        return var['app_sid']

