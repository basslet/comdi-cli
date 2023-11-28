import pprint


class CostGroup(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "cost_group_type": "str",
        "label": "str",
        "cost_group_sum": "AmountValue",
        "sum_reporting_currency": "AmountValue",
        "costs": "list[CostEntry]",
    }

    attribute_map = {
        "cost_group_type": "type",
        "label": "label",
        "cost_group_sum": "sum",
        "sum_reporting_currency": "sumReportingCurrency",
        "costs": "costs",
    }

    def __init__(
        self,
        cost_group_type=None,
        label=None,
        cost_group_sum=None,
        sum_reporting_currency=None,
        costs=None,
    ):
        """CostGroup"""

        self._cost_group_type = None
        self._label = None
        self._cost_group_sum = None
        self._sum_reporting_currency = None
        self._costs = None

        if cost_group_type is not None:
            self.cost_group_type = cost_group_type
        if label is not None:
            self.label = label
        if cost_group_sum is not None:
            self.cost_group_sum = cost_group_sum
        if sum_reporting_currency is not None:
            self.sum_reporting_currency = sum_reporting_currency
        if costs is not None:
            self.costs = costs

    @property
    def cost_group_type(self):
        """Gets the type of this CostGroup.

        Type of cost group. K: Costs of securities purchase, H: Costs of the holding period (per year), V: Costs of the sale of securities

        :return: The type of this CostGroup.
        :rtype: str
        """
        return self._cost_group_type

    @cost_group_type.setter
    def cost_group_type(self, cost_group_type):
        """Sets the type of this CostGroup.

        Type of cost group. K: Costs of securities purchase, H: Costs of the holding period (per year), V: Costs of the sale of securities

        :param type: The type of this CostGroup.
        :type: str
        """
        allowed_values = ["K", "H", "V"]
        if cost_group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(
                    cost_group_type, allowed_values
                )
            )

        self._cost_group_type = type

    @property
    def label(self):
        """Gets the label of this CostGroup.

        Name of cost group for showing in the cost-note

        :return: The label of this CostGroup.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CostGroup.

        Name of cost group for showing in the cost-note

        :param label: The label of this CostGroup.
        :type: str
        """

        self._label = label

    @property
    def cost_group_sum(self):
        """Gets the sum of this CostGroup.

        Sum of the cost group in trading currency (quantity.amount.unit)

        :return: The sum of this CostGroup.
        :rtype: AmountValue
        """
        return self._cost_group_sum

    @cost_group_sum.setter
    def cost_group_sum(self, cost_group_sum):
        """Sets the sum of this CostGroup.

        Sum of the cost group in trading currency (quantity.amount.unit)

        :param sum: The sum of this CostGroup.
        :type: AmountValue
        """

        self._cost_group_sum = cost_group_sum

    @property
    def sum_reporting_currency(self):
        """Gets the sum_reporting_currency of this CostGroup.

        Sum of the cost group in reporting currency

        :return: The sum_reporting_currency of this CostGroup.
        :rtype: AmountValue
        """
        return self._sum_reporting_currency

    @sum_reporting_currency.setter
    def sum_reporting_currency(self, sum_reporting_currency):
        """Sets the sum_reporting_currency of this CostGroup.

        Sum of the cost group in reporting currency

        :param sum_reporting_currency: The sum_reporting_currency of this CostGroup.
        :type: AmountValue
        """

        self._sum_reporting_currency = sum_reporting_currency

    @property
    def costs(self):
        """Gets the costs of this CostGroup.

        List of costs per cost group

        :return: The costs of this CostGroup.
        :rtype: list[CostEntry]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """Sets the costs of this CostGroup.

        List of costs per cost group

        :param costs: The costs of this CostGroup.
        :type: list[CostEntry]
        """

        self._costs = costs

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
        if issubclass(CostGroup, dict):
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
        if not isinstance(other, CostGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostGroup):
            return True

        return self.to_dict() != other.to_dict()
