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


class OmrGenerateTask(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'markup_file': 'str',
        'settings': 'PageSettings',
        'images': 'dict(str, str)',
        'output_format': 'FileExtension'
    }

    attribute_map = {
        'markup_file': 'markupFile',
        'settings': 'settings',
        'images': 'images',
        'output_format': 'outputFormat'
    }

    def __init__(self, markup_file=None, settings=None, images=None, output_format='Png'):  # noqa: E501
        """OmrGenerateTask - a model defined in Swagger"""  # noqa: E501
        self._markup_file = None
        self._settings = None
        self._images = None
        self._output_format = None
        self.discriminator = None
        self.markup_file = markup_file
        self.settings = settings
        self.images = images
        self.output_format = output_format

    @property
    def markup_file(self):
        """Gets the markup_file of this OmrGenerateTask.  # noqa: E501


        :return: The markup_file of this OmrGenerateTask.  # noqa: E501
        :rtype: str
        """
        return self._markup_file

    @markup_file.setter
    def markup_file(self, markup_file):
        """Sets the markup_file of this OmrGenerateTask.


        :param markup_file: The markup_file of this OmrGenerateTask.  # noqa: E501
        :type: str
        """
        if markup_file is None:
            raise ValueError("Invalid value for `markup_file`, must not be `None`")  # noqa: E501

        self._markup_file = markup_file

    @property
    def settings(self):
        """Gets the settings of this OmrGenerateTask.  # noqa: E501


        :return: The settings of this OmrGenerateTask.  # noqa: E501
        :rtype: PageSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OmrGenerateTask.


        :param settings: The settings of this OmrGenerateTask.  # noqa: E501
        :type: PageSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def images(self):
        """Gets the images of this OmrGenerateTask.  # noqa: E501


        :return: The images of this OmrGenerateTask.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this OmrGenerateTask.


        :param images: The images of this OmrGenerateTask.  # noqa: E501
        :type: dict(str, str)
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def output_format(self):
        """Gets the output_format of this OmrGenerateTask.  # noqa: E501


        :return: The output_format of this OmrGenerateTask.  # noqa: E501
        :rtype: FileExtension
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this OmrGenerateTask.


        :param output_format: The output_format of this OmrGenerateTask.  # noqa: E501
        :type: FileExtension
        """
        if output_format is None:
            raise ValueError("Invalid value for `output_format`, must not be `None`")  # noqa: E501

        self._output_format = output_format

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
        if issubclass(OmrGenerateTask, dict):
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
        if not isinstance(other, OmrGenerateTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
