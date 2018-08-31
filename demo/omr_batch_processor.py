
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

import argparse
import time
from argparse import RawTextHelpFormatter

from asposeomrcloud.apis.omr_api import OmrApi

from helpers import *


def get_apis(config_path):
    # Try to locate the config file
    config = dict()
    curr_path = os.path.abspath(os.path.realpath(os.getcwd()))
    print(curr_path)

    if os.path.isfile(config_path):
        with open(config_path) as f:
            config = json.loads(f.read())

    # Create an OMR API instance
    omr_api = OmrApi(config[u'app_key'], config[u'app_sid'],
                     config[u'base_path'])
    storage_api = create_storage_api(config)

    return omr_api, storage_api


class OMRBatchProcessor:
    def __init__(self, args=None):
        # construct the argument parser and parse the arguments
        description_text = \
            'OMR batch processor' \
            'Run examples:\n' \
            './omr_batch_processor.py ./Data/UserImages --template_text ./Data/Aspose_test.txt --cloud_data_folder Logos\n' \
            './omr_batch_processor.py ./Data/UserImages --template_path ./result\n' \
            './Data/UserImages --template_id 2d05d522-9923-4fcf-868f-6906d56e2793 --result_folder rec_res\n'

        ap = argparse.ArgumentParser(description=description_text, formatter_class=RawTextHelpFormatter)

        ap.add_argument('input_path', help='Batch path')
        ap.add_argument('--template_text',
                        help='Path to template text description')
        ap.add_argument('--template_path',
                        help='Path with template data (template image and markup *.omr file)')
        ap.add_argument('--template_id', help='Use ready template id', default=None)
        ap.add_argument('--result_folder', help='Folder for dumping result', default='result')
        # File with dictionary for configuration in JSON format
        # The config file should look like:
        # {
        #     "app_key"  : "xxxxx",
        #     "app_sid"   : "xxx-xxx-xxx-xxx-xxx",
        #     "base_path" : "https://api.aspose.cloud/v1.1"
        # }
        # Provide your own app_key and app_sid, which you can receive by registering at Aspose Cloud Dashboard
        # https://dashboard.aspose.cloud/
        ap.add_argument('--config_path', help='Path to configuration in JSON format', default='test_config.json')
        ap.add_argument('--data_path', help='Path to data folder with files to upload')
        ap.add_argument('--cloud_data_folder', help='Name of the cloud folder where to upload data.\n' \
                                                    'If it is omitted the data_path name will be used', default='')

        self.args = ap.parse_args(args)
        print(self.args)

    def run(self):
        postfix_str = time.strftime("%Y_%m_%d_%H:%M:%S")
        omr_api, storage_api = get_apis(self.args.config_path)

        if self.args.template_id is None:
            if self.args.data_path:
                print('\t\tUploading demo files...')
                upload_files(self.args.cloud_data_folder, self.args.cloud_data_folder, storage_api)

            if self.args.template_path:
                template_path = self.args.template_path
            elif self.args.result_folder:
                template_path = self.args.result_folder
            else:
                template_path = os.path.join(self.args.result_folder, 'template_' + postfix_str)

            if self.args.template_text:
                print('\t\tGenerating template...')
                res_gen = generate_template(self.args.template_text, self.args.cloud_data_folder, omr_api, storage_api)

                if res_gen.error_code == 0:
                    deserialize_files(res_gen.payload.result.response_files, template_path)
                else:
                    raise RuntimeError("Failed to generate template:\n" + res_gen.error_text)
                template_name = os.path.splitext(os.path.split(self.args.template_text)[1])[0]
                template_image_name = template_name + '.png'
            else:
                images_names = list_files(self.args.template_path, IMAGES_EXT)
                if len(images_names) != 1:
                    print("Found images:\n {}".format(images_names))
                elif not images_names:
                    raise RuntimeError("Failed to load template: template data is not found in {}".format(
                        os.path.abspath(self.args.template_path)))

                template_image_name = images_names[0]

            image_path = os.path.join(template_path, template_image_name)
            print('\t\tValidating template {}...'.format(os.path.abspath(image_path)))
            template_id = validate_template(image_path, template_path, omr_api, storage_api)
            print("template_id is {}".format(template_id))
        else:
            template_id = self.args.template_id
            print("Using template with id {}".format(template_id))

        if template_id is None or not template_id:
            print("Won't recognize anything since template_id is absent")
            return 1

        print('\t\tRecognizing user images...')
        recognize_user_images(self.args.input_path, os.path.join(self.args.result_folder, 'recognition'),
                              template_id, omr_api, storage_api)


if __name__ == "__main__":
    t = OMRBatchProcessor()
    t.run()
