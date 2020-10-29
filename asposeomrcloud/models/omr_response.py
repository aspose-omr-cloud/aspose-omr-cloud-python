# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="omr_responce.py">
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


class OmrResponse(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'error_code': 'int',
        'error_text': 'str',
        'payload': 'Payload',
        'server_stat': 'ServerStat'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_text': 'errorText',
        'payload': 'payload',
        'server_stat': 'serverStat'
    }

    def __init__(self, error_code=None, error_text=None, payload=None, server_stat=None):

        self._error_code = None
        self._error_text = None
        self._payload = None
        self._server_stat = None

        self.error_code = error_code
        self.error_text = error_text
        self.payload = payload
        self.server_stat = server_stat

    @property
    def error_code(self):
        """
        Gets the error_code of this OmrResponse.
        Integer field that indicates whether any critical errors occured during task execution
        :return: The error_code of this OmrResponse.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this OmrResponse.
        Integer field that indicates whether any critical errors occured during task execution
        :param error_code: The error_code of this OmrResponse.
        :type: int
        """

        self._error_code = error_code

    @property
    def error_text(self):
        """
        Gets the error_text of this OmrResponse.
        String description of occured critical error. Empty if no critical errors occured
        :return: The error_text of this OmrResponse.
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        """
        Sets the error_text of this OmrResponse.
        String description of occured critical error. Empty if no critical errors occured
        :param error_text: The error_text of this OmrResponse.
        :type: str
        """

        self._error_text = error_text

    @property
    def payload(self):
        """
        Gets the payload of this OmrResponse.
        Payload
        :return: The payload of this OmrResponse.
        :rtype: Payload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this OmrResponse.
        Payload
        :param payload: The payload of this OmrResponse.
        :type: Payload
        """

        self._payload = payload

    @property
    def server_stat(self):
        """
        Gets the server_stat of this OmrResponse.
        Server statistics
        :return: The server_stat of this OmrResponse.
        :rtype: ServerStat
        """
        return self._server_stat

    @server_stat.setter
    def server_stat(self, server_stat):
        """
        Sets the server_stat of this OmrResponse.
        Server statistics
        :param server_stat: The server_stat of this OmrResponse.
        :type: ServerStat
        """

        self._server_stat = server_stat