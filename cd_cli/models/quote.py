import pprint


class Quote(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot_id": "str",
        "side": "str",
        "instrument_id": "str",
        "venue_id": "str",
        "quantity": "AmountValue",
    }

    attribute_map = {
        "depot_id": "depotId",
        "side": "side",
        "instrument_id": "instrumentId",
        "venue_id": "venueId",
        "quantity": "quantity",
    }

    def __init__(
        self, depot_id=None, side=None, instrument_id=None, venue_id=None, quantity=None
    ):
        """Quote"""

        self._depot_id = None
        self._side = None
        self._instrument_id = None
        self._venue_id = None
        self._quantity = None

        if depot_id is not None:
            self.depot_id = depot_id
        if side is not None:
            self.side = side
        if instrument_id is not None:
            self.instrument_id = instrument_id
        if venue_id is not None:
            self.venue_id = venue_id
        if quantity is not None:
            self.quantity = quantity

    @property
    def depot_id(self):
        """Gets the depot_id of this Quote.

        Unique securities account identification (as UUID)

        :return: The depot_id of this Quote.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this Quote.

        Unique securities account identification (as UUID)

        :param depot_id: The depot_id of this Quote.
        :type: str
        """
        if depot_id is not None and len(depot_id) > 40:
            raise ValueError(
                "Invalid value for `depot_id`, length must be less than or equal to `40`"
            )
        if depot_id is not None and len(depot_id) < 0:
            raise ValueError(
                "Invalid value for `depot_id`, length must be greater than or equal to `0`"
            )

        self._depot_id = depot_id

    @property
    def side(self):
        """Gets the side of this Quote.

        Type of transaction

        :return: The side of this Quote.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Quote.

        Type of transaction

        :param side: The side of this Quote.
        :type: str
        """
        allowed_values = ["BUY", "SELL"]
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}".format(
                    side, allowed_values
                )
            )

        self._side = side

    @property
    def instrument_id(self):
        """Gets the instrument_id of this Quote.

        WKN, ISIN or uuId; wkn will be returned if instrumentId is entered as wkn, an ISIN is returned if instrumentId is entered as ISIN, a uuId is returned if instrumentId is entered as uuId

        :return: The instrument_id of this Quote.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this Quote.

        WKN, ISIN or uuId; wkn will be returned if instrumentId is entered as wkn, an ISIN is returned if instrumentId is entered as ISIN, a uuId is returned if instrumentId is entered as uuId

        :param instrument_id: The instrument_id of this Quote.
        :type: str
        """
        if instrument_id is not None and len(instrument_id) > 40:
            raise ValueError(
                "Invalid value for `instrument_id`, length must be less than or equal to `40`"
            )
        if instrument_id is not None and len(instrument_id) < 0:
            raise ValueError(
                "Invalid value for `instrument_id`, length must be greater than or equal to `0`"
            )

        self._instrument_id = instrument_id

    @property
    def venue_id(self):
        """Gets the venue_id of this Quote.

        UUID of the trading venue or partner. This is mandatory, if isBestEx=FALSE

        :return: The venue_id of this Quote.
        :rtype: str
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this Quote.

        UUID of the trading venue or partner. This is mandatory, if isBestEx=FALSE

        :param venue_id: The venue_id of this Quote.
        :type: str
        """
        if venue_id is not None and len(venue_id) > 40:
            raise ValueError(
                "Invalid value for `venue_id`, length must be less than or equal to `40`"
            )
        if venue_id is not None and len(venue_id) < 0:
            raise ValueError(
                "Invalid value for `venue_id`, length must be greater than or equal to `0`"
            )

        self._venue_id = venue_id

    @property
    def quantity(self):
        """Gets the quantity of this Quote.

        Quantity or nominal amount in the case of a percentage quotation

        :return: The quantity of this Quote.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Quote.

        Quantity or nominal amount in the case of a percentage quotation

        :param quantity: The quantity of this Quote.
        :type: AmountValue
        """

        self._quantity = quantity

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
        if issubclass(Quote, dict):
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
        if not isinstance(other, Quote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quote):
            return True

        return self.to_dict() != other.to_dict()
