import pprint


class StaticData(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "notation": "str",
        "currency": "CurrencyString",
        "instrument_type": "str",
        "priips_relevant": "bool",
        "kid_available": "bool",
        "shipping_waiver_required": "bool",
        "fund_redemption_limited": "bool",
    }

    attribute_map = {
        "notation": "notation",
        "currency": "currency",
        "instrument_type": "instrumentType",
        "priips_relevant": "priipsRelevant",
        "kid_available": "kidAvailable",
        "shipping_waiver_required": "shippingWaiverRequired",
        "fund_redemption_limited": "fundRedemptionLimited",
    }

    def __init__(
        self,
        notation=None,
        currency=None,
        instrument_type=None,
        priips_relevant=False,
        kid_available=False,
        shipping_waiver_required=False,
        fund_redemption_limited=False,
    ):
        """StaticData"""

        self._notation = None
        self._currency = None
        self._instrument_type = None
        self._priips_relevant = None
        self._kid_available = None
        self._shipping_waiver_required = None
        self._fund_redemption_limited = None

        if notation is not None:
            self.notation = notation
        if currency is not None:
            self.currency = currency
        if instrument_type is not None:
            self.instrument_type = instrument_type
        if priips_relevant is not None:
            self.priips_relevant = priips_relevant
        if kid_available is not None:
            self.kid_available = kid_available
        if shipping_waiver_required is not None:
            self.shipping_waiver_required = shipping_waiver_required
        if fund_redemption_limited is not None:
            self.fund_redemption_limited = fund_redemption_limited

    @property
    def notation(self):
        """Gets the notation of this StaticData.

        Ticker symbol or notation of a security

        :return: The notation of this StaticData.
        :rtype: str
        """
        return self._notation

    @notation.setter
    def notation(self, notation):
        """Sets the notation of this StaticData.

        Ticker symbol or notation of a security

        :param notation: The notation of this StaticData.
        :type: str
        """
        allowed_values = ["XXX", "XXC", "XXM", "XXP", "XXU"]
        if notation not in allowed_values:
            raise ValueError(
                "Invalid value for `notation` ({0}), must be one of {1}".format(
                    notation, allowed_values
                )
            )

        self._notation = notation

    @property
    def currency(self):
        """Gets the currency of this StaticData.

        instrument currency of a security, e.g., for bonds, bond and open real estate funds; additionally to ISO 4217 currency code the following values are possible: XXX (Pcs.), XXP (Pts.), XXU (Unknown)

        :return: The currency of this StaticData.
        :rtype: CurrencyString
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StaticData.

        instrument currency of a security, e.g., for bonds, bond and open real estate funds; additionally to ISO 4217 currency code the following values are possible: XXX (Pcs.), XXP (Pts.), XXU (Unknown)

        :param currency: The currency of this StaticData.
        :type: CurrencyString
        """

        self._currency = currency

    @property
    def instrument_type(self):
        """Gets the instrument_type of this StaticData.

        Instrument type

        :return: The instrument_type of this StaticData.
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this StaticData.

        Instrument type

        :param instrument_type: The instrument_type of this StaticData.
        :type: str
        """
        allowed_values = [
            "SHARE",
            "BONDS",
            "SUBSCRIPTION_RIGHT",
            "ETF",
            "PROFIT_PART_CERTIFICATE",
            "FUND",
            "WARRANT",
            "CERTIFICATE",
            "NOT_AVAILABLE",
        ]
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}".format(
                    instrument_type, allowed_values
                )
            )

        self._instrument_type = instrument_type

    @property
    def priips_relevant(self):
        """Gets the priips_relevant of this StaticData.

        Flag indicating - if TRUE - that EU-regulation referring to Packaged Retail and Insurance-based Investment Products - PRIIPs) is relevant for the instrument

        :return: The priips_relevant of this StaticData.
        :rtype: bool
        """
        return self._priips_relevant

    @priips_relevant.setter
    def priips_relevant(self, priips_relevant):
        """Sets the priips_relevant of this StaticData.

        Flag indicating - if TRUE - that EU-regulation referring to Packaged Retail and Insurance-based Investment Products - PRIIPs) is relevant for the instrument

        :param priips_relevant: The priips_relevant of this StaticData.
        :type: bool
        """

        self._priips_relevant = priips_relevant

    @property
    def kid_available(self):
        """Gets the kid_available of this StaticData.

        Flag indicating - if TRUE - that a Key Information Document (KID) of the issuer is electronically available. Before order placement a static note ought to displayed in such a case.

        :return: The kid_available of this StaticData.
        :rtype: bool
        """
        return self._kid_available

    @kid_available.setter
    def kid_available(self, kid_available):
        """Sets the kid_available of this StaticData.

        Flag indicating - if TRUE - that a Key Information Document (KID) of the issuer is electronically available. Before order placement a static note ought to displayed in such a case.

        :param kid_available: The kid_available of this StaticData.
        :type: bool
        """

        self._kid_available = kid_available

    @property
    def shipping_waiver_required(self):
        """Gets the shipping_waiver_required of this StaticData.

        Flag indicating - if TRUE - that within prevalidation and before placement of a buy order the investor must approve, e.g., by a frontend checkbox that no shipping of fund sales information is required (waiver); a static note regarding that information ought to be displayed in such a case. Without an explicit waiver the order placement must be prevented in the frontend.

        :return: The shipping_waiver_required of this StaticData.
        :rtype: bool
        """
        return self._shipping_waiver_required

    @shipping_waiver_required.setter
    def shipping_waiver_required(self, shipping_waiver_required):
        """Sets the shipping_waiver_required of this StaticData.

        Flag indicating - if TRUE - that within prevalidation and before placement of a buy order the investor must approve, e.g., by a frontend checkbox that no shipping of fund sales information is required (waiver); a static note regarding that information ought to be displayed in such a case. Without an explicit waiver the order placement must be prevented in the frontend.

        :param shipping_waiver_required: The shipping_waiver_required of this StaticData.
        :type: bool
        """

        self._shipping_waiver_required = shipping_waiver_required

    @property
    def fund_redemption_limited(self):
        """Gets the fund_redemption_limited of this StaticData.

        Flag indicating - if TRUE - that within prevalidation and before placement of a buy order a static note must be displayed indicating that the redemption of the fund is limited.

        :return: The fund_redemption_limited of this StaticData.
        :rtype: bool
        """
        return self._fund_redemption_limited

    @fund_redemption_limited.setter
    def fund_redemption_limited(self, fund_redemption_limited):
        """Sets the fund_redemption_limited of this StaticData.

        Flag indicating - if TRUE - that within prevalidation and before placement of a buy order a static note must be displayed indicating that the redemption of the fund is limited.

        :param fund_redemption_limited: The fund_redemption_limited of this StaticData.
        :type: bool
        """

        self._fund_redemption_limited = fund_redemption_limited

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
        if issubclass(StaticData, dict):
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
        if not isinstance(other, StaticData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaticData):
            return True

        return self.to_dict() != other.to_dict()
