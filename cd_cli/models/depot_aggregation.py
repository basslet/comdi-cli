import pprint


class DepotAggregation(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot": "Depot",
        "depot_id": "str",
        "date_last_update": "str",
        "current_value": "AmountValue",
        "purchase_value": "AmountValue",
        "prev_day_value": "AmountValue",
        "lending_value": "AmountValue",
        "profit_loss_purchase_abs": "AmountValue",
        "profit_loss_purchase_rel": "PercentageString",
        "profit_loss_prev_day_abs": "AmountValue",
        "profit_loss_prev_day_rel": "PercentageString",
    }

    attribute_map = {
        "depot": "depot",
        "depot_id": "depotId",
        "date_last_update": "dateLastUpdate",
        "current_value": "currentValue",
        "purchase_value": "purchaseValue",
        "prev_day_value": "prevDayValue",
        "lending_value": "lendingValue",
        "profit_loss_purchase_abs": "profitLossPurchaseAbs",
        "profit_loss_purchase_rel": "profitLossPurchaseRel",
        "profit_loss_prev_day_abs": "profitLossPrevDayAbs",
        "profit_loss_prev_day_rel": "profitLossPrevDayRel",
    }

    def __init__(
        self,
        depot=None,
        depot_id=None,
        date_last_update=None,
        current_value=None,
        purchase_value=None,
        prev_day_value=None,
        lending_value=None,
        profit_loss_purchase_abs=None,
        profit_loss_purchase_rel=None,
        profit_loss_prev_day_abs=None,
        profit_loss_prev_day_rel=None,
    ):
        """DepotAggregation"""

        self._depot = None
        self._depot_id = None
        self._date_last_update = None
        self._current_value = None
        self._purchase_value = None
        self._prev_day_value = None
        self._lending_value = None
        self._profit_loss_purchase_abs = None
        self._profit_loss_purchase_rel = None
        self._profit_loss_prev_day_abs = None
        self._profit_loss_prev_day_rel = None

        if depot is not None:
            self.depot = depot
        if depot_id is not None:
            self.depot_id = depot_id
        if date_last_update is not None:
            self.date_last_update = date_last_update
        if current_value is not None:
            self.current_value = current_value
        if purchase_value is not None:
            self.purchase_value = purchase_value
        if prev_day_value is not None:
            self.prev_day_value = prev_day_value
        if lending_value is not None:
            self.lending_value = lending_value
        if profit_loss_purchase_abs is not None:
            self.profit_loss_purchase_abs = profit_loss_purchase_abs
        if profit_loss_purchase_rel is not None:
            self.profit_loss_purchase_rel = profit_loss_purchase_rel
        if profit_loss_prev_day_abs is not None:
            self.profit_loss_prev_day_abs = profit_loss_prev_day_abs
        if profit_loss_prev_day_rel is not None:
            self.profit_loss_prev_day_rel = profit_loss_prev_day_rel

    @property
    def depot(self):
        """Gets the depot of this DepotAggregation.

        The master data of this securities account (this attribute can be suppressed by using the parameter 'without-attr=depot')

        :return: The depot of this DepotAggregation.
        :rtype: Depot
        """
        return self._depot

    @depot.setter
    def depot(self, depot):
        """Sets the depot of this DepotAggregation.

        The master data of this securities account (this attribute can be suppressed by using the parameter 'without-attr=depot')

        :param depot: The depot of this DepotAggregation.
        :type: Depot
        """

        self._depot = depot

    @property
    def depot_id(self):
        """Gets the depot_id of this DepotAggregation.

        Securities account Identifier (UUID)

        :return: The depot_id of this DepotAggregation.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this DepotAggregation.

        Securities account Identifier (UUID)

        :param depot_id: The depot_id of this DepotAggregation.
        :type: str
        """

        self._depot_id = depot_id

    @property
    def date_last_update(self):
        """Gets the date_last_update of this DepotAggregation.

        Date of the last update of securities holdings & master data. YYYY-MM-DD

        :return: The date_last_update of this DepotAggregation.
        :rtype: str
        """
        return self._date_last_update

    @date_last_update.setter
    def date_last_update(self, date_last_update):
        """Sets the date_last_update of this DepotAggregation.

        Date of the last update of securities holdings & master data. YYYY-MM-DD

        :param date_last_update: The date_last_update of this DepotAggregation.
        :type: str
        """

        self._date_last_update = date_last_update

    @property
    def current_value(self):
        """Gets the current_value of this DepotAggregation.

        Current value of the securities account (the sum of all the securities holdings at their current prices)

        :return: The current_value of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this DepotAggregation.

        Current value of the securities account (the sum of all the securities holdings at their current prices)

        :param current_value: The current_value of this DepotAggregation.
        :type: AmountValue
        """

        self._current_value = current_value

    @property
    def purchase_value(self):
        """Gets the purchase_value of this DepotAggregation.

        Sum of the purchase values of all the securities holdings

        :return: The purchase_value of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._purchase_value

    @purchase_value.setter
    def purchase_value(self, purchase_value):
        """Sets the purchase_value of this DepotAggregation.

        Sum of the purchase values of all the securities holdings

        :param purchase_value: The purchase_value of this DepotAggregation.
        :type: AmountValue
        """

        self._purchase_value = purchase_value

    @property
    def prev_day_value(self):
        """Gets the prev_day_value of this DepotAggregation.

        Value of the securities account (the sum of all the securities holdings at the closing prices of the previous day)

        :return: The prev_day_value of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._prev_day_value

    @prev_day_value.setter
    def prev_day_value(self, prev_day_value):
        """Sets the prev_day_value of this DepotAggregation.

        Value of the securities account (the sum of all the securities holdings at the closing prices of the previous day)

        :param prev_day_value: The prev_day_value of this DepotAggregation.
        :type: AmountValue
        """

        self._prev_day_value = prev_day_value

    @property
    def lending_value(self):
        """Gets the lending_value of this DepotAggregation.

        Sum of the lending values of all of the securities holdings

        :return: The lending_value of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._lending_value

    @lending_value.setter
    def lending_value(self, lending_value):
        """Sets the lending_value of this DepotAggregation.

        Sum of the lending values of all of the securities holdings

        :param lending_value: The lending_value of this DepotAggregation.
        :type: AmountValue
        """

        self._lending_value = lending_value

    @property
    def profit_loss_purchase_abs(self):
        """Gets the profit_loss_purchase_abs of this DepotAggregation.

        Profit/loss at the absolute purchase value

        :return: The profit_loss_purchase_abs of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._profit_loss_purchase_abs

    @profit_loss_purchase_abs.setter
    def profit_loss_purchase_abs(self, profit_loss_purchase_abs):
        """Sets the profit_loss_purchase_abs of this DepotAggregation.

        Profit/loss at the absolute purchase value

        :param profit_loss_purchase_abs: The profit_loss_purchase_abs of this DepotAggregation.
        :type: AmountValue
        """

        self._profit_loss_purchase_abs = profit_loss_purchase_abs

    @property
    def profit_loss_purchase_rel(self):
        """Gets the profit_loss_purchase_rel of this DepotAggregation.

        Profit/loss relative to purchase value in percentage

        :return: The profit_loss_purchase_rel of this DepotAggregation.
        :rtype: PercentageString
        """
        return self._profit_loss_purchase_rel

    @profit_loss_purchase_rel.setter
    def profit_loss_purchase_rel(self, profit_loss_purchase_rel):
        """Sets the profit_loss_purchase_rel of this DepotAggregation.

        Profit/loss relative to purchase value in percentage

        :param profit_loss_purchase_rel: The profit_loss_purchase_rel of this DepotAggregation.
        :type: PercentageString
        """

        self._profit_loss_purchase_rel = profit_loss_purchase_rel

    @property
    def profit_loss_prev_day_abs(self):
        """Gets the profit_loss_prev_day_abs of this DepotAggregation.

        Absolute profit/loss compared to the previous day

        :return: The profit_loss_prev_day_abs of this DepotAggregation.
        :rtype: AmountValue
        """
        return self._profit_loss_prev_day_abs

    @profit_loss_prev_day_abs.setter
    def profit_loss_prev_day_abs(self, profit_loss_prev_day_abs):
        """Sets the profit_loss_prev_day_abs of this DepotAggregation.

        Absolute profit/loss compared to the previous day

        :param profit_loss_prev_day_abs: The profit_loss_prev_day_abs of this DepotAggregation.
        :type: AmountValue
        """

        self._profit_loss_prev_day_abs = profit_loss_prev_day_abs

    @property
    def profit_loss_prev_day_rel(self):
        """Gets the profit_loss_prev_day_rel of this DepotAggregation.

        Profit/Loss compared to the previous day in percentage

        :return: The profit_loss_prev_day_rel of this DepotAggregation.
        :rtype: PercentageString
        """
        return self._profit_loss_prev_day_rel

    @profit_loss_prev_day_rel.setter
    def profit_loss_prev_day_rel(self, profit_loss_prev_day_rel):
        """Sets the profit_loss_prev_day_rel of this DepotAggregation.

        Profit/Loss compared to the previous day in percentage

        :param profit_loss_prev_day_rel: The profit_loss_prev_day_rel of this DepotAggregation.
        :type: PercentageString
        """

        self._profit_loss_prev_day_rel = profit_loss_prev_day_rel

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
        if issubclass(DepotAggregation, dict):
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
        if not isinstance(other, DepotAggregation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepotAggregation):
            return True

        return self.to_dict() != other.to_dict()
