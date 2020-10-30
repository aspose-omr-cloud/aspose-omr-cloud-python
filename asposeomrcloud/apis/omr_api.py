# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_api.py">
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

from asposeomrcloud.api_client import ApiClient


class OmrApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client

    ##########################################################
    #                  Run specific OMR task                 #
    ##########################################################

    def post_run_omr_task(self, url, action_name, omr_params, **kwargs):
        assert url is not None  

        all_params = ['additional_param', 'function_param']

        params = locals()
        query_params = []

        # verify the required parameter 'action_name' is set
        if ('action_name' not in params) or (params['action_name'] is None):
            raise ValueError("Missing the required parameter `action_name` when calling `post_run_omr_task`")

        # verify the required parameter 'param' is set
        if ('omr_params' not in params) or (params['omr_params'] is None):
            raise ValueError("Missing the required parameter `param` when calling `post_run_omr_task`")

        collection_formats = {}

        path_params = {}  # uri params #
        local_var_files = {}

        header_params = {}
        form_params = {}

        body_params = None
        body_params = omr_params

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        result = self.api_client.call_api(f'/omr/{url}/runOmrTask?actionName={action_name}', 'POST',
                                          path_params, query_params, header_params,
                                          body=body_params, post_params=form_params, files=local_var_files,
                                          response_type='OmrResponse', async_req=params.get('async_req'),
                                          _return_http_data_only=params.get('_return_http_data_only', True),
                                          collection_formats=collection_formats,
                                          _preload_content=params.get('_preload_content', True),
                                          _request_timeout=params.get('_request_timeout'))

        return result
