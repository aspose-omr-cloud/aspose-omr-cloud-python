# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_response_details.py">
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


class OmrResponseDetails(BaseModel):
    """
        Attributes:
            model_types (dict): The key is attribute name
                                and the value is attribute type.
            attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
    """
    model_types = {
        'task_messages': 'list[str]',
        'task_result': 'str',
        'recognition_statistics': 'list[RecognitionStatistics]'
    }

    attribute_map = {
        'task_messages': 'taskMessages',
        'task_result': 'taskResult',
        'recognition_statistics': 'recognitionStatistics'
    }

    def __init__(self, task_messages=None, task_result=None, recognition_statistics=None):
        """
        OMRResponseDetails - a model defined in Swagger
        """

        self._task_messages = None
        self._task_result = None
        self._recognition_statistics = None
        self.discriminator = None

        if task_messages is not None:
            self.task_messages = task_messages
        if task_result is not None:
            self.task_result = task_result
        if recognition_statistics is not None:
            self.recognition_statistics = recognition_statistics

    @property
    def task_messages(self):
        """
        Gets the task_messages of this OmrResponseDetails.
        Warnings and other messages regarding task, etc.
        :return: The task_messages of this OmrResponseDetails.
        :rtype: list[str]
        """
        return self._task_messages

    @task_messages.setter
    def task_messages(self, task_messages):
        """
        Sets the task_messages of this OmrResponseDetails.
        Warnings and other messages regarding task, etc.
        :param task_messages: The task_messages of this OmrResponseDetails.
        :type: list[str]
        """

        self._task_messages = task_messages

    @property
    def task_result(self):
        """
        Gets the task_result of this OmrResponseDetails.
        Indicates if each particular task passed or failed,
        :return: The task_result of this OmrResponseDetails.
        :rtype: str
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        """
        Sets the task_result of this OmrResponseDetails.
        Indicates if each particular task passed or failed,
        :param task_result: The task_result of this OmrResponseDetails.
        :type: str
        """

        self._task_result = task_result

    @property
    def recognition_statistics(self):
        """
        Gets the recognition_statistics of this OmrResponseDetails.
        RecognitionStatistics
        :return: The recognition_statistics of this OmrResponseDetails.
        :rtype: list[RecognitionStatistics]
        """
        return self._recognition_statistics

    @recognition_statistics.setter
    def recognition_statistics(self, recognition_statistics):
        """
        Sets the recognition_statistics of this OmrResponseDetails.
        RecognitionStatistics
        :param recognition_statistics: The recognition_statistics of this OmrResponseDetails.
        :type: list[RecognitionStatistics]
        """

        self._recognition_statistics = recognition_statistics