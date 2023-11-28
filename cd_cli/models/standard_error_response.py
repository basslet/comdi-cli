import pprint


class StandardErrorResponse(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"code": "str", "messages": "list[BusinessMessage]"}

    attribute_map = {"code": "code", "messages": "messages"}

    def __init__(self, code=None, messages=None):
        """StandardErrorResponse"""

        self._code = None
        self._messages = None

        if code is not None:
            self.code = code
        if messages is not None:
            self.messages = messages

    @property
    def code(self):
        """Gets the code of this StandardErrorResponse.


        :return: The code of this StandardErrorResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StandardErrorResponse.


        :param code: The code of this StandardErrorResponse.
        :type: str
        """

        self._code = code

    @property
    def messages(self):
        """Gets the messages of this StandardErrorResponse.


        :return: The messages of this StandardErrorResponse.
        :rtype: list[BusinessMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this StandardErrorResponse.


        :param messages: The messages of this StandardErrorResponse.
        :type: list[BusinessMessage]
        """

        self._messages = messages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in iter(self.attribute_types.items()):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(StandardErrorResponse, dict):
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
        if not isinstance(other, StandardErrorResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandardErrorResponse):
            return True

        return self.to_dict() != other.to_dict()
