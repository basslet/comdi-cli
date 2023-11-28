import pprint


class DepotPosition(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot_id": "str",
        "position_id": "str",
        "wkn": "str",
        "custody_type": "str",
        "quantity": "AmountValue",
        "available_quantity": "AmountValue",
        "current_price": "Price",
        "purchase_price": "AmountValue",
        "prev_day_price": "Price",
        "current_value": "AmountValue",
        "purchase_value": "AmountValue",
        "prev_day_value": "AmountValue",
        "profit_loss_purchase_abs": "AmountValue",
        "profit_loss_purchase_rel": "PercentageString",
        "profit_loss_prev_day_abs": "AmountValue",
        "profit_loss_prev_day_rel": "PercentageString",
        "instrument": "Instrument",
        "version": "str",
    }

    attribute_map = {
        "depot_id": "depotId",
        "position_id": "positionId",
        "wkn": "wkn",
        "custody_type": "custodyType",
        "quantity": "quantity",
        "available_quantity": "availableQuantity",
        "current_price": "currentPrice",
        "purchase_price": "purchasePrice",
        "prev_day_price": "prevDayPrice",
        "current_value": "currentValue",
        "purchase_value": "purchaseValue",
        "prev_day_value": "prevDayValue",
        "profit_loss_purchase_abs": "profitLossPurchaseAbs",
        "profit_loss_purchase_rel": "profitLossPurchaseRel",
        "profit_loss_prev_day_abs": "profitLossPrevDayAbs",
        "profit_loss_prev_day_rel": "profitLossPrevDayRel",
        "instrument": "instrument",
        "version": "version",
    }

    def __init__(
        self,
        depot_id=None,
        position_id=None,
        wkn=None,
        custody_type=None,
        quantity=None,
        available_quantity=None,
        current_price=None,
        purchase_price=None,
        prev_day_price=None,
        current_value=None,
        purchase_value=None,
        prev_day_value=None,
        profit_loss_purchase_abs=None,
        profit_loss_purchase_rel=None,
        profit_loss_prev_day_abs=None,
        profit_loss_prev_day_rel=None,
        instrument=None,
        version=None,
    ):
        """DepotPosition"""

        self._depot_id = None
        self._position_id = None
        self._wkn = None
        self._custody_type = None
        self._quantity = None
        self._available_quantity = None
        self._current_price = None
        self._purchase_price = None
        self._prev_day_price = None
        self._current_value = None
        self._purchase_value = None
        self._prev_day_value = None
        self._profit_loss_purchase_abs = None
        self._profit_loss_purchase_rel = None
        self._profit_loss_prev_day_abs = None
        self._profit_loss_prev_day_rel = None
        self._instrument = None
        self._version = None

        if depot_id is not None:
            self.depot_id = depot_id
        if position_id is not None:
            self.position_id = position_id
        if wkn is not None:
            self.wkn = wkn
        if custody_type is not None:
            self.custody_type = custody_type
        if quantity is not None:
            self.quantity = quantity
        if available_quantity is not None:
            self.available_quantity = available_quantity
        if current_price is not None:
            self.current_price = current_price
        if purchase_price is not None:
            self.purchase_price = purchase_price
        if prev_day_price is not None:
            self.prev_day_price = prev_day_price
        if current_value is not None:
            self.current_value = current_value
        if purchase_value is not None:
            self.purchase_value = purchase_value
        if prev_day_value is not None:
            self.prev_day_value = prev_day_value
        if profit_loss_purchase_abs is not None:
            self.profit_loss_purchase_abs = profit_loss_purchase_abs
        if profit_loss_purchase_rel is not None:
            self.profit_loss_purchase_rel = profit_loss_purchase_rel
        if profit_loss_prev_day_abs is not None:
            self.profit_loss_prev_day_abs = profit_loss_prev_day_abs
        if profit_loss_prev_day_rel is not None:
            self.profit_loss_prev_day_rel = profit_loss_prev_day_rel
        if instrument is not None:
            self.instrument = instrument
        if version is not None:
            self.version = version

    @property
    def depot_id(self):
        """Gets the depot_id of this DepotPosition.

        Securities account Identifier (UUID)

        :return: The depot_id of this DepotPosition.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this DepotPosition.

        Securities account Identifier (UUID)

        :param depot_id: The depot_id of this DepotPosition.
        :type: str
        """

        self._depot_id = depot_id

    @property
    def position_id(self):
        """Gets the position_id of this DepotPosition.

        Position identification number in securities account

        :return: The position_id of this DepotPosition.
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this DepotPosition.

        Position identification number in securities account

        :param position_id: The position_id of this DepotPosition.
        :type: str
        """

        self._position_id = position_id

    @property
    def wkn(self):
        """Gets the wkn of this DepotPosition.

        Identification number of the instrument

        :return: The wkn of this DepotPosition.
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn):
        """Sets the wkn of this DepotPosition.

        Identification number of the instrument

        :param wkn: The wkn of this DepotPosition.
        :type: str
        """

        self._wkn = wkn

    @property
    def custody_type(self):
        """Gets the custody_type of this DepotPosition.

        Custody type

        :return: The custody_type of this DepotPosition.
        :rtype: str
        """
        return self._custody_type

    @custody_type.setter
    def custody_type(self, custody_type):
        """Sets the custody_type of this DepotPosition.

        Custody type

        :param custody_type: The custody_type of this DepotPosition.
        :type: str
        """

        self._custody_type = custody_type

    @property
    def quantity(self):
        """Gets the quantity of this DepotPosition.

        Quantity or nominal amount in case of a percentage quotation

        :return: The quantity of this DepotPosition.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this DepotPosition.

        Quantity or nominal amount in case of a percentage quotation

        :param quantity: The quantity of this DepotPosition.
        :type: AmountValue
        """

        self._quantity = quantity

    @property
    def available_quantity(self):
        """Gets the available_quantity of this DepotPosition.

        Available quantity or nominal amount in case of a percentage quotation

        :return: The available_quantity of this DepotPosition.
        :rtype: AmountValue
        """
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        """Sets the available_quantity of this DepotPosition.

        Available quantity or nominal amount in case of a percentage quotation

        :param available_quantity: The available_quantity of this DepotPosition.
        :type: AmountValue
        """

        self._available_quantity = available_quantity

    @property
    def current_price(self):
        """Gets the current_price of this DepotPosition.

        Current price, if available

        :return: The current_price of this DepotPosition.
        :rtype: Price
        """
        return self._current_price

    @current_price.setter
    def current_price(self, current_price):
        """Sets the current_price of this DepotPosition.

        Current price, if available

        :param current_price: The current_price of this DepotPosition.
        :type: Price
        """

        self._current_price = current_price

    @property
    def purchase_price(self):
        """Gets the purchase_price of this DepotPosition.

        Purchase price, if available

        :return: The purchase_price of this DepotPosition.
        :rtype: AmountValue
        """
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, purchase_price):
        """Sets the purchase_price of this DepotPosition.

        Purchase price, if available

        :param purchase_price: The purchase_price of this DepotPosition.
        :type: AmountValue
        """

        self._purchase_price = purchase_price

    @property
    def prev_day_price(self):
        """Gets the prev_day_price of this DepotPosition.

        Price of the previous day, if available

        :return: The prev_day_price of this DepotPosition.
        :rtype: Price
        """
        return self._prev_day_price

    @prev_day_price.setter
    def prev_day_price(self, prev_day_price):
        """Sets the prev_day_price of this DepotPosition.

        Price of the previous day, if available

        :param prev_day_price: The prev_day_price of this DepotPosition.
        :type: Price
        """

        self._prev_day_price = prev_day_price

    @property
    def current_value(self):
        """Gets the current_value of this DepotPosition.

        Current value of the position

        :return: The current_value of this DepotPosition.
        :rtype: AmountValue
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this DepotPosition.

        Current value of the position

        :param current_value: The current_value of this DepotPosition.
        :type: AmountValue
        """

        self._current_value = current_value

    @property
    def purchase_value(self):
        """Gets the purchase_value of this DepotPosition.

        Average purchase value of the position

        :return: The purchase_value of this DepotPosition.
        :rtype: AmountValue
        """
        return self._purchase_value

    @purchase_value.setter
    def purchase_value(self, purchase_value):
        """Sets the purchase_value of this DepotPosition.

        Average purchase value of the position

        :param purchase_value: The purchase_value of this DepotPosition.
        :type: AmountValue
        """

        self._purchase_value = purchase_value

    @property
    def prev_day_value(self):
        """Gets the prev_day_value of this DepotPosition.

        Position value at previous day's closing price

        :return: The prev_day_value of this DepotPosition.
        :rtype: AmountValue
        """
        return self._prev_day_value

    @prev_day_value.setter
    def prev_day_value(self, prev_day_value):
        """Sets the prev_day_value of this DepotPosition.

        Position value at previous day's closing price

        :param prev_day_value: The prev_day_value of this DepotPosition.
        :type: AmountValue
        """

        self._prev_day_value = prev_day_value

    @property
    def profit_loss_purchase_abs(self):
        """Gets the profit_loss_purchase_abs of this DepotPosition.

        Absolute profit/loss at purchase price, if available

        :return: The profit_loss_purchase_abs of this DepotPosition.
        :rtype: AmountValue
        """
        return self._profit_loss_purchase_abs

    @profit_loss_purchase_abs.setter
    def profit_loss_purchase_abs(self, profit_loss_purchase_abs):
        """Sets the profit_loss_purchase_abs of this DepotPosition.

        Absolute profit/loss at purchase price, if available

        :param profit_loss_purchase_abs: The profit_loss_purchase_abs of this DepotPosition.
        :type: AmountValue
        """

        self._profit_loss_purchase_abs = profit_loss_purchase_abs

    @property
    def profit_loss_purchase_rel(self):
        """Gets the profit_loss_purchase_rel of this DepotPosition.

        Profit/loss relative to purchase value in percentage, if available

        :return: The profit_loss_purchase_rel of this DepotPosition.
        :rtype: PercentageString
        """
        return self._profit_loss_purchase_rel

    @profit_loss_purchase_rel.setter
    def profit_loss_purchase_rel(self, profit_loss_purchase_rel):
        """Sets the profit_loss_purchase_rel of this DepotPosition.

        Profit/loss relative to purchase value in percentage, if available

        :param profit_loss_purchase_rel: The profit_loss_purchase_rel of this DepotPosition.
        :type: PercentageString
        """

        self._profit_loss_purchase_rel = profit_loss_purchase_rel

    @property
    def profit_loss_prev_day_abs(self):
        """Gets the profit_loss_prev_day_abs of this DepotPosition.

        Absolute profit/loss compared to previous day, if available

        :return: The profit_loss_prev_day_abs of this DepotPosition.
        :rtype: AmountValue
        """
        return self._profit_loss_prev_day_abs

    @profit_loss_prev_day_abs.setter
    def profit_loss_prev_day_abs(self, profit_loss_prev_day_abs):
        """Sets the profit_loss_prev_day_abs of this DepotPosition.

        Absolute profit/loss compared to previous day, if available

        :param profit_loss_prev_day_abs: The profit_loss_prev_day_abs of this DepotPosition.
        :type: AmountValue
        """

        self._profit_loss_prev_day_abs = profit_loss_prev_day_abs

    @property
    def profit_loss_prev_day_rel(self):
        """Gets the profit_loss_prev_day_rel of this DepotPosition.

        Profit/Loss compared to previous day in percentage, if available

        :return: The profit_loss_prev_day_rel of this DepotPosition.
        :rtype: PercentageString
        """
        return self._profit_loss_prev_day_rel

    @profit_loss_prev_day_rel.setter
    def profit_loss_prev_day_rel(self, profit_loss_prev_day_rel):
        """Sets the profit_loss_prev_day_rel of this DepotPosition.

        Profit/Loss compared to previous day in percentage, if available

        :param profit_loss_prev_day_rel: The profit_loss_prev_day_rel of this DepotPosition.
        :type: PercentageString
        """

        self._profit_loss_prev_day_rel = profit_loss_prev_day_rel

    @property
    def instrument(self):
        """Gets the instrument of this DepotPosition.

        Information about the instrument of the securities position

        :return: The instrument of this DepotPosition.
        :rtype: Instrument
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this DepotPosition.

        Information about the instrument of the securities position

        :param instrument: The instrument of this DepotPosition.
        :type: Instrument
        """

        self._instrument = instrument

    @property
    def version(self):
        """Gets the version of this DepotPosition.

        Position version, if available

        :return: The version of this DepotPosition.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DepotPosition.

        Position version, if available

        :param version: The version of this DepotPosition.
        :type: str
        """

        self._version = version

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
        if issubclass(DepotPosition, dict):
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
        if not isinstance(other, DepotPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepotPosition):
            return True

        return self.to_dict() != other.to_dict()
