import pprint


class CurrencyString(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"currency": "str"}

    attribute_map = {"currency": "Currency"}

    def __init__(self, currency=None):
        """CurrencyString"""

        self._currency = None

        if currency is not None:
            self.currency = currency

    @property
    def currency(self):
        """Gets the currency of this CurrencyString.


        :return: The currency of this CurrencyString.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CurrencyString.


        :param currency: The currency of this CurrencyString.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError(
                "Invalid value for `currency`, length must be less than or equal to `3`"
            )
        if currency is not None and len(currency) < 3:
            raise ValueError(
                "Invalid value for `currency`, length must be greater than or equal to `3`"
            )

        self._currency = currency

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
        if issubclass(CurrencyString, dict):
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
        if not isinstance(other, CurrencyString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyString):
            return True

        return self.to_dict() != other.to_dict()
