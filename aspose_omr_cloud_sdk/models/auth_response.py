class AuthResponse(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, token_type=None, access_token=None):  # noqa: E501
        """OMRResponse - a model defined in Swagger"""  # noqa: E501
        self.token_type = token_type
        self.access_token = access_token

    @property
    def token_type(self):
        """Gets the id of this OMRResponse.  # noqa: E501


        :return: The id of this OMRResponse.  # noqa: E501
        :rtype: str
        """
        return self.token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the id of this OMRResponse.


        :param id: The id of this OMRResponse.  # noqa: E501
        :type: str
        """

        self.token_type = token_type

    @property
    def access_token(self):
        """Gets the response_status_code of this OMRResponse.  # noqa: E501


        :return: The response_status_code of this OMRResponse.  # noqa: E501
        :rtype: ResponseStatusCode
        """
        return self.access_token

    @access_token.setter
    def response_status_code(self, access_token):
        """Sets the response_status_code of this OMRResponse.


        :param response_status_code: The response_status_code of this OMRResponse.  # noqa: E501
        :type: ResponseStatusCode
        """

        self.access_token = access_token


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
        if issubclass(OMRResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return print.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OMRResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other