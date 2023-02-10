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


class PageSettings(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'font_family': 'str',
        'font_style': 'FontStyle',
        'font_size': 'int',
        'paper_size': 'PaperSize',
        'bubble_color': 'Color',
        'page_margin_left': 'int',
        'orientation': 'Orientation',
        'bubble_size': 'BubbleSize',
        'output_format': 'FileExtension'
    }

    attribute_map = {
        'font_family': 'fontFamily',
        'font_style': 'fontStyle',
        'font_size': 'fontSize',
        'paper_size': 'paperSize',
        'bubble_color': 'bubbleColor',
        'page_margin_left': 'pageMarginLeft',
        'orientation': 'orientation',
        'bubble_size': 'bubbleSize',
        'output_format': 'outputFormat'
    }

    def __init__(self, font_family=None, font_style=None, font_size=None, paper_size=None, bubble_color=None, page_margin_left=None, orientation=None, bubble_size=None, output_format=None):  # noqa: E501
        """PageSettings - a model defined in Swagger"""  # noqa: E501
        self._font_family = None
        self._font_style = None
        self._font_size = None
        self._paper_size = None
        self._bubble_color = None
        self._page_margin_left = None
        self._orientation = None
        self._bubble_size = None
        self._output_format = None
        self.discriminator = None
        if font_family is not None:
            self.font_family = font_family
        if font_style is not None:
            self.font_style = font_style
        if font_size is not None:
            self.font_size = font_size
        if paper_size is not None:
            self.paper_size = paper_size
        if bubble_color is not None:
            self.bubble_color = bubble_color
        if page_margin_left is not None:
            self.page_margin_left = page_margin_left
        if orientation is not None:
            self.orientation = orientation
        if bubble_size is not None:
            self.bubble_size = bubble_size
        if output_format is not None:
            self.output_format = output_format

    @property
    def font_family(self):
        """Gets the font_family of this PageSettings.  # noqa: E501


        :return: The font_family of this PageSettings.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this PageSettings.


        :param font_family: The font_family of this PageSettings.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

    @property
    def font_style(self):
        """Gets the font_style of this PageSettings.  # noqa: E501


        :return: The font_style of this PageSettings.  # noqa: E501
        :rtype: FontStyle
        """
        return self._font_style

    @font_style.setter
    def font_style(self, font_style):
        """Sets the font_style of this PageSettings.


        :param font_style: The font_style of this PageSettings.  # noqa: E501
        :type: FontStyle
        """

        self._font_style = font_style

    @property
    def font_size(self):
        """Gets the font_size of this PageSettings.  # noqa: E501


        :return: The font_size of this PageSettings.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this PageSettings.


        :param font_size: The font_size of this PageSettings.  # noqa: E501
        :type: int
        """

        self._font_size = font_size

    @property
    def paper_size(self):
        """Gets the paper_size of this PageSettings.  # noqa: E501


        :return: The paper_size of this PageSettings.  # noqa: E501
        :rtype: PaperSize
        """
        return self._paper_size

    @paper_size.setter
    def paper_size(self, paper_size):
        """Sets the paper_size of this PageSettings.


        :param paper_size: The paper_size of this PageSettings.  # noqa: E501
        :type: PaperSize
        """

        self._paper_size = paper_size

    @property
    def bubble_color(self):
        """Gets the bubble_color of this PageSettings.  # noqa: E501


        :return: The bubble_color of this PageSettings.  # noqa: E501
        :rtype: Color
        """
        return self._bubble_color

    @bubble_color.setter
    def bubble_color(self, bubble_color):
        """Sets the bubble_color of this PageSettings.


        :param bubble_color: The bubble_color of this PageSettings.  # noqa: E501
        :type: Color
        """

        self._bubble_color = bubble_color

    @property
    def page_margin_left(self):
        """Gets the page_margin_left of this PageSettings.  # noqa: E501


        :return: The page_margin_left of this PageSettings.  # noqa: E501
        :rtype: int
        """
        return self._page_margin_left

    @page_margin_left.setter
    def page_margin_left(self, page_margin_left):
        """Sets the page_margin_left of this PageSettings.


        :param page_margin_left: The page_margin_left of this PageSettings.  # noqa: E501
        :type: int
        """

        self._page_margin_left = page_margin_left

    @property
    def orientation(self):
        """Gets the orientation of this PageSettings.  # noqa: E501


        :return: The orientation of this PageSettings.  # noqa: E501
        :rtype: Orientation
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PageSettings.


        :param orientation: The orientation of this PageSettings.  # noqa: E501
        :type: Orientation
        """

        self._orientation = orientation

    @property
    def bubble_size(self):
        """Gets the bubble_size of this PageSettings.  # noqa: E501


        :return: The bubble_size of this PageSettings.  # noqa: E501
        :rtype: BubbleSize
        """
        return self._bubble_size

    @bubble_size.setter
    def bubble_size(self, bubble_size):
        """Sets the bubble_size of this PageSettings.


        :param bubble_size: The bubble_size of this PageSettings.  # noqa: E501
        :type: BubbleSize
        """

        self._bubble_size = bubble_size

    @property
    def output_format(self):
        """Gets the output_format of this PageSettings.  # noqa: E501


        :return: The output_format of this PageSettings.  # noqa: E501
        :rtype: FileExtension
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this PageSettings.


        :param output_format: The output_format of this PageSettings.  # noqa: E501
        :type: FileExtension
        """

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
        if issubclass(PageSettings, dict):
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
        if not isinstance(other, PageSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
