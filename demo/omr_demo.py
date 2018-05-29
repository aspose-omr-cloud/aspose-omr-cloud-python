# coding: utf-8

"""
Copyright (c) 2018 Aspose Pty Ltd. All Rights Reserved.

Licensed under the MIT (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      https://github.com/aspose-omr-cloud/aspose-omr-cloud-python/blob/master/LICENSE

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import absolute_import, unicode_literals

import base64
import json
import os
import sys
import traceback
from warnings import warn

import six

sys.path.append('../')
from asposeomrcloud.apis.omr_api import OmrApi
from asposeomrcloud.models.omr_function_param import OMRFunctionParam

# asposestoragecloud can be installed within pip: pip install asposestoragecloud
from asposestoragecloud.apis.storage_api import StorageApi
from asposestoragecloud.api_client import ApiClient as StorageApiClient
from asposestoragecloud.rest import ApiException as StorageApiException
from asposestoragecloud.configuration import Configuration as StorageConfiguration

from collections import OrderedDict


# File with dictionary for configuration in JSON format
# The config file should look like:
# {
#     "app_key"  : "xxxxx",
#     "app_sid"   : "xxx-xxx-xxx-xxx-xxx",
#     "base_path" : "https://api.aspose.cloud/v1.1",
#     "data_folder" : "Data"
# }
# Provide your own app_key and app_sid, which you can receive by registering at Aspose Cloud Dashboard
# https://dashboard.aspose.cloud/

CONFIG = 'test_config.json'
DEMO_DATA_SUBMODULE_NAME = 'aspose-omr-cloud-demo-data'
# Output path where all results are placed
PATH_TO_OUTPUT = './Temp'
# Name of the folder where all images used in template generation are located
LOGOS_FOLDER_NAME = 'Logos'

# Task file names
TEMPLATE_NAME = 'Aspose_test'
TEMPLATE_DST_NAME = TEMPLATE_NAME + '.txt'
TEMPLATE_IMAGE_NAME = TEMPLATE_NAME + '.png'
TEMPLATE_USER_IMAGES_NAMES = ['photo.jpg', 'scan.jpg']
TEMPLATE_LOGOS_IMAGES_NAMES = ['logo1.jpg', 'logo2.png']


def create_storage_api(config):
    """
    Instantiate a StorageApi object
    :param config: JSON dictionary containing config data
    :return: Configured StorageApi() object
    """
    import urllib3.util

    t = urllib3.util.parse_url(config[u'base_path'])
    if t.scheme is None:
        t.scheme = 'https'

    # Initialize StorageApi
    c = StorageConfiguration()
    c.base_url = str(config[u'base_path'])
    c.host = '%s://%s%s' % (t.scheme, t.host, '' if t.port is None else ':%d' % t.port)
    return StorageApi(StorageApiClient(apiKey=str(config[u'app_key']), appSid=str(config[u'app_sid']), configuration=c))


def upload_file(src_file, dst_path):
    """
    Upload files to the storage
    :param src_file: Source file path
    :param dst_path: Destination path
    :return: None
    """
    print('Uploading %s into %s' % (src_file, dst_path))
    try:
        with open(src_file, 'rb') as f:
            file_data = f.read()
        response = storage_api.put_create(path=dst_path, file=file_data)
        print('File %s uploaded successfully with response %s' % (dst_path, response['Status']))
    except StorageApiException as err:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, file=sys.stdout)

        print("Can't upload file. Reason: {}".format(str(err)))
        raise err


def upload_demo_files(data_dir_path):
    """
    Upload logo images used during template generation in a separate folder on cloud storage
    :data_dir_path: Path to directory containing logo images
    :return: None
    """
    try:
        response = storage_api.get_is_exist(path=str(LOGOS_FOLDER_NAME))
        if not response.file_exist.is_exist:
            storage_api.put_create_folder(path=str(LOGOS_FOLDER_NAME))
        for logo in TEMPLATE_LOGOS_IMAGES_NAMES:
            dest_logo_path = '%s/%s' % (LOGOS_FOLDER_NAME, logo)
            response = storage_api.get_is_exist(path=str(dest_logo_path))
            if not response.file_exist.is_exist:
                upload_file(os.path.join(data_dir_path, logo), dest_logo_path)
            else:
                print('File %s already exists' % dest_logo_path)
    except StorageApiException as err:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, file=sys.stdout)

        print("Can't upload file. Reason: {}".format(str(err)))
        raise err


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


def generate_template(omr_api, template_file_path, logos_folder):
    """
    Generate new template based on provided text description
    :param omr_api: OMR API Instance
    :param template_file_path: Path to template text description
    :param logos_folder: Name of the cloud folder with logo images
    :return: Generation response
    """
    file_name = os.path.basename(template_file_path)
    # upload template text description
    upload_file(template_file_path, file_name)
    
    # provide function parameters
    call_params = OMRFunctionParam(function_param=json.dumps(dict(ExtraStoragePath=logos_folder)), additional_param='')
    result = omr_api.post_run_omr_task(name=file_name,
                                       action_name='GenerateTemplate',
                                       param=call_params)
    return result


def correct_template(omr_api, template_image_path, template_data_dir):
    """
    Run template correction
    :param omr_api: OMR API Instance
    :param template_image_path: Path to template image
    :param template_data_dir: Path to template data file (.omr)
    :return: Correction response
    """
    
    image_file_name = os.path.basename(template_image_path)
    # upload template image
    upload_file(template_image_path, image_file_name)

    # locate generated template file (.omr) and provide it's data as function parameter
    template_data_path = os.path.join(template_data_dir, os.path.splitext(image_file_name)[0] + '.omr')
    function_param = serialize_files([template_data_path])
    call_params = OMRFunctionParam(function_param=function_param, additional_param='')
    
    # call template correction
    result = omr_api.post_run_omr_task(name=image_file_name,
                                       action_name='CorrectTemplate',
                                       param=call_params)
    return result


def finalize_template(omr_api, template_id, corrected_template_path):
    """
    Run template finalization
    :param omr_api:  OMR API Instance
    :param template_id: Template id received after template correction
    :param corrected_template_path: Path to corrected template (.omrcr)
    :return: Finalization response
    """
    
    template_file_name = os.path.basename(corrected_template_path)
    # upload corrected template data on cloud
    upload_file(corrected_template_path, template_file_name)
    # provide template id as function parameter
    call_params = OMRFunctionParam(function_param=template_id, additional_param='')
    # call template finalization
    result = omr_api.post_run_omr_task(name=template_file_name,
                                       action_name='FinalizeTemplate',
                                       param=call_params)
    return result


def recognize_image(omr_api, template_id, image_path):
    """
    Runs mark recognition on image
    :param omr_api: OMR API Instance
    :param template_id: Template ID
    :param image_path: Path to the image
    :return: Recognition response
    """
    image_file_name = os.path.basename(image_path)
    # upload image on cloud
    upload_file(image_path, image_file_name)
    
    # provide template id as function parameter
    call_params = OMRFunctionParam(function_param=template_id, additional_param='')
    
    # call image recognition
    result = omr_api.post_run_omr_task(name=image_file_name,
                                       action_name='RecognizeImage',
                                       param=call_params)
    return result


def validate_template(omr_api, template_image_path, template_data_dir):
    """
    Helper function that combines correct_template and finalize_template calls
    :param omr_api: OMR API Instance
    :param template_image_path: Path to template image
    :param template_data_dir: The folder where Template Data will be stored
    :return: Template ID
    """

    # Save correction results and provide them to the template finalization 
    corrected_template_path = ''
    res_cr = correct_template(omr_api, template_image_path, template_data_dir)
    if res_cr.error_code == 0:
        for file_info in res_cr.payload.result.response_files:
            response_file_local_path = deserialize_file(file_info, PATH_TO_OUTPUT)
            if file_info.name.lower().endswith('.omrcr'):
                corrected_template_path = response_file_local_path

    # Finalize template
    template_id = res_cr.payload.result.template_id
    res_fin = finalize_template(omr_api, template_id, corrected_template_path)
    if res_fin.error_code == 0:
        deserialize_files(res_fin.payload.result.response_files, PATH_TO_OUTPUT)
    return template_id


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
# Create an OMR API instance
storage_api = create_storage_api(config)

# Step 1: Upload demo files on cloud and Generate template
print('\t\tUploading demo files...')
upload_demo_files(data_dir)

omr_api = OmrApi(config[u'app_key'], config[u'app_sid'],
                 config[u'base_path'])

print('\t\tGenerate template...')
res_gen = generate_template(omr_api, os.path.join(data_dir, TEMPLATE_DST_NAME), LOGOS_FOLDER_NAME)
if res_gen.error_code == 0:
    deserialize_files(res_gen.payload.result.response_files, PATH_TO_OUTPUT)

# Step 2: Validate template
print('\t\tValidate template...')
template_id = validate_template(omr_api, os.path.join(PATH_TO_OUTPUT, TEMPLATE_IMAGE_NAME), PATH_TO_OUTPUT)

# Step 3: Recognize photos and scans
print('\t\tRecognize image...')
for user_image in TEMPLATE_USER_IMAGES_NAMES:
    res_rec = recognize_image(omr_api, template_id, os.path.join(data_dir, user_image))
    if res_rec.error_code == 0:
        result_file = deserialize_files(res_rec.payload.result.response_files, PATH_TO_OUTPUT)[0]
        print('Result file %s' % result_file)
