import pprint


class TotalHoldingCostBlock(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "year1": "TotalHoldingCostEntry",
        "year2": "TotalHoldingCostEntry",
        "sales": "TotalHoldingCostEntry",
    }

    attribute_map = {"year1": "year1", "year2": "year2", "sales": "sales"}

    def __init__(self, year1=None, year2=None, sales=None):
        """TotalHoldingCostBlock"""

        self._year1 = None
        self._year2 = None
        self._sales = None

        if year1 is not None:
            self.year1 = year1
        if year2 is not None:
            self.year2 = year2
        if sales is not None:
            self.sales = sales

    @property
    def year1(self):
        """Gets the year1 of this TotalHoldingCostBlock.

        Total holding cost entry for the first year

        :return: The year1 of this TotalHoldingCostBlock.
        :rtype: TotalHoldingCostEntry
        """
        return self._year1

    @year1.setter
    def year1(self, year1):
        """Sets the year1 of this TotalHoldingCostBlock.

        Total holding cost entry for the first year

        :param year1: The year1 of this TotalHoldingCostBlock.
        :type: TotalHoldingCostEntry
        """

        self._year1 = year1

    @property
    def year2(self):
        """Gets the year2 of this TotalHoldingCostBlock.

        Total holding cost entry for the second year

        :return: The year2 of this TotalHoldingCostBlock.
        :rtype: TotalHoldingCostEntry
        """
        return self._year2

    @year2.setter
    def year2(self, year2):
        """Sets the year2 of this TotalHoldingCostBlock.

        Total holding cost entry for the second year

        :param year2: The year2 of this TotalHoldingCostBlock.
        :type: TotalHoldingCostEntry
        """

        self._year2 = year2

    @property
    def sales(self):
        """Gets the sales of this TotalHoldingCostBlock.

        Total holding cost entry for the year of the sale

        :return: The sales of this TotalHoldingCostBlock.
        :rtype: TotalHoldingCostEntry
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this TotalHoldingCostBlock.

        Total holding cost entry for the year of the sale

        :param sales: The sales of this TotalHoldingCostBlock.
        :type: TotalHoldingCostEntry
        """

        self._sales = sales

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
        if issubclass(TotalHoldingCostBlock, dict):
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
        if not isinstance(other, TotalHoldingCostBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TotalHoldingCostBlock):
            return True

        return self.to_dict() != other.to_dict()
