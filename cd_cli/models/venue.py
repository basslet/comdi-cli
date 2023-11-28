import pprint


class Venue(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "name": "str",
        "venue_id": "str",
        "country": "str",
        "venue_type": "str",
        "currencies": "list[CurrencyString]",
        "sides": "list[str]",
        "validity_types": "list[str]",
        "order_types": "dict(str, OrderType)",
    }

    attribute_map = {
        "name": "name",
        "venue_id": "venueId",
        "country": "country",
        "venue_type": "type",
        "currencies": "currencies",
        "sides": "sides",
        "validity_types": "validityTypes",
        "order_types": "orderTypes",
    }

    def __init__(
        self,
        name=None,
        venue_id=None,
        country=None,
        venue_type=None,
        currencies=None,
        sides=None,
        validity_types=None,
        order_types=None,
    ):
        """Venue"""

        self._name = None
        self._venue_id = None
        self._country = None
        self._venue_type = None
        self._currencies = None
        self._sides = None
        self._validity_types = None
        self._order_types = None

        if name is not None:
            self.name = name
        if venue_id is not None:
            self.venue_id = venue_id
        if country is not None:
            self.country = country
        if venue_type is not None:
            self.venue_type = venue_type
        if currencies is not None:
            self.currencies = currencies
        if sides is not None:
            self.sides = sides
        if validity_types is not None:
            self.validity_types = validity_types
        if order_types is not None:
            self.order_types = order_types

    @property
    def name(self):
        """Gets the name of this Venue.


        :return: The name of this Venue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Venue.


        :param name: The name of this Venue.
        :type: str
        """

        self._name = name

    @property
    def venue_id(self):
        """Gets the venue_id of this Venue.


        :return: The venue_id of this Venue.
        :rtype: str
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this Venue.


        :param venue_id: The venue_id of this Venue.
        :type: str
        """

        self._venue_id = venue_id

    @property
    def country(self):
        """Gets the country of this Venue.


        :return: The country of this Venue.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Venue.


        :param country: The country of this Venue.
        :type: str
        """

        self._country = country

    @property
    def venue_type(self):
        """Gets the type of this Venue.


        :return: The type of this Venue.
        :rtype: str
        """
        return self._venue_type

    @venue_type.setter
    def venue_type(self, venue_type):
        """Sets the type of this Venue.


        :param type: The type of this Venue.
        :type: str
        """

        self._venue_type = venue_type

    @property
    def currencies(self):
        """Gets the currencies of this Venue.


        :return: The currencies of this Venue.
        :rtype: list[CurrencyString]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this Venue.


        :param currencies: The currencies of this Venue.
        :type: list[CurrencyString]
        """

        self._currencies = currencies

    @property
    def sides(self):
        """Gets the sides of this Venue.


        :return: The sides of this Venue.
        :rtype: list[str]
        """
        return self._sides

    @sides.setter
    def sides(self, sides):
        """Sets the sides of this Venue.


        :param sides: The sides of this Venue.
        :type: list[str]
        """

        self._sides = sides

    @property
    def validity_types(self):
        """Gets the validity_types of this Venue.


        :return: The validity_types of this Venue.
        :rtype: list[str]
        """
        return self._validity_types

    @validity_types.setter
    def validity_types(self, validity_types):
        """Sets the validity_types of this Venue.


        :param validity_types: The validity_types of this Venue.
        :type: list[str]
        """

        self._validity_types = validity_types

    @property
    def order_types(self):
        """Gets the order_types of this Venue.


        :return: The order_types of this Venue.
        :rtype: dict(str, OrderType)
        """
        return self._order_types

    @order_types.setter
    def order_types(self, order_types):
        """Sets the order_types of this Venue.


        :param order_types: The order_types of this Venue.
        :type: dict(str, OrderType)
        """

        self._order_types = order_types

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
        if issubclass(Venue, dict):
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
        if not isinstance(other, Venue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Venue):
            return True

        return self.to_dict() != other.to_dict()
