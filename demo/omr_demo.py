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

from __future__ import absolute_import, unicode_literals

import time
import base64
import json
import ntpath
import os
from msilib.schema import File
from pathlib import Path
from threading import Thread
from warnings import warn

import six

from aspose_omr_cloud_sdk import GenerateTemplateApi, RecognizeTemplateApi, PageSettings, OmrGenerateTask, OMRResponse, \
    ResponseStatusCode, OmrRecognizeTask, ApiClient, FileExtension
from aspose_omr_cloud_sdk.configuration import Configuration
from collections import OrderedDict


# The configuration file in JSON format:
# The config file should look like:
# {
#     "client_secret"  : "xxx",
#	  "client_id"   : "xxx-xxx-xxx-xxx-xxx",
#	  "base_path" : "Aspose.OMR Cloud URL",
#	  "auth_url":"Aspose.OMR Cloud Authorization URL",
#     "data_folder"   : "Data",
#     "result_folder" : "Temp",
# }
CONFIG_FILE_NAME = "test_config.json"

# Declare an object to hold the parsed configuration data
Config = dict()

# Name of the sub-module with demo data and the configuration file
DEMO_DATA_SUBMODULE_NAME = "aspose-omr-cloud-demo-data"

# File names for template sources, printable form, recognition pattern and results
BASE_FILE_NAME = "Aspose_test"
TEMPLATE_GENERATION_FILE_NAME = BASE_FILE_NAME + ".txt"
TEMPLATE_IMAGE_NAME = BASE_FILE_NAME + ".jpg"
OMR_FILE_NAME = BASE_FILE_NAME + ".omr"
RESULT_FILE_NAME = BASE_FILE_NAME + ".csv"
TEMPLATE_LOGOS_IMAGES_NAMES = ['logo1.jpg', 'logo2.png']


def generate_template(template_file_path, template_logos_images_names):
    # Read the template source code
    with open(template_file_path, 'r+b') as f:
        image = base64.b64encode(f.read()).decode('utf-8')

    # Configure the page layout
    settings = PageSettings(font_size=12, font_family="Segoe UI", font_style="Regular", paper_size="A4", bubble_color="Black", page_margin_left=210, orientation="Vertical", bubble_size="Normal", output_format="Png")

    # Load images used in the template
    # images = dict()
    if template_logos_images_names is not None:
        case_list = {}
        for logo_name in template_logos_images_names:
            with open(os.path.join(DataFolder, logo_name), 'r+b') as f:
                logo = base64.b64encode(f.read()).decode('utf-8')
                name = ntpath.basename(logo_name)
                item = {name, logo}
            case_list[name] = logo
    # images.update(case_list)
    # Build request
    task = OmrGenerateTask(image, settings, case_list)
    kwargs = {"body":task};
    # Put the request into queue
    return GenerateTemplateApi.post_generate_template(**kwargs)


def get_generation_result_by_id(template_id):
    generationResult = OMRResponse()
    while True:
        kwargs = {"id": template_id};
        generationResult = GenerateTemplateApi.get_generate_template(**kwargs)
        if generationResult.response_status_code == "Ok":
            break
        elif generationResult.response_status_code == "Error":
            raise Exception("Something went wrong ...", generationResult.Error)
        else:
            print("Please wait while we are processing your request...")
            time.sleep(5)

    return generationResult


def save_generation_result(generation_result, path):
    if generation_result.error is None:
        for result in generation_result.results:
            name = BASE_FILE_NAME + "." + result.type.lower()
            pathFile = os.path.join(path, name)
            with open(os.path.join(pathFile), 'wb') as f:
                f.write(base64.b64decode(result.data))

    else:
        print("Error :", generation_result.Error.ToString())


def recognize_image(image_path, omr_file_path):
    # Read the recognition pattern file
    with open(omr_file_path, 'r+b') as f:
        omrFile = base64.b64encode(f.read()).decode('utf-8')

    # Set the recognition accuracy
    # Lower value allow even the lightest marks to be recognized
    # Higher value require a more solid fill and may cause pencil marks to be ignored
    recognitionThreshold = 30

    # Read the filled form
    with open(image_path, 'r+b') as f:
        image = base64.b64encode(f.read()).decode('utf-8')
    images = [image]

    # Build request
    task = OmrRecognizeTask(images, omrFile, FileExtension.CSV, recognitionThreshold)

    # Put the request into queue
    kwargs = {"body": task}
    return RecognizeTemplateApi.post_recognize_template(**kwargs)


def get_recognition_result_by_id(template_id):
    recognitionResult = OMRResponse()
    while True:
        kwargs = {"id": template_id}
        recognitionResult = RecognizeTemplateApi.get_recognize_template(**kwargs)
        if recognitionResult.response_status_code == "Ok":
            break
        elif recognitionResult.response_status_code == "Error":
            raise Exception("Something went wrong ...", recognitionResult.error)
        else:
            print("Please wait while we are processing your request...")
            time.sleep(5)

    return recognitionResult


def save_recognition_result(recognition_result, path):
    if recognition_result.error is None:
        with open(os.path.join(path), 'wb') as f:
            f.write(base64.b64decode(recognition_result.results[0].data))
    else:
        print("Error :", recognition_result.Error.ToString())


curr_path = os.path.abspath(os.path.dirname(os.path.realpath(os.getcwd())))
config_file_relative_path = os.path.join(DEMO_DATA_SUBMODULE_NAME, CONFIG_FILE_NAME)

while curr_path != os.path.abspath(os.path.join(curr_path, os.pardir)) and not os.path.isfile(
        os.path.join(curr_path, config_file_relative_path)):
    curr_path = os.path.abspath(os.path.join(curr_path, os.pardir))
    if os.path.isfile(os.path.join(curr_path, config_file_relative_path)):
        config_file_path = os.path.join(curr_path, config_file_relative_path)
        with open(config_file_path) as f:
            Config = json.loads(f.read())
    else:
        raise IOError("Can't find config file %s" % CONFIG_FILE_NAME)

# Parse the configuration file
    DataFolder = os.path.join(os.path.dirname(config_file_path), Config[u'data_folder'])
    ResultFolder = os.path.join(os.path.dirname(config_file_path), Config[u'result_folder'])

    configuration = Configuration(hostUrl = Config["base_path"],
                                  authUrl = Config["auth_url"],
                                  clientId = Config["client_id"],
                                  clientSecret = Config["client_secret"])
    apiClient = ApiClient(configuration= configuration)
    # Create an instance of GenerateTemplateApi class
    GenerateTemplateApi = GenerateTemplateApi(apiClient)

    # Create an instance of RecognizeTemplateApi class
    RecognizeTemplateApi = RecognizeTemplateApi(apiClient)


def run_demo():
    # STEP 1: Queue the template source file for generation
    print("\t\tGenerate template...")
    templateId = generate_template(os.path.join(DataFolder, TEMPLATE_GENERATION_FILE_NAME),
                                   TEMPLATE_LOGOS_IMAGES_NAMES)

    # STEP 2: Fetch generated printable form and recognition pattern
    print("\t\tGet generation result by ID...")
    generationResult = get_generation_result_by_id(templateId)

    # STEP 3: Save the printable form and recognition pattern into result_folder
    print("\t\tSave generation result...")
    save_generation_result(generationResult, ResultFolder)

    # STEP 4: Queue the scan / photo of the filled form for recognition
    print("\t\tRecognize image...")
    recognizeTemplateId = recognize_image(os.path.join(DataFolder, TEMPLATE_IMAGE_NAME),
                                          os.path.join(ResultFolder, OMR_FILE_NAME))

    # STEP 5: Fetch recognition results
    print("\t\tGet recognition result by ID...")
    recognitionResponse = get_recognition_result_by_id(recognizeTemplateId)

    # STEP 6: Save the recognition results into result_folder
    print("\t\tSave recognition result...")
    save_recognition_result(recognitionResponse, os.path.join(ResultFolder, RESULT_FILE_NAME))
