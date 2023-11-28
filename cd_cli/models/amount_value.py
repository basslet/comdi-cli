import pprint


class AmountValue(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"value": "str", "unit": "str"}

    attribute_map = {"value": "value", "unit": "unit"}

    def __init__(self, value=None, unit=None):
        """AmountValue"""

        self._value = None
        self._unit = None

        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def value(self):
        """Gets the value of this AmountValue.

        Nominal value in corresponding unit

        :return: The value of this AmountValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AmountValue.

        Nominal value in corresponding unit

        :param value: The value of this AmountValue.
        :type: str
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this AmountValue.

        {XXX, XXC, XXM, XXP, XXU} or currencies according to ISO-4217 (EUR, USD, GBP,...)

        :return: The unit of this AmountValue.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AmountValue.

        {XXX, XXC, XXM, XXP, XXU} or currencies according to ISO-4217 (EUR, USD, GBP,...)

        :param unit: The unit of this AmountValue.
        :type: str
        """
        if unit is not None and len(unit) > 3:
            raise ValueError(
                "Invalid value for `unit`, length must be less than or equal to `3`"
            )
        if unit is not None and len(unit) < 3:
            raise ValueError(
                "Invalid value for `unit`, length must be greater than or equal to `3`"
            )

        self._unit = unit

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
        if issubclass(AmountValue, dict):
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
        if not isinstance(other, AmountValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmountValue):
            return True

        return self.to_dict() != other.to_dict()
