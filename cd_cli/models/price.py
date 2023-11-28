import pprint


class Price(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "price_type": "str",
        "price": "AmountValue",
        "quantity": "AmountValue",
        "price_date_time": "DateTimeString",
    }

    attribute_map = {
        "price_type": "type",
        "price": "price",
        "quantity": "quantity",
        "price_date_time": "priceDateTime",
    }

    def __init__(
        self, price_type=None, price=None, quantity=None, price_date_time=None
    ):
        """Price"""

        self._price_type = None
        self._price = None
        self._quantity = None
        self._price_date_time = None

        if price_type is not None:
            self.price_type = price_type
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if price_date_time is not None:
            self.price_date_time = price_date_time

    @property
    def price_type(self):
        """Gets the type of this Price.

        Type of the price. Can be one of the following: {LST, BID, ASK, MID}.

        :return: The type of this Price.
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the type of this Price.

        Type of the price. Can be one of the following: {LST, BID, ASK, MID}.

        :param type: The type of this Price.
        :type: str
        """
        if price_type is not None and len(price_type) > 3:
            raise ValueError(
                "Invalid value for `type`, length must be less than or equal to `3`"
            )
        if price_type is not None and len(price_type) < 3:
            raise ValueError(
                "Invalid value for `type`, length must be greater than or equal to `3`"
            )

        self._price_type = price_type

    @property
    def price(self):
        """Gets the price of this Price.

        Price.

        :return: The price of this Price.
        :rtype: AmountValue
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Price.

        Price.

        :param price: The price of this Price.
        :type: AmountValue
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this Price.

        Quantity or nominal amount in case of a percentage quotation.

        :return: The quantity of this Price.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Price.

        Quantity or nominal amount in case of a percentage quotation.

        :param quantity: The quantity of this Price.
        :type: AmountValue
        """

        self._quantity = quantity

    @property
    def price_date_time(self):
        """Gets the price_date_time of this Price.

        Datetime with format: 'yyyy-MM-dd'T'HH:mm:ssX

        :return: The price_date_time of this Price.
        :rtype: DateTimeString
        """
        return self._price_date_time

    @price_date_time.setter
    def price_date_time(self, price_date_time):
        """Sets the price_date_time of this Price.

        Datetime with format: 'yyyy-MM-dd'T'HH:mm:ssX

        :param price_date_time: The price_date_time of this Price.
        :type: DateTimeString
        """

        self._price_date_time = price_date_time

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
        if issubclass(Price, dict):
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
        if not isinstance(other, Price):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Price):
            return True

        return self.to_dict() != other.to_dict()
