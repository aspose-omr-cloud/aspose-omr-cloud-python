# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="server_stat.py">
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


class ServerStat(BaseModel):
    """
    Attributes:
    model_types (dict): The key is attribute name
                        and the value is attribute type.
    attribute_map (dict): The key is attribute name
                        and the value is json key in definition.
    """
    model_types = {
        'storage_download_time': 'str',
        'omr_function_call_time': 'str'
    }

    attribute_map = {
        'storage_download_time': 'storageDownloadTime',
        'omr_function_call_time': 'omrFunctionCallTime'
    }

    def __init__(self, storage_download_time=None, omr_function_call_time=None):

        self._storage_download_time = None
        self._omr_function_call_time = None

        if storage_download_time is not None:
            self.storage_download_time = storage_download_time
        if omr_function_call_time is not None:
            self.omr_function_call_time = omr_function_call_time

    @property
    def storage_download_time(self):
        """
        Gets the storage_download_time of this ServerStat.
        Get or set StorageDownloadTime
        :return: The storage_download_time of this ServerStat.
        :rtype: str
        """
        return self._storage_download_time

    @storage_download_time.setter
    def storage_download_time(self, storage_download_time):
        """
        Sets the storage_download_time of this ServerStat.
        Get or set StorageDownloadTime
        :param storage_download_time: The storage_download_time of this ServerStat.
        :type: str
        """
        if storage_download_time is None:
            raise ValueError("Invalid value for `storage_download_time`, must not be `None`")

        self._storage_download_time = storage_download_time

    @property
    def omr_function_call_time(self):
        """
        Gets the omr_function_call_time of this ServerStat.
        Get or set OmrFunctionCallTime
        :return: The omr_function_call_time of this ServerStat.
        :rtype: str
        """
        return self._omr_function_call_time

    @omr_function_call_time.setter
    def omr_function_call_time(self, omr_function_call_time):
        """
        Sets the omr_function_call_time of this ServerStat.
        Get or set OmrFunctionCallTime
        :param omr_function_call_time: The omr_function_call_time of this ServerStat.
        :type: str
        """
        if omr_function_call_time is None:
            raise ValueError("Invalid value for `omr_function_call_time`, must not be `None`")

        self._omr_function_call_time = omr_function_call_time