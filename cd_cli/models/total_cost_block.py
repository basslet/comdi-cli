import pprint


class TotalCostBlock(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "service_costs": "TotalCostEntry",
        "service_inducement": "AmountValue",
        "external_costs": "TotalCostEntry",
        "product_costs": "TotalCostEntry",
    }

    attribute_map = {
        "service_costs": "serviceCosts",
        "service_inducement": "serviceInducement",
        "external_costs": "externalCosts",
        "product_costs": "productCosts",
    }

    def __init__(
        self,
        service_costs=None,
        service_inducement=None,
        external_costs=None,
        product_costs=None,
    ):
        """TotalCostBlock"""

        self._service_costs = None
        self._service_inducement = None
        self._external_costs = None
        self._product_costs = None

        if service_costs is not None:
            self.service_costs = service_costs
        if service_inducement is not None:
            self.service_inducement = service_inducement
        if external_costs is not None:
            self.external_costs = external_costs
        if product_costs is not None:
            self.product_costs = product_costs

    @property
    def service_costs(self):
        """Gets the service_costs of this TotalCostBlock.

        Total cost entry for own service costs of bank (E)

        :return: The service_costs of this TotalCostBlock.
        :rtype: TotalCostEntry
        """
        return self._service_costs

    @service_costs.setter
    def service_costs(self, service_costs):
        """Sets the service_costs of this TotalCostBlock.

        Total cost entry for own service costs of bank (E)

        :param service_costs: The service_costs of this TotalCostBlock.
        :type: TotalCostEntry
        """

        self._service_costs = service_costs

    @property
    def service_inducement(self):
        """Gets the service_inducement of this TotalCostBlock.

        Total amount of inducements for own service costs of bank

        :return: The service_inducement of this TotalCostBlock.
        :rtype: AmountValue
        """
        return self._service_inducement

    @service_inducement.setter
    def service_inducement(self, service_inducement):
        """Sets the service_inducement of this TotalCostBlock.

        Total amount of inducements for own service costs of bank

        :param service_inducement: The service_inducement of this TotalCostBlock.
        :type: AmountValue
        """

        self._service_inducement = service_inducement

    @property
    def external_costs(self):
        """Gets the external_costs of this TotalCostBlock.

        Total cost entry for external service costs (F)

        :return: The external_costs of this TotalCostBlock.
        :rtype: TotalCostEntry
        """
        return self._external_costs

    @external_costs.setter
    def external_costs(self, external_costs):
        """Sets the external_costs of this TotalCostBlock.

        Total cost entry for external service costs (F)

        :param external_costs: The external_costs of this TotalCostBlock.
        :type: TotalCostEntry
        """

        self._external_costs = external_costs

    @property
    def product_costs(self):
        """Gets the product_costs of this TotalCostBlock.

        Total cost entry for product costs (P)

        :return: The product_costs of this TotalCostBlock.
        :rtype: TotalCostEntry
        """
        return self._product_costs

    @product_costs.setter
    def product_costs(self, product_costs):
        """Sets the product_costs of this TotalCostBlock.

        Total cost entry for product costs (P)

        :param product_costs: The product_costs of this TotalCostBlock.
        :type: TotalCostEntry
        """

        self._product_costs = product_costs

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
        if issubclass(TotalCostBlock, dict):
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
        if not isinstance(other, TotalCostBlock):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TotalCostBlock):
            return True

        return self.to_dict() != other.to_dict()
