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


class OmrRecognizeTask(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'images': 'list[str]',
        'omr_file': 'str',
        'output_format': 'FileExtension',
        'recognition_threshold': 'int'
    }

    attribute_map = {
        'images': 'images',
        'omr_file': 'omrFile',
        'output_format': 'outputFormat',
        'recognition_threshold': 'recognitionThreshold'
    }

    def __init__(self, images=None, omr_file=None, output_format = None, recognition_threshold=None):  # noqa: E501
        """OmrRecognizeTask - a model defined in Swagger"""  # noqa: E501
        self._images = None
        self._omr_file = None
        self._output_format = None
        self._recognition_threshold = None
        self.discriminator = None
        self.images = images
        self.omr_file = omr_file
        self.output_format = output_format
        if recognition_threshold is not None:
            self.recognition_threshold = recognition_threshold

    @property
    def images(self):
        """Gets the images of this OmrRecognizeTask.  # noqa: E501


        :return: The images of this OmrRecognizeTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this OmrRecognizeTask.


        :param images: The images of this OmrRecognizeTask.  # noqa: E501
        :type: list[str]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def omr_file(self):
        """Gets the omr_file of this OmrRecognizeTask.  # noqa: E501


        :return: The omr_file of this OmrRecognizeTask.  # noqa: E501
        :rtype: str
        """
        return self._omr_file

    @omr_file.setter
    def omr_file(self, omr_file):
        """Sets the omr_file of this OmrRecognizeTask.


        :param omr_file: The omr_file of this OmrRecognizeTask.  # noqa: E501
        :type: str
        """
        if omr_file is None:
            raise ValueError("Invalid value for `omr_file`, must not be `None`")  # noqa: E501

        self._omr_file = omr_file

    @property
    def output_format(self):
        """Gets the output_format of this OmrRecognizeTask.  # noqa: E501


        :return: The output_format of this OmrRecognizeTask.  # noqa: E501
        :rtype: FileExtension
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this OmrRecognizeTask.


        :param output_format: The output_format of this OmrRecognizeTask.  # noqa: E501
        :type: FileExtension
        """
        if output_format is None:
            raise ValueError("Invalid value for `output_format`, must not be `None`")  # noqa: E501

        self._output_format = output_format

    @property
    def recognition_threshold(self):
        """Gets the recognition_threshold of this OmrRecognizeTask.  # noqa: E501


        :return: The recognition_threshold of this OmrRecognizeTask.  # noqa: E501
        :rtype: int
        """
        return self._recognition_threshold

    @recognition_threshold.setter
    def recognition_threshold(self, recognition_threshold):
        """Sets the recognition_threshold of this OmrRecognizeTask.


        :param recognition_threshold: The recognition_threshold of this OmrRecognizeTask.  # noqa: E501
        :type: int
        """

        self._recognition_threshold = recognition_threshold

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
        if issubclass(OmrRecognizeTask, dict):
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
        if not isinstance(other, OmrRecognizeTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
