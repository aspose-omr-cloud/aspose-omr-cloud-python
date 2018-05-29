import os
import unittest
from . import common

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        from asposeomrcloud.apis.omr_api import OmrApi
        from asposeomrcloud.apis.omr_storage_api import OmrStorageApi


        self.omr_api = OmrApi(common.config['app_key'],
                     common.config['app_sid'],
                     common.config['base_path'])

        self.storage_api = OmrStorageApi(common.config['app_key'],
                                    common.config['app_sid'],
                                    common.config['base_path'])

    def test_generate_template(self):
        from asposeomrcloud.models.omr_function_param import OMRFunctionParam

        upload_response = self.storage_api.put_upload('Aspose_test.txt', os.path.join(common.data_dir, 'Aspose_test.txt'))
        self.assertTrue(upload_response.status == 'OK')

        omr_response = self.omr_api.post_run_omr_task(name='Aspose_test.txt', action_name='GenerateTemplate'
                , param=OMRFunctionParam(function_param='{ "ExtraStoragePath":"Logos"}', additional_param='')
        )
        self.assertTrue(omr_response.error_code == 0)

if __name__ == '__main__':
    unittest.main()