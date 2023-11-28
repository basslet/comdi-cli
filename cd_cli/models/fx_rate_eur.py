import pprint


class FXRateEUR(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"bid": "AmountValue", "ask": "AmountValue"}

    attribute_map = {"bid": "bid", "ask": "ask"}

    def __init__(self, bid=None, ask=None):
        """FXRateEUR"""

        self._bid = None
        self._ask = None

        if bid is not None:
            self.bid = bid
        if ask is not None:
            self.ask = ask

    @property
    def bid(self):
        """Gets the bid of this FXRateEUR.

        Bid rate of settlement currency to FX

        :return: The bid of this FXRateEUR.
        :rtype: AmountValue
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this FXRateEUR.

        Bid rate of settlement currency to FX

        :param bid: The bid of this FXRateEUR.
        :type: AmountValue
        """

        self._bid = bid

    @property
    def ask(self):
        """Gets the ask of this FXRateEUR.

        Ask rate of settlement currency to FX

        :return: The ask of this FXRateEUR.
        :rtype: AmountValue
        """
        return self._ask

    @ask.setter
    def ask(self, ask):
        """Sets the ask of this FXRateEUR.

        Ask rate of settlement currency to FX

        :param ask: The ask of this FXRateEUR.
        :type: AmountValue
        """

        self._ask = ask

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
        if issubclass(FXRateEUR, dict):
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
        if not isinstance(other, FXRateEUR):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FXRateEUR):
            return True

        return self.to_dict() != other.to_dict()
