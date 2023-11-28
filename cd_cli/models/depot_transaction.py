import pprint


class DepotTransaction(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "transaction_id": "str",
        "booking_status": "str",
        "booking_date": "DateString",
        "settlement_date": "DateTimeString",
        "business_date": "DateString",
        "quantity": "AmountValue",
        "instrument_id": "str",
        "instrument": "Instrument",
        "execution_price": "AmountValue",
        "transaction_value": "AmountValue",
        "transaction_direction": "str",
        "transaction_type": "str",
        "fx_rate": "FXRateEUR",
    }

    attribute_map = {
        "transaction_id": "transactionId",
        "booking_status": "bookingStatus",
        "booking_date": "bookingDate",
        "settlement_date": "settlementDate",
        "business_date": "businessDate",
        "quantity": "quantity",
        "instrument_id": "instrumentId",
        "instrument": "instrument",
        "execution_price": "executionPrice",
        "transaction_value": "transactionValue",
        "transaction_direction": "transactionDirection",
        "transaction_type": "transactionType",
        "fx_rate": "fxRate",
    }

    def __init__(
        self,
        transaction_id=None,
        booking_status=None,
        booking_date=None,
        settlement_date=None,
        business_date=None,
        quantity=None,
        instrument_id=None,
        instrument=None,
        execution_price=None,
        transaction_value=None,
        transaction_direction=None,
        transaction_type=None,
        fx_rate=None,
    ):
        """DepotTransaction"""

        self._transaction_id = None
        self._booking_status = None
        self._booking_date = None
        self._settlement_date = None
        self._business_date = None
        self._quantity = None
        self._instrument_id = None
        self._instrument = None
        self._execution_price = None
        self._transaction_value = None
        self._transaction_direction = None
        self._transaction_type = None
        self._fx_rate = None

        if transaction_id is not None:
            self.transaction_id = transaction_id
        if booking_status is not None:
            self.booking_status = booking_status
        if booking_date is not None:
            self.booking_date = booking_date
        if settlement_date is not None:
            self.settlement_date = settlement_date
        if business_date is not None:
            self.business_date = business_date
        if quantity is not None:
            self.quantity = quantity
        if instrument_id is not None:
            self.instrument_id = instrument_id
        if instrument is not None:
            self.instrument = instrument
        if execution_price is not None:
            self.execution_price = execution_price
        if transaction_value is not None:
            self.transaction_value = transaction_value
        if transaction_direction is not None:
            self.transaction_direction = transaction_direction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if fx_rate is not None:
            self.fx_rate = fx_rate

    @property
    def transaction_id(self):
        """Gets the transaction_id of this DepotTransaction.

        Transaction Identifier (UUID)

        :return: The transaction_id of this DepotTransaction.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this DepotTransaction.

        Transaction Identifier (UUID)

        :param transaction_id: The transaction_id of this DepotTransaction.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def booking_status(self):
        """Gets the booking_status of this DepotTransaction.

        Status of transaction

        :return: The booking_status of this DepotTransaction.
        :rtype: str
        """
        return self._booking_status

    @booking_status.setter
    def booking_status(self, booking_status):
        """Sets the booking_status of this DepotTransaction.

        Status of transaction

        :param booking_status: The booking_status of this DepotTransaction.
        :type: str
        """
        allowed_values = ["BOOKED", "NOTBOOKED"]
        if booking_status not in allowed_values:
            raise ValueError(
                "Invalid value for `booking_status` ({0}), must be one of {1}".format(
                    booking_status, allowed_values
                )
            )

        self._booking_status = booking_status

    @property
    def booking_date(self):
        """Gets the booking_date of this DepotTransaction.

        The booking date

        :return: The booking_date of this DepotTransaction.
        :rtype: DateString
        """
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        """Sets the booking_date of this DepotTransaction.

        The booking date

        :param booking_date: The booking_date of this DepotTransaction.
        :type: DateString
        """

        self._booking_date = booking_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this DepotTransaction.

        Date and time of settlement

        :return: The settlement_date of this DepotTransaction.
        :rtype: DateTimeString
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this DepotTransaction.

        Date and time of settlement

        :param settlement_date: The settlement_date of this DepotTransaction.
        :type: DateTimeString
        """

        self._settlement_date = settlement_date

    @property
    def business_date(self):
        """Gets the business_date of this DepotTransaction.

        The business date

        :return: The business_date of this DepotTransaction.
        :rtype: DateString
        """
        return self._business_date

    @business_date.setter
    def business_date(self, business_date):
        """Sets the business_date of this DepotTransaction.

        The business date

        :param business_date: The business_date of this DepotTransaction.
        :type: DateString
        """

        self._business_date = business_date

    @property
    def quantity(self):
        """Gets the quantity of this DepotTransaction.

        The quantity

        :return: The quantity of this DepotTransaction.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DepotTransaction.

        The quantity

        :param quantity: The quantity of this DepotTransaction.
        :type: AmountValue
        """

        self._quantity = quantity

    @property
    def instrument_id(self):
        """Gets the instrument_id of this DepotTransaction.

        InstrumentId as UUID

        :return: The instrument_id of this DepotTransaction.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this DepotTransaction.

        InstrumentId as UUID

        :param instrument_id: The instrument_id of this DepotTransaction.
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def instrument(self):
        """Gets the instrument of this DepotTransaction.

        Information about the instrument of the securities position

        :return: The instrument of this DepotTransaction.
        :rtype: Instrument
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this DepotTransaction.

        Information about the instrument of the securities position

        :param instrument: The instrument of this DepotTransaction.
        :type: Instrument
        """

        self._instrument = instrument

    @property
    def execution_price(self):
        """Gets the execution_price of this DepotTransaction.

        Price of the execution

        :return: The execution_price of this DepotTransaction.
        :rtype: AmountValue
        """
        return self._execution_price

    @execution_price.setter
    def execution_price(self, execution_price):
        """Sets the execution_price of this DepotTransaction.

        Price of the execution

        :param execution_price: The execution_price of this DepotTransaction.
        :type: AmountValue
        """

        self._execution_price = execution_price

    @property
    def transaction_value(self):
        """Gets the transaction_value of this DepotTransaction.

        Value of the transaction

        :return: The transaction_value of this DepotTransaction.
        :rtype: AmountValue
        """
        return self._transaction_value

    @transaction_value.setter
    def transaction_value(self, transaction_value):
        """Sets the transaction_value of this DepotTransaction.

        Value of the transaction

        :param transaction_value: The transaction_value of this DepotTransaction.
        :type: AmountValue
        """

        self._transaction_value = transaction_value

    @property
    def transaction_direction(self):
        """Gets the transaction_direction of this DepotTransaction.

        Transaction direction

        :return: The transaction_direction of this DepotTransaction.
        :rtype: str
        """
        return self._transaction_direction

    @transaction_direction.setter
    def transaction_direction(self, transaction_direction):
        """Sets the transaction_direction of this DepotTransaction.

        Transaction direction

        :param transaction_direction: The transaction_direction of this DepotTransaction.
        :type: str
        """
        allowed_values = ["IN", "OUT"]
        if transaction_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_direction` ({0}), must be one of {1}".format(
                    transaction_direction, allowed_values
                )
            )

        self._transaction_direction = transaction_direction

    @property
    def transaction_type(self):
        """Gets the transaction_type of this DepotTransaction.

        On the basis of securities account turnover transaction type

        :return: The transaction_type of this DepotTransaction.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this DepotTransaction.

        On the basis of securities account turnover transaction type

        :param transaction_type: The transaction_type of this DepotTransaction.
        :type: str
        """
        allowed_values = ["BUY", "SELL", "TRANSFER_IN", "TRANSFER_OUT", "OTHER"]
        if transaction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}".format(
                    transaction_type, allowed_values
                )
            )

        self._transaction_type = transaction_type

    @property
    def fx_rate(self):
        """Gets the fx_rate of this DepotTransaction.

        Exchange rate settlement currency EUR to FX if exectionPrice amount is not notated in EUR

        :return: The fx_rate of this DepotTransaction.
        :rtype: FXRateEUR
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """Sets the fx_rate of this DepotTransaction.

        Exchange rate settlement currency EUR to FX if exectionPrice amount is not notated in EUR

        :param fx_rate: The fx_rate of this DepotTransaction.
        :type: FXRateEUR
        """

        self._fx_rate = fx_rate

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
        if issubclass(DepotTransaction, dict):
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
        if not isinstance(other, DepotTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepotTransaction):
            return True

        return self.to_dict() != other.to_dict()
