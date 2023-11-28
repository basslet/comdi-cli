import pprint


class EnumText(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"key": "str", "text": "str"}

    attribute_map = {"key": "key", "text": "text"}

    def __init__(self, key=None, text=None):
        """EnumText"""

        self._key = None
        self._text = None

        if key is not None:
            self.key = key
        if text is not None:
            self.text = text

    @property
    def key(self):
        """Gets the key of this EnumText.

        Unique key value for an enumeration type.

        :return: The key of this EnumText.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this EnumText.

        Unique key value for an enumeration type.

        :param key: The key of this EnumText.
        :type: str
        """
        if key is not None and len(key) > 40:
            raise ValueError(
                "Invalid value for `key`, length must be less than or equal to `40`"
            )
        if key is not None and len(key) < 1:
            raise ValueError(
                "Invalid value for `key`, length must be greater than or equal to `1`"
            )

        self._key = key

    @property
    def text(self):
        """Gets the text of this EnumText.

        Display text in German language.

        :return: The text of this EnumText.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EnumText.

        Display text in German language.

        :param text: The text of this EnumText.
        :type: str
        """
        if text is not None and len(text) > 65:
            raise ValueError(
                "Invalid value for `text`, length must be less than or equal to `65`"
            )
        if text is not None and len(text) < 0:
            raise ValueError(
                "Invalid value for `text`, length must be greater than or equal to `0`"
            )

        self._text = text

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
        if issubclass(EnumText, dict):
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
        if not isinstance(other, EnumText):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnumText):
            return True

        return self.to_dict() != other.to_dict()
