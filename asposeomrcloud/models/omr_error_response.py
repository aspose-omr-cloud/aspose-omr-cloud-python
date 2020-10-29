# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_error_responce.py">
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


class OmrErrorResponse(BaseModel):
    """
    Attributes:
        model_types (dict): The key is attribute name
                            and the value is attribute type.
        attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'message': 'str',
    }

    attribute_map = {
        'message': 'message',
    }

    def __init__(self, message=None):
        self._message = None

        if message is not None:
            self.message = message

    @property
    def message(self):
        """
        Gets the message of this OmrErrorResponse.
        Integer field that indicates whether any critical errors occured during task execution
        :return: The message of this OmrErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def error_code(self, message):
        """
        Sets the message of this OmrErrorResponse.
        Integer field that indicates whether any critical errors occured during task execution
        :param message: The message of this OmrErrorResponse.
        :type: str
        """

        self._message = message