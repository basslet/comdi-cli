import pprint


class CostIndicationExAnte(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot_id": "str",
        "calculation_successful": "bool",
        "name": "str",
        "wkn": "str",
        "side": "str",
        "quantity": "AmountValue",
        "limit": "AmountValue",
        "expected_value": "AmountValue",
        "venue_name": "str",
        "settlement_currency": "CurrencyString",
        "trading_currency": "CurrencyString",
        "reporting_currency": "CurrencyString",
        "fx_rate": "FXRateEUR",
        "expected_settlement_costs": "AmountValue",
        "purchase_costs": "CostGroup",
        "holding_costs": "CostGroup",
        "sales_costs": "CostGroup",
        "holding_period": "str",
        "total_costs_abs": "AmountValue",
        "total_costs_rel": "PercentageString",
        "total_costs_detail": "TotalCostBlock",
        "total_holding_costs": "TotalHoldingCostBlock",
        "link_costs": "str",
        "link_kid": "str",
    }

    attribute_map = {
        "depot_id": "depotId",
        "calculation_successful": "calculationSuccessful",
        "name": "name",
        "wkn": "wkn",
        "side": "side",
        "quantity": "quantity",
        "limit": "limit",
        "expected_value": "expectedValue",
        "venue_name": "venueName",
        "settlement_currency": "settlementCurrency",
        "trading_currency": "tradingCurrency",
        "reporting_currency": "reportingCurrency",
        "fx_rate": "fxRate",
        "expected_settlement_costs": "expectedSettlementCosts",
        "purchase_costs": "purchaseCosts",
        "holding_costs": "holdingCosts",
        "sales_costs": "salesCosts",
        "holding_period": "holdingPeriod",
        "total_costs_abs": "totalCostsAbs",
        "total_costs_rel": "totalCostsRel",
        "total_costs_detail": "totalCostsDetail",
        "total_holding_costs": "totalHoldingCosts",
        "link_costs": "linkCosts",
        "link_kid": "linkKid",
    }

    def __init__(
        self,
        depot_id=None,
        calculation_successful=False,
        name=None,
        wkn=None,
        side=None,
        quantity=None,
        limit=None,
        expected_value=None,
        venue_name=None,
        settlement_currency=None,
        trading_currency=None,
        reporting_currency=None,
        fx_rate=None,
        expected_settlement_costs=None,
        purchase_costs=None,
        holding_costs=None,
        sales_costs=None,
        holding_period=None,
        total_costs_abs=None,
        total_costs_rel=None,
        total_costs_detail=None,
        total_holding_costs=None,
        link_costs=None,
        link_kid=None,
    ):
        """CostIndicationExAnte"""

        self._depot_id = None
        self._calculation_successful = None
        self._name = None
        self._wkn = None
        self._side = None
        self._quantity = None
        self._limit = None
        self._expected_value = None
        self._venue_name = None
        self._settlement_currency = None
        self._trading_currency = None
        self._reporting_currency = None
        self._fx_rate = None
        self._expected_settlement_costs = None
        self._purchase_costs = None
        self._holding_costs = None
        self._sales_costs = None
        self._holding_period = None
        self._total_costs_abs = None
        self._total_costs_rel = None
        self._total_costs_detail = None
        self._total_holding_costs = None
        self._link_costs = None
        self._link_kid = None

        if depot_id is not None:
            self.depot_id = depot_id
        if calculation_successful is not None:
            self.calculation_successful = calculation_successful
        if name is not None:
            self.name = name
        if wkn is not None:
            self.wkn = wkn
        if side is not None:
            self.side = side
        if quantity is not None:
            self.quantity = quantity
        if limit is not None:
            self.limit = limit
        if expected_value is not None:
            self.expected_value = expected_value
        if venue_name is not None:
            self.venue_name = venue_name
        if settlement_currency is not None:
            self.settlement_currency = settlement_currency
        if trading_currency is not None:
            self.trading_currency = trading_currency
        if reporting_currency is not None:
            self.reporting_currency = reporting_currency
        if fx_rate is not None:
            self.fx_rate = fx_rate
        if expected_settlement_costs is not None:
            self.expected_settlement_costs = expected_settlement_costs
        if purchase_costs is not None:
            self.purchase_costs = purchase_costs
        if holding_costs is not None:
            self.holding_costs = holding_costs
        if sales_costs is not None:
            self.sales_costs = sales_costs
        if holding_period is not None:
            self.holding_period = holding_period
        if total_costs_abs is not None:
            self.total_costs_abs = total_costs_abs
        if total_costs_rel is not None:
            self.total_costs_rel = total_costs_rel
        if total_costs_detail is not None:
            self.total_costs_detail = total_costs_detail
        if total_holding_costs is not None:
            self.total_holding_costs = total_holding_costs
        if link_costs is not None:
            self.link_costs = link_costs
        if link_kid is not None:
            self.link_kid = link_kid

    @property
    def depot_id(self):
        """Gets the depot_id of this CostIndicationExAnte.

        Securities account number (UUID)

        :return: The depot_id of this CostIndicationExAnte.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this CostIndicationExAnte.

        Securities account number (UUID)

        :param depot_id: The depot_id of this CostIndicationExAnte.
        :type: str
        """

        self._depot_id = depot_id

    @property
    def calculation_successful(self):
        """Gets the calculation_successful of this CostIndicationExAnte.

        Result of calculation of cost indication; if false, linkCosts will link to a generic cost indication

        :return: The calculation_successful of this CostIndicationExAnte.
        :rtype: bool
        """
        return self._calculation_successful

    @calculation_successful.setter
    def calculation_successful(self, calculation_successful):
        """Sets the calculation_successful of this CostIndicationExAnte.

        Result of calculation of cost indication; if false, linkCosts will link to a generic cost indication

        :param calculation_successful: The calculation_successful of this CostIndicationExAnte.
        :type: bool
        """

        self._calculation_successful = calculation_successful

    @property
    def name(self):
        """Gets the name of this CostIndicationExAnte.

        Instrument name analogous to Instrument.name

        :return: The name of this CostIndicationExAnte.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CostIndicationExAnte.

        Instrument name analogous to Instrument.name

        :param name: The name of this CostIndicationExAnte.
        :type: str
        """

        self._name = name

    @property
    def wkn(self):
        """Gets the wkn of this CostIndicationExAnte.

        WKN analogous to Instrument.wkn

        :return: The wkn of this CostIndicationExAnte.
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn):
        """Sets the wkn of this CostIndicationExAnte.

        WKN analogous to Instrument.wkn

        :param wkn: The wkn of this CostIndicationExAnte.
        :type: str
        """

        self._wkn = wkn

    @property
    def side(self):
        """Gets the side of this CostIndicationExAnte.

        Type of transaction analogous to Order.side

        :return: The side of this CostIndicationExAnte.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this CostIndicationExAnte.

        Type of transaction analogous to Order.side

        :param side: The side of this CostIndicationExAnte.
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
    def quantity(self):
        """Gets the quantity of this CostIndicationExAnte.

        Quantity analogous to Order.quantity

        :return: The quantity of this CostIndicationExAnte.
        :rtype: AmountValue
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CostIndicationExAnte.

        Quantity analogous to Order.quantity

        :param quantity: The quantity of this CostIndicationExAnte.
        :type: AmountValue
        """

        self._quantity = quantity

    @property
    def limit(self):
        """Gets the limit of this CostIndicationExAnte.

        Limit analogous to Order.limit with trading currency

        :return: The limit of this CostIndicationExAnte.
        :rtype: AmountValue
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CostIndicationExAnte.

        Limit analogous to Order.limit with trading currency

        :param limit: The limit of this CostIndicationExAnte.
        :type: AmountValue
        """

        self._limit = limit

    @property
    def expected_value(self):
        """Gets the expected_value of this CostIndicationExAnte.

        Expected value (net costs) of the order: in trading currency

        :return: The expected_value of this CostIndicationExAnte.
        :rtype: AmountValue
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, expected_value):
        """Sets the expected_value of this CostIndicationExAnte.

        Expected value (net costs) of the order: in trading currency

        :param expected_value: The expected_value of this CostIndicationExAnte.
        :type: AmountValue
        """

        self._expected_value = expected_value

    @property
    def venue_name(self):
        """Gets the venue_name of this CostIndicationExAnte.

        Execution venue as name for the display

        :return: The venue_name of this CostIndicationExAnte.
        :rtype: str
        """
        return self._venue_name

    @venue_name.setter
    def venue_name(self, venue_name):
        """Sets the venue_name of this CostIndicationExAnte.

        Execution venue as name for the display

        :param venue_name: The venue_name of this CostIndicationExAnte.
        :type: str
        """

        self._venue_name = venue_name

    @property
    def settlement_currency(self):
        """Gets the settlement_currency of this CostIndicationExAnte.

        Settlement currency analogous to Account.currency

        :return: The settlement_currency of this CostIndicationExAnte.
        :rtype: CurrencyString
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """Sets the settlement_currency of this CostIndicationExAnte.

        Settlement currency analogous to Account.currency

        :param settlement_currency: The settlement_currency of this CostIndicationExAnte.
        :type: CurrencyString
        """

        self._settlement_currency = settlement_currency

    @property
    def trading_currency(self):
        """Gets the trading_currency of this CostIndicationExAnte.

        Trading currency

        :return: The trading_currency of this CostIndicationExAnte.
        :rtype: CurrencyString
        """
        return self._trading_currency

    @trading_currency.setter
    def trading_currency(self, trading_currency):
        """Sets the trading_currency of this CostIndicationExAnte.

        Trading currency

        :param trading_currency: The trading_currency of this CostIndicationExAnte.
        :type: CurrencyString
        """

        self._trading_currency = trading_currency

    @property
    def reporting_currency(self):
        """Gets the reporting_currency of this CostIndicationExAnte.

        Reporting currency

        :return: The reporting_currency of this CostIndicationExAnte.
        :rtype: CurrencyString
        """
        return self._reporting_currency

    @reporting_currency.setter
    def reporting_currency(self, reporting_currency):
        """Sets the reporting_currency of this CostIndicationExAnte.

        Reporting currency

        :param reporting_currency: The reporting_currency of this CostIndicationExAnte.
        :type: CurrencyString
        """

        self._reporting_currency = reporting_currency

    @property
    def fx_rate(self):
        """Gets the fx_rate of this CostIndicationExAnte.

        Exchange rate for settlement currency to FX, for buy and sell (both sides for conversion depending on BUY/SELL)

        :return: The fx_rate of this CostIndicationExAnte.
        :rtype: FXRateEUR
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """Sets the fx_rate of this CostIndicationExAnte.

        Exchange rate for settlement currency to FX, for buy and sell (both sides for conversion depending on BUY/SELL)

        :param fx_rate: The fx_rate of this CostIndicationExAnte.
        :type: FXRateEUR
        """

        self._fx_rate = fx_rate

    @property
    def expected_settlement_costs(self):
        """Gets the expected_settlement_costs of this CostIndicationExAnte.

        Expected costs for order analogue (real) settlement costs

        :return: The expected_settlement_costs of this CostIndicationExAnte.
        :rtype: AmountValue
        """
        return self._expected_settlement_costs

    @expected_settlement_costs.setter
    def expected_settlement_costs(self, expected_settlement_costs):
        """Sets the expected_settlement_costs of this CostIndicationExAnte.

        Expected costs for order analogue (real) settlement costs

        :param expected_settlement_costs: The expected_settlement_costs of this CostIndicationExAnte.
        :type: AmountValue
        """

        self._expected_settlement_costs = expected_settlement_costs

    @property
    def purchase_costs(self):
        """Gets the purchase_costs of this CostIndicationExAnte.

        CostGroup type K

        :return: The purchase_costs of this CostIndicationExAnte.
        :rtype: CostGroup
        """
        return self._purchase_costs

    @purchase_costs.setter
    def purchase_costs(self, purchase_costs):
        """Sets the purchase_costs of this CostIndicationExAnte.

        CostGroup type K

        :param purchase_costs: The purchase_costs of this CostIndicationExAnte.
        :type: CostGroup
        """

        self._purchase_costs = purchase_costs

    @property
    def holding_costs(self):
        """Gets the holding_costs of this CostIndicationExAnte.

        CostGroup type H

        :return: The holding_costs of this CostIndicationExAnte.
        :rtype: CostGroup
        """
        return self._holding_costs

    @holding_costs.setter
    def holding_costs(self, holding_costs):
        """Sets the holding_costs of this CostIndicationExAnte.

        CostGroup type H

        :param holding_costs: The holding_costs of this CostIndicationExAnte.
        :type: CostGroup
        """

        self._holding_costs = holding_costs

    @property
    def sales_costs(self):
        """Gets the sales_costs of this CostIndicationExAnte.

        CostGroup type V

        :return: The sales_costs of this CostIndicationExAnte.
        :rtype: CostGroup
        """
        return self._sales_costs

    @sales_costs.setter
    def sales_costs(self, sales_costs):
        """Sets the sales_costs of this CostIndicationExAnte.

        CostGroup type V

        :param sales_costs: The sales_costs of this CostIndicationExAnte.
        :type: CostGroup
        """

        self._sales_costs = sales_costs

    @property
    def holding_period(self):
        """Gets the holding_period of this CostIndicationExAnte.

        Holding period in years, displayed on purchase

        :return: The holding_period of this CostIndicationExAnte.
        :rtype: str
        """
        return self._holding_period

    @holding_period.setter
    def holding_period(self, holding_period):
        """Sets the holding_period of this CostIndicationExAnte.

        Holding period in years, displayed on purchase

        :param holding_period: The holding_period of this CostIndicationExAnte.
        :type: str
        """

        self._holding_period = holding_period

    @property
    def total_costs_abs(self):
        """Gets the total_costs_abs of this CostIndicationExAnte.

        Absolute amount of the total costs

        :return: The total_costs_abs of this CostIndicationExAnte.
        :rtype: AmountValue
        """
        return self._total_costs_abs

    @total_costs_abs.setter
    def total_costs_abs(self, total_costs_abs):
        """Sets the total_costs_abs of this CostIndicationExAnte.

        Absolute amount of the total costs

        :param total_costs_abs: The total_costs_abs of this CostIndicationExAnte.
        :type: AmountValue
        """

        self._total_costs_abs = total_costs_abs

    @property
    def total_costs_rel(self):
        """Gets the total_costs_rel of this CostIndicationExAnte.

        Amount of total costs relative to the investment

        :return: The total_costs_rel of this CostIndicationExAnte.
        :rtype: PercentageString
        """
        return self._total_costs_rel

    @total_costs_rel.setter
    def total_costs_rel(self, total_costs_rel):
        """Sets the total_costs_rel of this CostIndicationExAnte.

        Amount of total costs relative to the investment

        :param total_costs_rel: The total_costs_rel of this CostIndicationExAnte.
        :type: PercentageString
        """

        self._total_costs_rel = total_costs_rel

    @property
    def total_costs_detail(self):
        """Gets the total_costs_detail of this CostIndicationExAnte.

        Total cost block including total cost entries segregated as: E (own service costs of bank), F (external service costs), and P (product costs)

        :return: The total_costs_detail of this CostIndicationExAnte.
        :rtype: TotalCostBlock
        """
        return self._total_costs_detail

    @total_costs_detail.setter
    def total_costs_detail(self, total_costs_detail):
        """Sets the total_costs_detail of this CostIndicationExAnte.

        Total cost block including total cost entries segregated as: E (own service costs of bank), F (external service costs), and P (product costs)

        :param total_costs_detail: The total_costs_detail of this CostIndicationExAnte.
        :type: TotalCostBlock
        """

        self._total_costs_detail = total_costs_detail

    @property
    def total_holding_costs(self):
        """Gets the total_holding_costs of this CostIndicationExAnte.

        List of cost blocks over time

        :return: The total_holding_costs of this CostIndicationExAnte.
        :rtype: TotalHoldingCostBlock
        """
        return self._total_holding_costs

    @total_holding_costs.setter
    def total_holding_costs(self, total_holding_costs):
        """Sets the total_holding_costs of this CostIndicationExAnte.

        List of cost blocks over time

        :param total_holding_costs: The total_holding_costs of this CostIndicationExAnte.
        :type: TotalHoldingCostBlock
        """

        self._total_holding_costs = total_holding_costs

    @property
    def link_costs(self):
        """Gets the link_costs of this CostIndicationExAnte.

        HTTP link to further cost information

        :return: The link_costs of this CostIndicationExAnte.
        :rtype: str
        """
        return self._link_costs

    @link_costs.setter
    def link_costs(self, link_costs):
        """Sets the link_costs of this CostIndicationExAnte.

        HTTP link to further cost information

        :param link_costs: The link_costs of this CostIndicationExAnte.
        :type: str
        """

        self._link_costs = link_costs

    @property
    def link_kid(self):
        """Gets the link_kid of this CostIndicationExAnte.

        HTTP link to key information document

        :return: The link_kid of this CostIndicationExAnte.
        :rtype: str
        """
        return self._link_kid

    @link_kid.setter
    def link_kid(self, link_kid):
        """Sets the link_kid of this CostIndicationExAnte.

        HTTP link to key information document

        :param link_kid: The link_kid of this CostIndicationExAnte.
        :type: str
        """

        self._link_kid = link_kid

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
        if issubclass(CostIndicationExAnte, dict):
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
        if not isinstance(other, CostIndicationExAnte):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostIndicationExAnte):
            return True

        return self.to_dict() != other.to_dict()
