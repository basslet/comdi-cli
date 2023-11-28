import pprint


class BusinessMessage(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "key": "str",
        "severity": "str",
        "message": "str",
        "origin": "list[str]",
        "args": "list[object]",
    }

    attribute_map = {
        "key": "key",
        "severity": "severity",
        "message": "message",
        "origin": "origin",
        "args": "args",
    }

    def __init__(self, key=None, severity=None, message=None, origin=None, args=None):
        """BusinessMessage"""

        self._key = None
        self._severity = None
        self._message = None
        self._origin = None
        self._args = None

        if key is not None:
            self.key = key
        if severity is not None:
            self.severity = severity
        if message is not None:
            self.message = message
        if origin is not None:
            self.origin = origin
        if args is not None:
            self.args = args

    @property
    def key(self):
        """Gets the key of this BusinessMessage.

        Identifier for the error

        :return: The key of this BusinessMessage.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this BusinessMessage.

        Identifier for the error

        :param key: The key of this BusinessMessage.
        :type: str
        """
        allowed_values = ["request.object.invalid", "request.query.invalid", "expired"]
        if key not in allowed_values:
            raise ValueError(
                "Invalid value for `key` ({0}), must be one of {1}".format(
                    key, allowed_values
                )
            )

        self._key = key

    @property
    def severity(self):
        """Gets the severity of this BusinessMessage.

        Severity level of the error

        :return: The severity of this BusinessMessage.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this BusinessMessage.

        Severity level of the error

        :param severity: The severity of this BusinessMessage.
        :type: str
        """
        allowed_values = ["ERROR", "INFO", "WARN"]
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}".format(
                    severity, allowed_values
                )
            )

        self._severity = severity

    @property
    def message(self):
        """Gets the message of this BusinessMessage.

        Default error message

        :return: The message of this BusinessMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BusinessMessage.

        Default error message

        :param message: The message of this BusinessMessage.
        :type: str
        """

        self._message = message

    @property
    def origin(self):
        """Gets the origin of this BusinessMessage.

        List of properties causing validation errors

        :return: The origin of this BusinessMessage.
        :rtype: list[str]
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BusinessMessage.

        List of properties causing validation errors

        :param origin: The origin of this BusinessMessage.
        :type: list[str]
        """

        self._origin = origin

    @property
    def args(self):
        """Gets the args of this BusinessMessage.

        Arguments for the error message

        :return: The args of this BusinessMessage.
        :rtype: list[object]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this BusinessMessage.

        Arguments for the error message

        :param args: The args of this BusinessMessage.
        :type: list[object]
        """

        self._args = args

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
        if issubclass(BusinessMessage, dict):
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
        if not isinstance(other, BusinessMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BusinessMessage):
            return True

        return self.to_dict() != other.to_dict()
