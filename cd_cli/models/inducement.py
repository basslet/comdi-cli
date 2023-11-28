import pprint


class Inducement(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"amount": "AmountValue", "estimated": "bool"}

    attribute_map = {"amount": "amount", "estimated": "estimated"}

    def __init__(self, amount=None, estimated=False):
        """Inducement"""

        self._amount = None
        self._estimated = None

        if amount is not None:
            self.amount = amount
        if estimated is not None:
            self.estimated = estimated

    @property
    def amount(self):
        """Gets the amount of this Inducement.

        Amount of the inducement

        :return: The amount of this Inducement.
        :rtype: AmountValue
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Inducement.

        Amount of the inducement

        :param amount: The amount of this Inducement.
        :type: AmountValue
        """

        self._amount = amount

    @property
    def estimated(self):
        """Gets the estimated of this Inducement.

        TRUE, if the amount is an estimation

        :return: The estimated of this Inducement.
        :rtype: bool
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated):
        """Sets the estimated of this Inducement.

        TRUE, if the amount is an estimation

        :param estimated: The estimated of this Inducement.
        :type: bool
        """

        self._estimated = estimated

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
        if issubclass(Inducement, dict):
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
        if not isinstance(other, Inducement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Inducement):
            return True

        return self.to_dict() != other.to_dict()
