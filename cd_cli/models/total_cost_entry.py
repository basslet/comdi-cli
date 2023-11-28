import pprint


class TotalCostEntry(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "total_cost_entry_type": "str",
        "label": "str",
        "amount": "AmountValue",
        "average_return_pa": "PercentageString",
    }

    attribute_map = {
        "total_cost_entry_type": "type",
        "label": "label",
        "amount": "amount",
        "average_return_pa": "averageReturnPA",
    }

    def __init__(
        self,
        total_cost_entry_type=None,
        label=None,
        amount=None,
        average_return_pa=None,
    ):
        """TotalCostEntry"""

        self._total_cost_entry_type = None
        self._label = None
        self._amount = None
        self._average_return_pa = None

        if total_cost_entry_type is not None:
            self.total_cost_entry_type = total_cost_entry_type
        if label is not None:
            self.label = label
        if amount is not None:
            self.amount = amount
        if average_return_pa is not None:
            self.average_return_pa = average_return_pa

    @property
    def total_cost_entry_type(self):
        """Gets the type of this TotalCostEntry.

        Type of total cost entry

        :return: The type of this TotalCostEntry.
        :rtype: str
        """
        return self._total_cost_entry_type

    @total_cost_entry_type.setter
    def total_cost_entry_type(self, total_cost_entry_type):
        """Sets the type of this TotalCostEntry.

        Type of total cost entry

        :param type: The type of this TotalCostEntry.
        :type: str
        """
        allowed_values = ["E", "F", "P"]
        if total_cost_entry_type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(
                    total_cost_entry_type, allowed_values
                )
            )

        self._total_cost_entry_type = total_cost_entry_type

    @property
    def label(self):
        """Gets the label of this TotalCostEntry.

        Label of total cost entry

        :return: The label of this TotalCostEntry.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TotalCostEntry.

        Label of total cost entry

        :param label: The label of this TotalCostEntry.
        :type: str
        """

        self._label = label

    @property
    def amount(self):
        """Gets the amount of this TotalCostEntry.

        Total cost in reporting currency

        :return: The amount of this TotalCostEntry.
        :rtype: AmountValue
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TotalCostEntry.

        Total cost in reporting currency

        :param amount: The amount of this TotalCostEntry.
        :type: AmountValue
        """

        self._amount = amount

    @property
    def average_return_pa(self):
        """Gets the average_return_pa of this TotalCostEntry.

        Average return reduction per year

        :return: The average_return_pa of this TotalCostEntry.
        :rtype: PercentageString
        """
        return self._average_return_pa

    @average_return_pa.setter
    def average_return_pa(self, average_return_pa):
        """Sets the average_return_pa of this TotalCostEntry.

        Average return reduction per year

        :param average_return_pa: The average_return_pa of this TotalCostEntry.
        :type: PercentageString
        """

        self._average_return_pa = average_return_pa

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
        if issubclass(TotalCostEntry, dict):
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
        if not isinstance(other, TotalCostEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TotalCostEntry):
            return True

        return self.to_dict() != other.to_dict()
