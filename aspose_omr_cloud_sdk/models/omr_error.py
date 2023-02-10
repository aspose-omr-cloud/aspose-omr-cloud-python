"""
 * Copyright (c) 2023 Aspose Pty Ltd. All Rights Reserved.
 *
 * Licensed under the MIT (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://github.com/aspose-omr-cloud/aspose-omr-cloud-dotnet/blob/master/LICENSE
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

import pprint
import re  # noqa: F401

import six


class OMRError(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'messages': 'list[str]',
        'warnings': 'list[str]'
    }

    attribute_map = {
        'messages': 'messages',
        'warnings': 'warnings'
    }

    def __init__(self, messages=None, warnings=None):  # noqa: E501
        """OMRError - a model defined in Swagger"""  # noqa: E501
        self._messages = None
        self._warnings = None
        self.discriminator = None
        if messages is not None:
            self.messages = messages
        if warnings is not None:
            self.warnings = warnings

    @property
    def messages(self):
        """Gets the messages of this OMRError.  # noqa: E501


        :return: The messages of this OMRError.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this OMRError.


        :param messages: The messages of this OMRError.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def warnings(self):
        """Gets the warnings of this OMRError.  # noqa: E501


        :return: The warnings of this OMRError.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this OMRError.


        :param warnings: The warnings of this OMRError.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OMRError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OMRError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
