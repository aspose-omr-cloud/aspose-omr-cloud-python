# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="file_info.py">
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
import re


class FileInfo(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'name': 'str',
        'size': 'int',
        'data': 'str'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'data': 'data'
    }

    def __init__(self, name=None, size=None, data=None):

        self._name = None
        self._size = None
        self._data = None

        if name is not None:
            self.name = name
        self.size = size
        if data is not None:
            self.data = data
    
    @property
    def name(self):
        """
        Gets the name of this FileInfo.
        Name of the file
        :return: The name of this FileInfo.
        :type: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileInfo.
        Name of the file
        :param name: The name of this FileInfo.
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """
        Gets the size of this FileInfo.
        Size of the image in bytes
        :return: The size of this FileInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FileInfo.
        Size of the image in bytes
        :param size: The size of this FileInfo.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size

    @property
    def data(self):
        """
        Gets the data of this FileInfo.
        File data packed in base64 string
        :return: The data of this FileInfo.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this FileInfo.
        File data packed in base64 string
        :param data: The data of this FileInfo.
        :type: str
        """
        if data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', data):
            raise ValueError("Invalid value for `data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")

        self._data = data