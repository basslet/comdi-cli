import pprint


class ListResourceDepot(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "paging": "PagingInfo",
        "aggregated": "AggregatedInfo",
        "values": "list[Depot]",
    }

    attribute_map = {"paging": "paging", "aggregated": "aggregated", "values": "values"}

    def __init__(self, paging=None, aggregated=None, values=None):
        """ListResourceDepot"""

        self._paging = None
        self._aggregated = None
        self._values = None

        if paging is not None:
            self.paging = paging
        if aggregated is not None:
            self.aggregated = aggregated
        if values is not None:
            self.values = values

    @property
    def paging(self):
        """Gets the paging of this ListResourceDepot.


        :return: The paging of this ListResourceDepot.
        :rtype: PagingInfo
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this ListResourceDepot.


        :param paging: The paging of this ListResourceDepot.
        :type: PagingInfo
        """

        self._paging = paging

    @property
    def aggregated(self):
        """Gets the aggregated of this ListResourceDepot.


        :return: The aggregated of this ListResourceDepot.
        :rtype: AggregatedInfo
        """
        return self._aggregated

    @aggregated.setter
    def aggregated(self, aggregated):
        """Sets the aggregated of this ListResourceDepot.


        :param aggregated: The aggregated of this ListResourceDepot.
        :type: AggregatedInfo
        """

        self._aggregated = aggregated

    @property
    def values(self):
        """Gets the values of this ListResourceDepot.


        :return: The values of this ListResourceDepot.
        :rtype: list[Depot]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ListResourceDepot.


        :param values: The values of this ListResourceDepot.
        :type: list[Depot]
        """

        self._values = values

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
        if issubclass(ListResourceDepot, dict):
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
        if not isinstance(other, ListResourceDepot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListResourceDepot):
            return True

        return self.to_dict() != other.to_dict()
