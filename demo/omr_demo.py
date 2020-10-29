# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_demo.py">
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
from __future__ import absolute_import, unicode_literals

import base64
import json
import os
from warnings import warn

import six

import asposeomrcloud.apis.storage_api as storage_api
from asposeomrcloud.configuration import Configuration
from asposeomrcloud.apis.omr_api import OmrApi
from asposeomrcloud.models import OmrFunctionParam

from collections import OrderedDict

# File with dictionary for configuration in JSON format
# The config file should look like:
# {
#     "app_key"  : "xxx",
#     "app_sid"   : "xxx-xxx-xxx-xxx-xxx",
#     "base_path" : "https://api.aspose.cloud/v3.0",
#     "data_folder" : "Data"
# }
# Provide your own app_key and app_sid, which you can receive by registering at Aspose Cloud Dashboard
# https://dashboard.aspose.cloud/


CONFIG = 'test_config.json'
DEMO_DATA_SUBMODULE_NAME = 'demo-data'
# Output path where all results are placed
PATH_TO_OUTPUT = '.\\Temp'
# Name of the folder where all images used in template generation are located
LOGOS_FOLDER_NAME = 'Logos'

# Task file names
TEMPLATE_NAME = 'Aspose_test'
TEMPLATE_DST_NAME = TEMPLATE_NAME + '.txt'
TEMPLATE_IMAGE_NAME = TEMPLATE_NAME + '.png'
TEMPLATE_USER_IMAGES_NAMES = ['photo.jpg', 'scan.jpg']
TEMPLATE_LOGOS_IMAGES_NAMES = ['logo1.jpg', 'logo2.png']


def serialize_files(file_paths):
    """
    Serialize files to JSON object
    :param file_paths: array of input file paths
    :return: JSON string with serialized files
    """
    d = OrderedDict([('Files', [])])
    for file_path in file_paths:
        try:
            with open(file_path, 'r+b') as f:
                data = f.read()

            encoded_data = str(base64.b64encode(data)) if six.PY2 else base64.b64encode(data).decode("ascii")

            d['Files'].append(OrderedDict([('Name', os.path.split(file_path)[1]), ('Size', os.path.getsize(file_path)),
                                           ('Data', encoded_data)]))
        except (IOError, OSError, EOFError) as err:
            text = "Can't read {} Reason: {} ".format(file_path, str(err))
            warn(text)
    return json.dumps(d, sort_keys=False, indent=4, separators=(', ', ': '))


def deserialize_file(file_info, dst_path):
    """
    Deserialize single response file to the specified location
    :param file_info: Response file to deserialize
    :param dst_path: Destination folder path
    :return: Path to deserialized file
    """
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    dst_file_path = os.path.join(dst_path, file_info.name)
    with open(dst_file_path, 'w+b') as f:
        f.write(base64.b64decode(file_info.data))
    print('File saved %s' % file_info.name)
    return dst_file_path


def deserialize_files(files, dst_path):
    """
    Deserialize list of files to the specified location
    :param files: List of response files
    :param dst_path: Destination folder path
    :return: Path to deserialized files
    """
    return [deserialize_file(file_info, dst_path) for file_info in files]


def upload_file(storage_api, src_file, dst_path):
    """
    Upload files to the storage
    :param src_file: Source file path
    :param dst_path: Destination path
    :return: None
    """

    # Upload file to storage
    print('Uploading %s into %s' % (src_file, dst_path))
    res = storage_api.upload_file(src_file, dst_path)
    print('Success!!! Uploaded file: ', res.uploaded)


def upload_demo_files(storage_api, data_dir_path):
    """
    Upload logo images used during template generation in a separate folder on cloud storage
    :data_dir_path: Path to directory containing logo images
    :return: None
    """

    response = storage_api.object_exists(path=str(LOGOS_FOLDER_NAME))
    if not response.exists:
        storage_api.create_folder(path=str(LOGOS_FOLDER_NAME))
    for logo in TEMPLATE_LOGOS_IMAGES_NAMES:
        dest_logo_path = '%s/%s' % (LOGOS_FOLDER_NAME, logo)
        response = storage_api.object_exists(path=str(dest_logo_path))
        if not response.exists:
            upload_file(storage_api, dest_logo_path, os.path.join(data_dir_path, logo))
        else:
            print('File %s already exists' % dest_logo_path)


def generate_template(omr_api, storage_api, template_dst_name, logos_folder):
    """
        Generate new template based on provided text description
        :param omr_api: OMR API Instance
        :param template_file_path: Path to template text description
        :param logos_folder: Name of the cloud folder with logo images
        :return: Generation response
    """

    image_file_name = os.path.basename(template_dst_name)

    # upload image on cloud
    upload_file(storage_api, image_file_name, template_dst_name)

    # provide function parameters
    omr_params = OmrFunctionParam(function_param=json.dumps(dict(ExtraStoragePath=logos_folder)), additional_param='')
    return omr_api.post_run_omr_task(image_file_name, "GenerateTemplate", omr_params)


def recognize_image(omr_api, storage_api, template_id, image_path):
    """
        Runs mark recognition on image
        :param omr_api: OMR API Instance
        :param template_id: Template ID
        :param image_path: Path to the image
        :return: Recognition response
    """

    image_file_name = os.path.basename(image_path)

    # upload image on cloud
    upload_file(storage_api, image_file_name, image_path)

    # provide template id as function parameter
    call_params = OmrFunctionParam(function_param=template_id, additional_param='')

    # call image recognition
    result = omr_api.post_run_omr_task(image_file_name, 'RecognizeImage', call_params)
    return result


def validate_template(omr_api, storage_api, template_image_path, template_data_dir):
    """
        Helper function that combines correct_template and finalize_template calls
        :param omr_api: OMR API Instance
        :param template_image_path: Path to template image
        :param template_data_dir: The folder where Template Data will be stored
        :return: Template ID
    """
    # Save correction results and provide them to the template finalization
    corrected_template_path = ''
    res_cr = correct_template(omr_api, storage_api, template_image_path, template_data_dir)
    if res_cr.error_code == 0:
        for file_info in res_cr.payload.result.response_files:
            response_file_local_path = deserialize_file(file_info, PATH_TO_OUTPUT)
            if file_info.name.lower().endswith('.omrcr'):
                corrected_template_path = response_file_local_path

    # Finalize template
    template_id = res_cr.payload.result.template_id
    res_fin = finalize_template(omr_api, storage_api, template_id, corrected_template_path)
    if res_fin.error_code == 0:
        deserialize_files(res_fin.payload.result.response_files, PATH_TO_OUTPUT)
    return template_id


def correct_template(omr_api, storage_api, template_image_path, template_data_dir):
    """
    Run template correction
    :param omr_api: OMR API Instance
    :param template_image_path: Path to template image
    :param template_data_dir: Path to template data file (.omr)
    :return: Correction response
    """

    image_file_name = os.path.basename(template_image_path)

    # upload template image
    upload_file(storage_api, image_file_name, template_image_path)

    # locate generated template file (.omr) and provide it's data as function parameter
    template_data_path = os.path.join(template_data_dir, os.path.splitext(image_file_name)[0] + '.omr')
    function_param = serialize_files([template_data_path])
    call_params = OmrFunctionParam(function_param=function_param, additional_param='')

    # call template correction
    result = omr_api.post_run_omr_task(image_file_name, "CorrectTemplate", call_params)
    return result


def finalize_template(omr_api, storage_api, template_id, corrected_template_path):
    """
    Run template finalization
    :param omr_api:  OMR API Instance
    :param template_id: Template id received after template correction
    :param corrected_template_path: Path to corrected template (.omrcr)
    :return: Finalization response
    """

    template_file_name = os.path.basename(corrected_template_path)

    # upload corrected template data on cloud
    upload_file(storage_api, template_file_name, corrected_template_path)

    # provide template id as function parameter
    call_params = OmrFunctionParam(function_param=template_id, additional_param='')

    # call template finalization
    result = omr_api.post_run_omr_task(template_file_name, 'FinalizeTemplate', call_params)
    return result


# Try to locate the config file
config = dict()
data_dir = ''
curr_path = os.path.abspath(os.path.dirname(os.path.realpath(os.getcwd())))
config_file_relative_path = os.path.join(DEMO_DATA_SUBMODULE_NAME, CONFIG)
config_file_path = None

# Parse config
while curr_path != os.path.abspath(os.path.join(curr_path, os.pardir)) and not os.path.isfile(
        os.path.join(curr_path, config_file_relative_path)):
    curr_path = os.path.abspath(os.path.join(curr_path, os.pardir))
if os.path.isfile(os.path.join(curr_path, config_file_relative_path)):
    config_file_path = os.path.join(curr_path, config_file_relative_path)
    with open(config_file_path) as f:
        config = json.loads(f.read())
else:
    raise IOError("Can't find config file %s" % CONFIG)

data_dir = os.path.join(os.path.dirname(config_file_path), config[u'data_folder'])
if not os.path.isdir(data_dir):
    raise IOError("Can't find folder with data %s" % data_dir)


def run_demo():

    configuration = Configuration(apiKey=config.get('app_key'), appSid=config.get('app_sid'))

    api = OmrApi(configuration)
    storage = storage_api.StorageApi(configuration)

    # Step 1: Upload demo files on cloud and Generate template
    print("\t\tUploading demo files...")
    upload_demo_files(storage, data_dir)
    print("\t\tGenerate template...")
    res_gen = generate_template(api, storage, os.path.join(data_dir, TEMPLATE_DST_NAME), LOGOS_FOLDER_NAME)
    if res_gen.error_code == 0:
        deserialize_files(res_gen.payload.result.response_files, PATH_TO_OUTPUT)

    # Step 2: Validate template
    print("\t\tValidate template...")
    template_id = validate_template(api, storage, os.path.join(PATH_TO_OUTPUT, TEMPLATE_IMAGE_NAME), PATH_TO_OUTPUT)

    # Step 3: Recognize photos and scans
    print("\t\tRecognize image...")
    for user_image in TEMPLATE_USER_IMAGES_NAMES:
        res_rec = recognize_image(api, storage, template_id, os.path.join(data_dir, user_image))
        if res_rec.error_code == 0:
            result_file = deserialize_files(res_rec.payload.result.response_files, PATH_TO_OUTPUT)[0]
            print('Result file %s' % result_file)





