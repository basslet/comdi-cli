import pprint


class ProductBalance(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "product_id": "str",
        "product_type": "str",
        "target_client_id": "str",
        "client_connection_type": "str",
        "balance": "Balance",
    }

    attribute_map = {
        "product_id": "productId",
        "product_type": "productType",
        "target_client_id": "targetClientId",
        "client_connection_type": "clientConnectionType",
        "balance": "balance",
    }

    def __init__(
        self,
        product_id=None,
        product_type=None,
        target_client_id=None,
        client_connection_type=None,
        balance=None,
    ):
        """ProductBalance"""

        self._product_id = None
        self._product_type = None
        self._target_client_id = None
        self._client_connection_type = None
        self._balance = None

        if product_id is not None:
            self.product_id = product_id
        if product_type is not None:
            self.product_type = product_type
        if target_client_id is not None:
            self.target_client_id = target_client_id
        if client_connection_type is not None:
            self.client_connection_type = client_connection_type
        if balance is not None:
            self.balance = balance

    @property
    def product_id(self):
        """Gets the product_id of this ProductBalance.

        Unique ID of the product (UUID).

        :return: The product_id of this ProductBalance.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductBalance.

        Unique ID of the product (UUID).

        :param product_id: The product_id of this ProductBalance.
        :type: str
        """

        self._product_id = product_id

    @property
    def product_type(self):
        """Gets the product_type of this ProductBalance.

        Type of the product.

        :return: The product_type of this ProductBalance.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ProductBalance.

        Type of the product.

        :param product_type: The product_type of this ProductBalance.
        :type: str
        """
        allowed_values = ["ACCOUNT", "CARD", "DEPOT", "LOAN", "SAVINGS"]
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}".format(
                    product_type, allowed_values
                )
            )

        self._product_type = product_type

    @property
    def target_client_id(self):
        """Gets the target_client_id of this ProductBalance.

        Unique Id of the target client (UUID).

        :return: The target_client_id of this ProductBalance.
        :rtype: str
        """
        return self._target_client_id

    @target_client_id.setter
    def target_client_id(self, target_client_id):
        """Sets the target_client_id of this ProductBalance.

        Unique Id of the target client (UUID).

        :param target_client_id: The target_client_id of this ProductBalance.
        :type: str
        """

        self._target_client_id = target_client_id

    @property
    def client_connection_type(self):
        """Gets the client_connection_type of this ProductBalance.

        Type of the client connection.

        :return: The client_connection_type of this ProductBalance.
        :rtype: str
        """
        return self._client_connection_type

    @client_connection_type.setter
    def client_connection_type(self, client_connection_type):
        """Sets the client_connection_type of this ProductBalance.

        Type of the client connection.

        :param client_connection_type: The client_connection_type of this ProductBalance.
        :type: str
        """
        allowed_values = ["CURRENT_CLIENT", "OTHER_COMDIRECT", "OTHER_EXTERNAL"]
        if client_connection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `client_connection_type` ({0}), must be one of {1}".format(
                    client_connection_type, allowed_values
                )
            )

        self._client_connection_type = client_connection_type

    @property
    def balance(self):
        """Gets the balance of this ProductBalance.

        Balance object based on the product type.

        :return: The balance of this ProductBalance.
        :rtype: Balance
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ProductBalance.

        Balance object based on the product type.

        :param balance: The balance of this ProductBalance.
        :type: Balance
        """

        self._balance = balance

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
        if issubclass(ProductBalance, dict):
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
        if not isinstance(other, ProductBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductBalance):
            return True

        return self.to_dict() != other.to_dict()
