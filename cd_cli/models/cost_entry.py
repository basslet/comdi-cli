import pprint


class CostEntry(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "cost_entry_type": "str",
        "label": "str",
        "amount": "AmountValue",
        "amount_reporting_currency": "AmountValue",
        "inducement": "Inducement",
    }

    attribute_map = {
        "cost_entry_type": "type",
        "label": "label",
        "amount": "amount",
        "amount_reporting_currency": "amountReportingCurrency",
        "inducement": "inducement",
    }

    def __init__(
        self,
        cost_entry_type=None,
        label=None,
        amount=None,
        amount_reporting_currency=None,
        inducement=None,
    ):
        """CostEntry"""

        self._cost_entry_type = None
        self._label = None
        self._amount = None
        self._amount_reporting_currency = None
        self._inducement = None

        if cost_entry_type is not None:
            self.cost_entry_type = cost_entry_type
        if label is not None:
            self.label = label
        if amount is not None:
            self.amount = amount
        if amount_reporting_currency is not None:
            self.amount_reporting_currency = amount_reporting_currency
        if inducement is not None:
            self.inducement = inducement

    @property
    def cost_entry_type(self):
        """Gets the type of this CostEntry.

        Type of the cost entry

        :return: The type of this CostEntry.
        :rtype: str
        """
        return self._cost_entry_type

    @cost_entry_type.setter
    def cost_entry_type(self, cost_entry_type):
        """Sets the type of this CostEntry.

        Type of the cost entry

        :param type: The type of this CostEntry.
        :type: str
        """
        allowed_values = ["E", "F", "P"]
        if cost_entry_type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(
                    cost_entry_type, allowed_values
                )
            )

        self._cost_entry_type = cost_entry_type

    @property
    def label(self):
        """Gets the label of this CostEntry.

        Label of the cost entry

        :return: The label of this CostEntry.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CostEntry.

        Label of the cost entry

        :param label: The label of this CostEntry.
        :type: str
        """

        self._label = label

    @property
    def amount(self):
        """Gets the amount of this CostEntry.

        Cost in trading currency

        :return: The amount of this CostEntry.
        :rtype: AmountValue
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CostEntry.

        Cost in trading currency

        :param amount: The amount of this CostEntry.
        :type: AmountValue
        """

        self._amount = amount

    @property
    def amount_reporting_currency(self):
        """Gets the amount_reporting_currency of this CostEntry.

        Cost in reporting currency

        :return: The amount_reporting_currency of this CostEntry.
        :rtype: AmountValue
        """
        return self._amount_reporting_currency

    @amount_reporting_currency.setter
    def amount_reporting_currency(self, amount_reporting_currency):
        """Sets the amount_reporting_currency of this CostEntry.

        Cost in reporting currency

        :param amount_reporting_currency: The amount_reporting_currency of this CostEntry.
        :type: AmountValue
        """

        self._amount_reporting_currency = amount_reporting_currency

    @property
    def inducement(self):
        """Gets the inducement of this CostEntry.

        Inducement of the cost entry

        :return: The inducement of this CostEntry.
        :rtype: Inducement
        """
        return self._inducement

    @inducement.setter
    def inducement(self, inducement):
        """Sets the inducement of this CostEntry.

        Inducement of the cost entry

        :param inducement: The inducement of this CostEntry.
        :type: Inducement
        """

        self._inducement = inducement

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
        if issubclass(CostEntry, dict):
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
        if not isinstance(other, CostEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostEntry):
            return True

        return self.to_dict() != other.to_dict()
