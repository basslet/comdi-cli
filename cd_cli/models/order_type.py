import pprint


class OrderType(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "limit_extensions": "list[str]",
        "trading_restrictions": "list[str]",
    }

    attribute_map = {
        "limit_extensions": "limitExtensions",
        "trading_restrictions": "tradingRestrictions",
    }

    def __init__(self, limit_extensions=None, trading_restrictions=None):
        """OrderType"""

        self._limit_extensions = None
        self._trading_restrictions = None

        if limit_extensions is not None:
            self.limit_extensions = limit_extensions
        if trading_restrictions is not None:
            self.trading_restrictions = trading_restrictions

    @property
    def limit_extensions(self):
        """Gets the limit_extensions of this OrderType.

        Names of the possible limit extensions

        :return: The limit_extensions of this OrderType.
        :rtype: list[str]
        """
        return self._limit_extensions

    @limit_extensions.setter
    def limit_extensions(self, limit_extensions):
        """Sets the limit_extensions of this OrderType.

        Names of the possible limit extensions

        :param limit_extensions: The limit_extensions of this OrderType.
        :type: list[str]
        """

        self._limit_extensions = limit_extensions

    @property
    def trading_restrictions(self):
        """Gets the trading_restrictions of this OrderType.

        Names of possible trading restrictions

        :return: The trading_restrictions of this OrderType.
        :rtype: list[str]
        """
        return self._trading_restrictions

    @trading_restrictions.setter
    def trading_restrictions(self, trading_restrictions):
        """Sets the trading_restrictions of this OrderType.

        Names of possible trading restrictions

        :param trading_restrictions: The trading_restrictions of this OrderType.
        :type: list[str]
        """

        self._trading_restrictions = trading_restrictions

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
        if issubclass(OrderType, dict):
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
        if not isinstance(other, OrderType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderType):
            return True

        return self.to_dict() != other.to_dict()
