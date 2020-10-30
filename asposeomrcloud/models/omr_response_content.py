# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_responce_content.py">
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

from asposeomrcloud.models import BaseModel


class OmrResponseContent(BaseModel):
    """
       Attributes:
         model_types (dict): The key is attribute name
                               and the value is attribute type.
         attribute_map (dict): The key is attribute name
                               and the value is json key in definition.
    """
    model_types = {
        'template_id': 'str',
        'execution_time': 'float',
        'response_files': 'list[FileInfo]',
        'info': 'OmrResponseInfo'
    }

    attribute_map = {
        'template_id': 'templateId',
        'execution_time': 'executionTime',
        'response_files': 'responseFiles',
        'info': 'info'
    }

    def __init__(self, template_id=None, execution_time=None, response_files=None, info=None):
        self._template_id = None
        self._execution_time = None
        self._response_files = None
        self._info = None

        if template_id is not None:
            self.template_id = template_id
        if execution_time is not None:
            self.execution_time = execution_time
        if response_files is not None:
            self.response_files = response_files
        if info is not None:
            self.info = info

    @property
    def template_id(self):
        """
        Gets the template_id of this OmrResponseContent.
        GUID string that is used to identify template on server This value is assigned after Template Correction and used later in Template Finalization and Image Recognition
        :return: The template_id of this OmrResponseContent.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this OmrResponseContent.
        GUID string that is used to identify template on server This value is assigned after Template Correction and used later in Template Finalization and Image Recognition
        :param template_id: The template_id of this OmrResponseContent.
        :type: str
        """
        self._template_id = template_id

    @property
    def execution_time(self):
        """
        Gets the execution_time of this OmrResponseContent.
        Indicates how long it took to perform task on server.
        :return: The execution_time of this OmrResponseContent.
        :rtype: float
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """
        Sets the execution_time of this OmrResponseContent.
        Indicates how long it took to perform task on server.
        :param execution_time: The execution_time of this OmrResponseContent.
        :type: float
        """
        if execution_time is None:
            raise ValueError("Invalid value for `execution_time`, must not be `None`")

        self._execution_time = execution_time

    @property
    def response_files(self):
        """
        Gets the response_files of this OmrResponseContent.
        This structure holds array of files returned in response Type and content of files differes depending on action
        :return: The response_files of this OmrResponseContent.
        :rtype: list[FileInfo]
        """
        return self._response_files

    @response_files.setter
    def response_files(self, response_files):
        """
        Sets the response_files of this OmrResponseContent.
        This structure holds array of files returned in response Type and content of files differes depending on action
        :param response_files: The response_files of this OmrResponseContent.
        :type: list[FileInfo]
        """

        self._response_files = response_files

    @property
    def info(self):
        """
        Gets the info of this OmrResponseContent.
        :return: The info of this OmrResponseContent.
        :rtype: OmrResponseInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """
        Sets the info of this OmrResponseContent.
        :param info: The info of this OmrResponseContent.
        :type: OmrResponseInfo
        """

        self._info = info