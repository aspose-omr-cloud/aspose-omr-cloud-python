# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_response_info.py">
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


class OmrResponseInfo(BaseModel):
    """
    Attributes:
        model_types (dict): The key is attribute name
                            and the value is attribute type.
        attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'response_version': 'str',
        'processed_tasks_count': 'int',
        'successful_tasks_count': 'int',
        'details': 'OmrResponseDetails'
    }

    attribute_map = {
        'response_version': 'responseVersion',
        'processed_tasks_count': 'processedTasksCount',
        'successful_tasks_count': 'successfulTasksCount',
        'details': 'details'
    }

    def __init__(self, response_version=None, processed_tasks_count=None, successful_tasks_count=None, details=None):
        """
        OmrResponseInfo - a model defined in Swagger
        """

        self._response_version = None
        self._processed_tasks_count = None
        self._successful_tasks_count = None
        self._details = None
        self.discriminator = None

        if response_version is not None:
            self.response_version = response_version
        self.processed_tasks_count = processed_tasks_count
        self.successful_tasks_count = successful_tasks_count
        if details is not None:
            self.details = details

    @property
    def response_version(self):
        """
        Gets the response_version of this OmrResponseInfo.
        String value representing version of the response.
        :return: The response_version of this OmrResponseInfo.
        :rtype: str
        """
        return self._response_version

    @response_version.setter
    def response_version(self, response_version):
        """
        Sets the response_version of this OmrResponseInfo.
        String value representing version of the response.
        :param response_version: The response_version of this OmrResponseInfo.
        :type: str
        """

        self._response_version = response_version

    @property
    def processed_tasks_count(self):
        """
        Gets the processed_tasks_count of this OmrResponseInfo.
        Total amount of processed tasks
        :return: The processed_tasks_count of this OmrResponseInfo.
        :rtype: int
        """
        return self._processed_tasks_count

    @processed_tasks_count.setter
    def processed_tasks_count(self, processed_tasks_count):
        """
        Sets the processed_tasks_count of this OmrResponseInfo.
        Total amount of processed tasks
        :param processed_tasks_count: The processed_tasks_count of this OmrResponseInfo.
        :type: int
        """
        if processed_tasks_count is None:
            raise ValueError("Invalid value for `processed_tasks_count`, must not be `None`")

        self._processed_tasks_count = processed_tasks_count

    @property
    def successful_tasks_count(self):
        """
        Gets the successful_tasks_count of this OmrResponseInfo.
        Total amount of successful tasks, i.e. tasks that completed without errors
        :return: The successful_tasks_count of this OmrResponseInfo.
        :rtype: int
        """
        return self._successful_tasks_count

    @successful_tasks_count.setter
    def successful_tasks_count(self, successful_tasks_count):
        """
        Sets the successful_tasks_count of this OmrResponseInfo.
        Total amount of successful tasks, i.e. tasks that completed without errors
        :param successful_tasks_count: The successful_tasks_count of this OmrResponseInfo.
        :type: int
        """
        if successful_tasks_count is None:
            raise ValueError("Invalid value for `successful_tasks_count`, must not be `None`")

        self._successful_tasks_count = successful_tasks_count

    @property
    def details(self):
        """
        Gets the details of this OmrResponseInfo.
        Additional information regarding performed task.
        :return: The details of this OmrResponseInfo.
        :rtype: OMRResponseDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this OmrResponseInfo.
        Additional information regarding performed task.
        :param details: The details of this OmrResponseInfo.
        :type: OMRResponseDetails
        """

        self._details = details