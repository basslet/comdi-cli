import pprint


class Order(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot_id": "str",
        "settlement_account_id": "str",
        "order_id": "str",
        "creation_timestamp": "TimestampString",
        "leg_number": "int",
        "best_ex": "bool",
        "order_type": "str",
        "order_status": "str",
        "sub_orders": "list[Order]",
        "side": "str",
        "instrument_id": "str",
        "quote_id": "str",
        "venue_id": "str",
        "quantity": "AmountValue",
        "open_quantity": "AmountValue",
        "cancelled_quantity": "AmountValue",
        "executed_quantity": "AmountValue",
        "limit_extension": "str",
        "trading_restriction": "str",
        "limit": "AmountValue",
        "trigger_limit": "AmountValue",
        "trailing_limit_dist_abs": "AmountValue",
        "trailing_limit_dist_rel": "PercentageString",
        "validity_type": "str",
        "validity": "DateString",
        "expected_value": "AmountValue",
        "executions": "list[Execution]",
        "quote_ticket_id": "str",
        "version": "str",
    }

    attribute_map = {
        "depot_id": "depotId",
        "settlement_account_id": "settlementAccountId",
        "order_id": "orderId",
        "creation_timestamp": "creationTimestamp",
        "leg_number": "legNumber",
        "best_ex": "bestEx",
        "order_type": "orderType",
        "order_status": "orderStatus",
        "sub_orders": "subOrders",
        "side": "side",
        "instrument_id": "instrumentId",
        "quote_id": "quoteId",
        "venue_id": "venueId",
        "quantity": "quantity",
        "open_quantity": "openQuantity",
        "cancelled_quantity": "cancelledQuantity",
        "executed_quantity": "executedQuantity",
        "limit_extension": "limitExtension",
        "trading_restriction": "tradingRestriction",
        "limit": "limit",
        "trigger_limit": "triggerLimit",
        "trailing_limit_dist_abs": "trailingLimitDistAbs",
        "trailing_limit_dist_rel": "trailingLimitDistRel",
        "validity_type": "validityType",
        "validity": "validity",
        "expected_value": "expectedValue",
        "executions": "executions",
        "quote_ticket_id": "quoteTicketId",
        "version": "version",
    }

    def __init__(
        self,
        depot_id=None,
        settlement_account_id=None,
        order_id=None,
        creation_timestamp=None,
        leg_number=None,
        best_ex=False,
        order_type=None,
        order_status=None,
        sub_orders=None,
        side=None,
        instrument_id=None,
        quote_id=None,
        venue_id=None,
        quantity=None,
        open_quantity=None,
        cancelled_quantity=None,
        executed_quantity=None,
        limit_extension=None,
        trading_restriction=None,
        limit=None,
        trigger_limit=None,
        trailing_limit_dist_abs=None,
        trailing_limit_dist_rel=None,
        validity_type=None,
        validity=None,
        expected_value=None,
        executions=None,
        quote_ticket_id=None,
        version=None,
    ):
        """Order"""

        self._depot_id = None
        self._settlement_account_id = None
        self._order_id = None
        self._creation_timestamp = None
        self._leg_number = None
        self._best_ex = None
        self._order_type = None
        self._order_status = None
        self._sub_orders = None
        self._side = None
        self._instrument_id = None
        self._quote_id = None
        self._venue_id = None
        self._quantity = None
        self._open_quantity = None
        self._cancelled_quantity = None
        self._executed_quantity = None
        self._limit_extension = None
        self._trading_restriction = None
        self._limit = None
        self._trigger_limit = None
        self._trailing_limit_dist_abs = None
        self._trailing_limit_dist_rel = None
        self._validity_type = None
        self._validity = None
        self._expected_value = None
        self._executions = None
        self._quote_ticket_id = None
        self._version = None

        if depot_id is not None:
            self.depot_id = depot_id
        if settlement_account_id is not None:
            self.settlement_account_id = settlement_account_id
        if order_id is not None:
            self.order_id = order_id
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if leg_number is not None:
            self.leg_number = leg_number
        if best_ex is not None:
            self.best_ex = best_ex
        if order_type is not None:
            self.order_type = order_type
        if order_status is not None:
            self.order_status = order_status
        if sub_orders is not None:
            self.sub_orders = sub_orders
        if side is not None:
            self.side = side
        if instrument_id is not None:
            self.instrument_id = instrument_id
        if quote_id is not None:
            self.quote_id = quote_id
        if venue_id is not None:
            self.venue_id = venue_id
        if quantity is not None:
            self.quantity = quantity
        if open_quantity is not None:
            self.open_quantity = open_quantity
        if cancelled_quantity is not None:
            self.cancelled_quantity = cancelled_quantity
        if executed_quantity is not None:
            self.executed_quantity = executed_quantity
        if limit_extension is not None:
            self.limit_extension = limit_extension
        if trading_restriction is not None:
            self.trading_restriction = trading_restriction
        if limit is not None:
            self.limit = limit
        if trigger_limit is not None:
            self.trigger_limit = trigger_limit
        if trailing_limit_dist_abs is not None:
            self.trailing_limit_dist_abs = trailing_limit_dist_abs
        if trailing_limit_dist_rel is not None:
            self.trailing_limit_dist_rel = trailing_limit_dist_rel
        if validity_type is not None:
            self.validity_type = validity_type
        if validity is not None:
            self.validity = validity
        if expected_value is not None:
            self.expected_value = expected_value
        if executions is not None:
            self.executions = executions
        if quote_ticket_id is not None:
            self.quote_ticket_id = quote_ticket_id
        if version is not None:
            self.version = version

    @property
    def depot_id(self):
        """Gets the depot_id of this Order.

        Unique securities account identification (as UUID)

        :return: The depot_id of this Order.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this Order.

        Unique securities account identification (as UUID)

        :param depot_id: The depot_id of this Order.
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
    def settlement_account_id(self):
        """Gets the settlement_account_id of this Order.

        Reference settlement account for the securities account, if different from the settlement account assigned directly to the securities account (UUID)

        :return: The settlement_account_id of this Order.
        :rtype: str
        """
        return self._settlement_account_id

    @settlement_account_id.setter
    def settlement_account_id(self, settlement_account_id):
        """Sets the settlement_account_id of this Order.

        Reference settlement account for the securities account, if different from the settlement account assigned directly to the securities account (UUID)

        :param settlement_account_id: The settlement_account_id of this Order.
        :type: str
        """
        if settlement_account_id is not None and len(settlement_account_id) > 40:
            raise ValueError(
                "Invalid value for `settlement_account_id`, length must be less than or equal to `40`"
            )
        if settlement_account_id is not None and len(settlement_account_id) < 0:
            raise ValueError(
                "Invalid value for `settlement_account_id`, length must be greater than or equal to `0`"
            )

        self._settlement_account_id = settlement_account_id

    @property
    def order_id(self):
        """Gets the order_id of this Order.

        Unique order-Id (UUID)

        :return: The order_id of this Order.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        Unique order-Id (UUID)

        :param order_id: The order_id of this Order.
        :type: str
        """
        if order_id is not None and len(order_id) > 40:
            raise ValueError(
                "Invalid value for `order_id`, length must be less than or equal to `40`"
            )
        if order_id is not None and len(order_id) < 0:
            raise ValueError(
                "Invalid value for `order_id`, length must be greater than or equal to `0`"
            )

        self._order_id = order_id

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Order.

        Date/timestamp of the order entry in UTC with the following format: YYYY-MM-DDThh:mm:ss,ffffff+zz

        :return: The creation_timestamp of this Order.
        :rtype: TimestampString
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Order.

        Date/timestamp of the order entry in UTC with the following format: YYYY-MM-DDThh:mm:ss,ffffff+zz

        :param creation_timestamp: The creation_timestamp of this Order.
        :type: TimestampString
        """

        self._creation_timestamp = creation_timestamp

    @property
    def leg_number(self):
        """Gets the leg_number of this Order.

        Order leg number (if ordertype is OCO or NEO)

        :return: The leg_number of this Order.
        :rtype: int
        """
        return self._leg_number

    @leg_number.setter
    def leg_number(self, leg_number):
        """Sets the leg_number of this Order.

        Order leg number (if ordertype is OCO or NEO)

        :param leg_number: The leg_number of this Order.
        :type: int
        """

        self._leg_number = leg_number

    @property
    def best_ex(self):
        """Gets the best_ex of this Order.

        Flag if order is a best-execution-order, default value is false

        :return: The best_ex of this Order.
        :rtype: bool
        """
        return self._best_ex

    @best_ex.setter
    def best_ex(self, best_ex):
        """Sets the best_ex of this Order.

        Flag if order is a best-execution-order, default value is false

        :param best_ex: The best_ex of this Order.
        :type: bool
        """

        self._best_ex = best_ex

    @property
    def order_type(self):
        """Gets the order_type of this Order.

        Ordertype, partially executed and open orders are listed in the execution parameters

        :return: The order_type of this Order.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this Order.

        Ordertype, partially executed and open orders are listed in the execution parameters

        :param order_type: The order_type of this Order.
        :type: str
        """
        allowed_values = [
            "MARKET",
            "LIMIT",
            "QUOTE",
            "STOP_MARKET",
            "STOP_LIMIT",
            "TRAILING_STOP_MARKET",
            "TRAILING_STOP_LIMIT",
            "ONE_CANCELS_OTHER",
            "NEXT_ORDER",
        ]
        if order_type not in allowed_values:
            raise ValueError(
                "Invalid value for `order_type` ({0}), must be one of {1}".format(
                    order_type, allowed_values
                )
            )

        self._order_type = order_type

    @property
    def order_status(self):
        """Gets the order_status of this Order.

        Status of the order

        :return: The order_status of this Order.
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this Order.

        Status of the order

        :param order_status: The order_status of this Order.
        :type: str
        """
        allowed_values = [
            "PENDING",
            "OPEN",
            "EXECUTED",
            "SETTLED",
            "CANCELLED_USER",
            "EXPIRED",
            "CANCELLED_SYSTEM",
            "CANCELLED_TRADE",
            "UNKNOWN",
        ]
        if order_status not in allowed_values:
            raise ValueError(
                "Invalid value for `order_status` ({0}), must be one of {1}".format(
                    order_status, allowed_values
                )
            )

        self._order_status = order_status

    @property
    def sub_orders(self):
        """Gets the sub_orders of this Order.

        Parts of the orders, e.g. combination orders OCO, NEO (Next Order) with different order legs or partially executed or partially cancelled orders with different parts of an order

        :return: The sub_orders of this Order.
        :rtype: list[Order]
        """
        return self._sub_orders

    @sub_orders.setter
    def sub_orders(self, sub_orders):
        """Sets the sub_orders of this Order.

        Parts of the orders, e.g. combination orders OCO, NEO (Next Order) with different order legs or partially executed or partially cancelled orders with different parts of an order

        :param sub_orders: The sub_orders of this Order.
        :type: list[Order]
        """

        self._sub_orders = sub_orders

    @property
    def side(self):
        """Gets the side of this Order.

        Type of transaction

        :return: The side of this Order.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Order.

        Type of transaction

        :param side: The side of this Order.
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
        """Gets the instrument_id of this Order.

        WKN, ISIN or uuId; wkn will be returned if instrumentId is entered as wkn, an ISIN is returned if instrumentId is entered as ISIN, a uuId is returned if instrumentId is entered as uuId

        :return: The instrument_id of this Order.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this Order.

        WKN, ISIN or uuId; wkn will be returned if instrumentId is entered as wkn, an ISIN is returned if instrumentId is entered as ISIN, a uuId is returned if instrumentId is entered as uuId

        :param instrument_id: The instrument_id of this Order.
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
    def quote_id(self):
        """Gets the quote_id of this Order.

        Quote-Id as reference for the quote received from the trading venue (issuer or exchange) on the quote request

        :return: The quote_id of this Order.
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this Order.

        Quote-Id as reference for the quote received from the trading venue (issuer or exchange) on the quote request

        :param quote_id: The quote_id of this Order.
        :type: str
        """
        if quote_id is not None and len(quote_id) > 40:
            raise ValueError(
                "Invalid value for `quote_id`, length must be less than or equal to `40`"
            )
        if quote_id is not None and len(quote_id) < 0:
            raise ValueError(
                "Invalid value for `quote_id`, length must be greater than or equal to `0`"
            )

        self._quote_id = quote_id

    @property
    def venue_id(self):
        """Gets the venue_id of this Order.

        UUID of the trading venue or partner. This is mandatory, if isBestEx=FALSE

        :return: The venue_id of this Order.
        :rtype: str
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this Order.

        UUID of the trading venue or partner. This is mandatory, if isBestEx=FALSE

        :param venue_id: The venue_id of this Order.
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
        """Gets the quantity of this Order.

        Quantity or nominal amount in the case of a percentage quotation

        :return: The quantity of this Order.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.

        Quantity or nominal amount in the case of a percentage quotation

        :param quantity: The quantity of this Order.
        :type: AmountValue
        """

        self._quantity = quantity

    @property
    def open_quantity(self):
        """Gets the open_quantity of this Order.

        Open quantity or nominal amount

        :return: The open_quantity of this Order.
        :rtype: AmountValue
        """
        return self._open_quantity

    @open_quantity.setter
    def open_quantity(self, open_quantity):
        """Sets the open_quantity of this Order.

        Open quantity or nominal amount

        :param open_quantity: The open_quantity of this Order.
        :type: AmountValue
        """

        self._open_quantity = open_quantity

    @property
    def cancelled_quantity(self):
        """Gets the cancelled_quantity of this Order.

        Canceled quantity or nominal amount

        :return: The cancelled_quantity of this Order.
        :rtype: AmountValue
        """
        return self._cancelled_quantity

    @cancelled_quantity.setter
    def cancelled_quantity(self, cancelled_quantity):
        """Sets the cancelled_quantity of this Order.

        Canceled quantity or nominal amount

        :param cancelled_quantity: The cancelled_quantity of this Order.
        :type: AmountValue
        """

        self._cancelled_quantity = cancelled_quantity

    @property
    def executed_quantity(self):
        """Gets the executed_quantity of this Order.

        Canceled quantity or nominal amount

        :return: The executed_quantity of this Order.
        :rtype: AmountValue
        """
        return self._executed_quantity

    @executed_quantity.setter
    def executed_quantity(self, executed_quantity):
        """Sets the executed_quantity of this Order.

        Canceled quantity or nominal amount

        :param executed_quantity: The executed_quantity of this Order.
        :type: AmountValue
        """

        self._executed_quantity = executed_quantity

    @property
    def limit_extension(self):
        """Gets the limit_extension of this Order.

        Order extensions (Fill-or-Kill, Immediate-or-Cancel, All-or-None)

        :return: The limit_extension of this Order.
        :rtype: str
        """
        return self._limit_extension

    @limit_extension.setter
    def limit_extension(self, limit_extension):
        """Sets the limit_extension of this Order.

        Order extensions (Fill-or-Kill, Immediate-or-Cancel, All-or-None)

        :param limit_extension: The limit_extension of this Order.
        :type: str
        """
        allowed_values = ["FOK", "IOC", "AON"]
        if limit_extension not in allowed_values:
            raise ValueError(
                "Invalid value for `limit_extension` ({0}), must be one of {1}".format(
                    limit_extension, allowed_values
                )
            )

        self._limit_extension = limit_extension

    @property
    def trading_restriction(self):
        """Gets the trading_restriction of this Order.

        Restrictions on trade (Opening Auction Only, Auction Only, Closing Auction Only)

        :return: The trading_restriction of this Order.
        :rtype: str
        """
        return self._trading_restriction

    @trading_restriction.setter
    def trading_restriction(self, trading_restriction):
        """Sets the trading_restriction of this Order.

        Restrictions on trade (Opening Auction Only, Auction Only, Closing Auction Only)

        :param trading_restriction: The trading_restriction of this Order.
        :type: str
        """
        allowed_values = ["OAO", "AO", "CAO"]
        if trading_restriction not in allowed_values:
            raise ValueError(
                "Invalid value for `trading_restriction` ({0}), must be one of {1}".format(
                    trading_restriction, allowed_values
                )
            )

        self._trading_restriction = trading_restriction

    @property
    def limit(self):
        """Gets the limit of this Order.

        Limit of the order, empty in case of a market order, stop market, trailing stop market order or a corresponding suborder

        :return: The limit of this Order.
        :rtype: AmountValue
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Order.

        Limit of the order, empty in case of a market order, stop market, trailing stop market order or a corresponding suborder

        :param limit: The limit of this Order.
        :type: AmountValue
        """

        self._limit = limit

    @property
    def trigger_limit(self):
        """Gets the trigger_limit of this Order.

        Trigger limit: stop limit by which a Stop order is triggered (Stop, TLS, OCO)

        :return: The trigger_limit of this Order.
        :rtype: AmountValue
        """
        return self._trigger_limit

    @trigger_limit.setter
    def trigger_limit(self, trigger_limit):
        """Sets the trigger_limit of this Order.

        Trigger limit: stop limit by which a Stop order is triggered (Stop, TLS, OCO)

        :param trigger_limit: The trigger_limit of this Order.
        :type: AmountValue
        """

        self._trigger_limit = trigger_limit

    @property
    def trailing_limit_dist_abs(self):
        """Gets the trailing_limit_dist_abs of this Order.

        Distance trigger limit of the trailing stop order from the current absolute price

        :return: The trailing_limit_dist_abs of this Order.
        :rtype: AmountValue
        """
        return self._trailing_limit_dist_abs

    @trailing_limit_dist_abs.setter
    def trailing_limit_dist_abs(self, trailing_limit_dist_abs):
        """Sets the trailing_limit_dist_abs of this Order.

        Distance trigger limit of the trailing stop order from the current absolute price

        :param trailing_limit_dist_abs: The trailing_limit_dist_abs of this Order.
        :type: AmountValue
        """

        self._trailing_limit_dist_abs = trailing_limit_dist_abs

    @property
    def trailing_limit_dist_rel(self):
        """Gets the trailing_limit_dist_rel of this Order.

        Distance trigger limit of the trailing stop order from the current price in percentage

        :return: The trailing_limit_dist_rel of this Order.
        :rtype: PercentageString
        """
        return self._trailing_limit_dist_rel

    @trailing_limit_dist_rel.setter
    def trailing_limit_dist_rel(self, trailing_limit_dist_rel):
        """Sets the trailing_limit_dist_rel of this Order.

        Distance trigger limit of the trailing stop order from the current price in percentage

        :param trailing_limit_dist_rel: The trailing_limit_dist_rel of this Order.
        :type: PercentageString
        """

        self._trailing_limit_dist_rel = trailing_limit_dist_rel

    @property
    def validity_type(self):
        """Gets the validity_type of this Order.

        Type of order validity (Good-for-day (default), Good-til-date (incl. end of month))

        :return: The validity_type of this Order.
        :rtype: str
        """
        return self._validity_type

    @validity_type.setter
    def validity_type(self, validity_type):
        """Sets the validity_type of this Order.

        Type of order validity (Good-for-day (default), Good-til-date (incl. end of month))

        :param validity_type: The validity_type of this Order.
        :type: str
        """
        allowed_values = ["GFD", "GTD"]
        if validity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `validity_type` ({0}), must be one of {1}".format(
                    validity_type, allowed_values
                )
            )

        self._validity_type = validity_type

    @property
    def validity(self):
        """Gets the validity of this Order.

        Date of order validity in format YYYY-MM-DD; required for validityType=GTD

        :return: The validity of this Order.
        :rtype: DateString
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this Order.

        Date of order validity in format YYYY-MM-DD; required for validityType=GTD

        :param validity: The validity of this Order.
        :type: DateString
        """

        self._validity = validity

    @property
    def expected_value(self):
        """Gets the expected_value of this Order.

        Expected value of the limit order

        :return: The expected_value of this Order.
        :rtype: AmountValue
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, expected_value):
        """Sets the expected_value of this Order.

        Expected value of the limit order

        :param expected_value: The expected_value of this Order.
        :type: AmountValue
        """

        self._expected_value = expected_value

    @property
    def executions(self):
        """Gets the executions of this Order.

        List of execution types for the order

        :return: The executions of this Order.
        :rtype: list[Execution]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """Sets the executions of this Order.

        List of execution types for the order

        :param executions: The executions of this Order.
        :type: list[Execution]
        """

        self._executions = executions

    @property
    def quote_ticket_id(self):
        """Gets the quote_ticket_id of this Order.

        Ticket UUID for the quote order. This is mandatory, if for a quote order

        :return: The quote_ticket_id of this Order.
        :rtype: str
        """
        return self._quote_ticket_id

    @quote_ticket_id.setter
    def quote_ticket_id(self, quote_ticket_id):
        """Sets the quote_ticket_id of this Order.

        Ticket UUID for the quote order. This is mandatory, if for a quote order

        :param quote_ticket_id: The quote_ticket_id of this Order.
        :type: str
        """
        if quote_ticket_id is not None and len(quote_ticket_id) > 40:
            raise ValueError(
                "Invalid value for `quote_ticket_id`, length must be less than or equal to `40`"
            )
        if quote_ticket_id is not None and len(quote_ticket_id) < 0:
            raise ValueError(
                "Invalid value for `quote_ticket_id`, length must be greater than or equal to `0`"
            )

        self._quote_ticket_id = quote_ticket_id

    @property
    def version(self):
        """Gets the version of this Order.

        Version of the position to be sold. Only applicable for sell

        :return: The version of this Order.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Order.

        Version of the position to be sold. Only applicable for sell

        :param version: The version of this Order.
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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()
