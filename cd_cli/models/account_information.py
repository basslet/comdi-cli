import pprint


class AccountInformation(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"holder_name": "str", "iban": "str", "bic": "str"}

    attribute_map = {"holder_name": "holderName", "iban": "iban", "bic": "bic"}

    def __init__(self, holder_name=None, iban=None, bic=None):
        """AccountInformation"""

        self._holder_name = None
        self._iban = None
        self._bic = None

        if holder_name is not None:
            self.holder_name = holder_name
        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic

    @property
    def holder_name(self):
        """Gets the holder_name of this AccountInformation.

        name of the account owner

        :return: The holder_name of this AccountInformation.
        :rtype: str
        """
        return self._holder_name

    @holder_name.setter
    def holder_name(self, holder_name):
        """Sets the holder_name of this AccountInformation.

        name of the account owner

        :param holder_name: The holder_name of this AccountInformation.
        :type: str
        """

        self._holder_name = holder_name

    @property
    def iban(self):
        """Gets the iban of this AccountInformation.

        The IBAN (International bank account number) for the account - if available

        :return: The iban of this AccountInformation.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountInformation.

        The IBAN (International bank account number) for the account - if available

        :param iban: The iban of this AccountInformation.
        :type: str
        """

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this AccountInformation.

        The BIC (Bank Identifier Code) for the IBAN - if available

        :return: The bic of this AccountInformation.
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this AccountInformation.

        The BIC (Bank Identifier Code) for the IBAN - if available

        :param bic: The bic of this AccountInformation.
        :type: str
        """

        self._bic = bic

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
        if issubclass(AccountInformation, dict):
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
        if not isinstance(other, AccountInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountInformation):
            return True

        return self.to_dict() != other.to_dict()
