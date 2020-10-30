# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="recognition_statistics.py">
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


class RecognitionStatistics(BaseModel):
    """
    Attributes:
        model_types (dict):   The key is attribute name
                                and the value is attribute type.
        attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
    """
    model_types = {
        'name': 'str',
        'task_messages': 'list[str]',
        'task_result': 'str',
        'run_seconds': 'float'
    }

    attribute_map = {
        'name': 'name',
        'task_messages': 'taskMessages',
        'task_result': 'taskResult',
        'run_seconds': 'runSeconds'
    }

    def __init__(self, name=None, task_messages=None, task_result=None, run_seconds=None):

        self._name = None
        self._task_messages = None
        self._task_result = None
        self._run_seconds = None

        if name is not None:
            self.name = name
        if task_messages is not None:
            self.task_messages = task_messages
        if task_result is not None:
            self.task_result = task_result
        self.run_seconds = run_seconds

    @property
    def name(self):
        """
        Gets the name of this RecognitionStatistics.
        Gets or sets Name
        :return: The name of this RecognitionStatistics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecognitionStatistics.
        Gets or sets Name
        :param name: The name of this RecognitionStatistics.
        :type: str
        """

        self._name = name

    @property
    def task_messages(self):
        """
        Gets the task_messages of this RecognitionStatistics.
        Warnings and other messages regarding task, etc.
        :return: The task_messages of this RecognitionStatistics.
        :rtype: list[str]
        """
        return self._task_messages

    @task_messages.setter
    def task_messages(self, task_messages):
        """
        Sets the task_messages of this RecognitionStatistics.
        Warnings and other messages regarding task, etc.
        :param task_messages: The task_messages of this RecognitionStatistics.
        :type: list[str]
        """

        self._task_messages = task_messages

    @property
    def task_result(self):
        """
        Gets the task_result of this RecognitionStatistics.
        Indicates if each particular task passed or failed,
        :return: The task_result of this RecognitionStatistics.
        :rtype: str
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        """
        Sets the task_result of this RecognitionStatistics.
        Indicates if each particular task passed or failed,
        :param task_result: The task_result of this RecognitionStatistics.
        :type: str
        """

        self._task_result = task_result

    @property
    def run_seconds(self):
        """
        Gets the run_seconds of this RecognitionStatistics.
        Gets or sets RunSeconds
        :return: The run_seconds of this RecognitionStatistics.
        :rtype: float
        """
        return self._run_seconds

    @run_seconds.setter
    def run_seconds(self, run_seconds):
        """
        Sets the run_seconds of this RecognitionStatistics.
        Gets or sets RunSeconds
        :param run_seconds: The run_seconds of this RecognitionStatistics.
        :type: float
        """
        if run_seconds is None:
            raise ValueError("Invalid value for `run_seconds`, must not be `None`")

        self._run_seconds = run_seconds