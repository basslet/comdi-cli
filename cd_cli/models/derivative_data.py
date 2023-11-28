import pprint


class DerivativeData(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "underlying_instrument": "Instrument",
        "underlying_price": "Price",
        "certificate_type": "str",
        "rating": "Rating",
        "strike_price": "AmountValue",
        "leverage": "str",
        "multiplier": "str",
        "expiry_date": "str",
        "yield_pa": "str",
        "remaining_term_in_years": "str",
        "nominal_rate": "str",
        "warrant_type": "str",
        "maturity_date": "str",
        "interest_payment_date": "str",
        "interest_payment_interval": "str",
    }

    attribute_map = {
        "underlying_instrument": "underlyingInstrument",
        "underlying_price": "underlyingPrice",
        "certificate_type": "certificateType",
        "rating": "rating",
        "strike_price": "strikePrice",
        "leverage": "leverage",
        "multiplier": "multiplier",
        "expiry_date": "expiryDate",
        "yield_pa": "yieldPA",
        "remaining_term_in_years": "remainingTermInYears",
        "nominal_rate": "nominalRate",
        "warrant_type": "warrantType",
        "maturity_date": "maturityDate",
        "interest_payment_date": "interestPaymentDate",
        "interest_payment_interval": "interestPaymentInterval",
    }

    def __init__(
        self,
        underlying_instrument=None,
        underlying_price=None,
        certificate_type=None,
        rating=None,
        strike_price=None,
        leverage=None,
        multiplier=None,
        expiry_date=None,
        yield_pa=None,
        remaining_term_in_years=None,
        nominal_rate=None,
        warrant_type=None,
        maturity_date=None,
        interest_payment_date=None,
        interest_payment_interval=None,
    ):
        """DerivativeData"""

        self._underlying_instrument = None
        self._underlying_price = None
        self._certificate_type = None
        self._rating = None
        self._strike_price = None
        self._leverage = None
        self._multiplier = None
        self._expiry_date = None
        self._yield_pa = None
        self._remaining_term_in_years = None
        self._nominal_rate = None
        self._warrant_type = None
        self._maturity_date = None
        self._interest_payment_date = None
        self._interest_payment_interval = None

        if underlying_instrument is not None:
            self.underlying_instrument = underlying_instrument
        if underlying_price is not None:
            self.underlying_price = underlying_price
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if rating is not None:
            self.rating = rating
        if strike_price is not None:
            self.strike_price = strike_price
        if leverage is not None:
            self.leverage = leverage
        if multiplier is not None:
            self.multiplier = multiplier
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if yield_pa is not None:
            self.yield_pa = yield_pa
        if remaining_term_in_years is not None:
            self.remaining_term_in_years = remaining_term_in_years
        if nominal_rate is not None:
            self.nominal_rate = nominal_rate
        if warrant_type is not None:
            self.warrant_type = warrant_type
        if maturity_date is not None:
            self.maturity_date = maturity_date
        if interest_payment_date is not None:
            self.interest_payment_date = interest_payment_date
        if interest_payment_interval is not None:
            self.interest_payment_interval = interest_payment_interval

    @property
    def underlying_instrument(self):
        """Gets the underlying_instrument of this DerivativeData.

        the underlying instrument

        :return: The underlying_instrument of this DerivativeData.
        :rtype: Instrument
        """
        return self._underlying_instrument

    @underlying_instrument.setter
    def underlying_instrument(self, underlying_instrument):
        """Sets the underlying_instrument of this DerivativeData.

        the underlying instrument

        :param underlying_instrument: The underlying_instrument of this DerivativeData.
        :type: Instrument
        """

        self._underlying_instrument = underlying_instrument

    @property
    def underlying_price(self):
        """Gets the underlying_price of this DerivativeData.

        Price of the underlying

        :return: The underlying_price of this DerivativeData.
        :rtype: Price
        """
        return self._underlying_price

    @underlying_price.setter
    def underlying_price(self, underlying_price):
        """Sets the underlying_price of this DerivativeData.

        Price of the underlying

        :param underlying_price: The underlying_price of this DerivativeData.
        :type: Price
        """

        self._underlying_price = underlying_price

    @property
    def certificate_type(self):
        """Gets the certificate_type of this DerivativeData.

        Certificate Type

        :return: The certificate_type of this DerivativeData.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this DerivativeData.

        Certificate Type

        :param certificate_type: The certificate_type of this DerivativeData.
        :type: str
        """
        allowed_values = [
            "Hebel",
            "Index",
            "Basket",
            "Hedge-Fonds-Zertifikat",
            "Discount",
            "Aktienanleihe",
            "Bandbreite",
            "Outperformance",
            "Express",
            "Bonus",
            "Kapitalschutz",
        ]
        if certificate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `certificate_type` ({0}), must be one of {1}".format(
                    certificate_type, allowed_values
                )
            )

        self._certificate_type = certificate_type

    @property
    def rating(self):
        """Gets the rating of this DerivativeData.

        rating

        :return: The rating of this DerivativeData.
        :rtype: Rating
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this DerivativeData.

        rating

        :param rating: The rating of this DerivativeData.
        :type: Rating
        """

        self._rating = rating

    @property
    def strike_price(self):
        """Gets the strike_price of this DerivativeData.

        strike price of the underlying

        :return: The strike_price of this DerivativeData.
        :rtype: AmountValue
        """
        return self._strike_price

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this DerivativeData.

        strike price of the underlying

        :param strike_price: The strike_price of this DerivativeData.
        :type: AmountValue
        """

        self._strike_price = strike_price

    @property
    def leverage(self):
        """Gets the leverage of this DerivativeData.

        Leverage of the derivate

        :return: The leverage of this DerivativeData.
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this DerivativeData.

        Leverage of the derivate

        :param leverage: The leverage of this DerivativeData.
        :type: str
        """

        self._leverage = leverage

    @property
    def multiplier(self):
        """Gets the multiplier of this DerivativeData.

        multiplier of the underlying

        :return: The multiplier of this DerivativeData.
        :rtype: str
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this DerivativeData.

        multiplier of the underlying

        :param multiplier: The multiplier of this DerivativeData.
        :type: str
        """

        self._multiplier = multiplier

    @property
    def expiry_date(self):
        """Gets the expiry_date of this DerivativeData.

        expiry date of a derivative

        :return: The expiry_date of this DerivativeData.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this DerivativeData.

        expiry date of a derivative

        :param expiry_date: The expiry_date of this DerivativeData.
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def yield_pa(self):
        """Gets the yield_pa of this DerivativeData.

        yield p.a.

        :return: The yield_pa of this DerivativeData.
        :rtype: str
        """
        return self._yield_pa

    @yield_pa.setter
    def yield_pa(self, yield_pa):
        """Sets the yield_pa of this DerivativeData.

        yield p.a.

        :param yield_pa: The yield_pa of this DerivativeData.
        :type: str
        """

        self._yield_pa = yield_pa

    @property
    def remaining_term_in_years(self):
        """Gets the remaining_term_in_years of this DerivativeData.

        remaining Term (expiryDate-today)

        :return: The remaining_term_in_years of this DerivativeData.
        :rtype: str
        """
        return self._remaining_term_in_years

    @remaining_term_in_years.setter
    def remaining_term_in_years(self, remaining_term_in_years):
        """Sets the remaining_term_in_years of this DerivativeData.

        remaining Term (expiryDate-today)

        :param remaining_term_in_years: The remaining_term_in_years of this DerivativeData.
        :type: str
        """

        self._remaining_term_in_years = remaining_term_in_years

    @property
    def nominal_rate(self):
        """Gets the nominal_rate of this DerivativeData.

        nominal rate

        :return: The nominal_rate of this DerivativeData.
        :rtype: str
        """
        return self._nominal_rate

    @nominal_rate.setter
    def nominal_rate(self, nominal_rate):
        """Sets the nominal_rate of this DerivativeData.

        nominal rate

        :param nominal_rate: The nominal_rate of this DerivativeData.
        :type: str
        """

        self._nominal_rate = nominal_rate

    @property
    def warrant_type(self):
        """Gets the warrant_type of this DerivativeData.

        Warrant Type

        :return: The warrant_type of this DerivativeData.
        :rtype: str
        """
        return self._warrant_type

    @warrant_type.setter
    def warrant_type(self, warrant_type):
        """Sets the warrant_type of this DerivativeData.

        Warrant Type

        :param warrant_type: The warrant_type of this DerivativeData.
        :type: str
        """
        allowed_values = ["Call", "Put"]
        if warrant_type not in allowed_values:
            raise ValueError(
                "Invalid value for `warrant_type` ({0}), must be one of {1}".format(
                    warrant_type, allowed_values
                )
            )

        self._warrant_type = warrant_type

    @property
    def maturity_date(self):
        """Gets the maturity_date of this DerivativeData.

        maturity Date of a bonds

        :return: The maturity_date of this DerivativeData.
        :rtype: str
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this DerivativeData.

        maturity Date of a bonds

        :param maturity_date: The maturity_date of this DerivativeData.
        :type: str
        """

        self._maturity_date = maturity_date

    @property
    def interest_payment_date(self):
        """Gets the interest_payment_date of this DerivativeData.

        date of the interest payment of a bond

        :return: The interest_payment_date of this DerivativeData.
        :rtype: str
        """
        return self._interest_payment_date

    @interest_payment_date.setter
    def interest_payment_date(self, interest_payment_date):
        """Sets the interest_payment_date of this DerivativeData.

        date of the interest payment of a bond

        :param interest_payment_date: The interest_payment_date of this DerivativeData.
        :type: str
        """

        self._interest_payment_date = interest_payment_date

    @property
    def interest_payment_interval(self):
        """Gets the interest_payment_interval of this DerivativeData.

        interval of the interest payment of a bond\",allowableValues = \"monthly, quarterly, biannualy, annualy

        :return: The interest_payment_interval of this DerivativeData.
        :rtype: str
        """
        return self._interest_payment_interval

    @interest_payment_interval.setter
    def interest_payment_interval(self, interest_payment_interval):
        """Sets the interest_payment_interval of this DerivativeData.

        interval of the interest payment of a bond\",allowableValues = \"monthly, quarterly, biannualy, annualy

        :param interest_payment_interval: The interest_payment_interval of this DerivativeData.
        :type: str
        """
        allowed_values = ["MONTHLY", "QUARTERLY", "SEMIANNUALLY", "ANNUALLY", "OTHER"]
        if interest_payment_interval not in allowed_values:
            raise ValueError(
                "Invalid value for `interest_payment_interval` ({0}), must be one of {1}".format(
                    interest_payment_interval, allowed_values
                )
            )

        self._interest_payment_interval = interest_payment_interval

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
        if issubclass(DerivativeData, dict):
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
        if not isinstance(other, DerivativeData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivativeData):
            return True

        return self.to_dict() != other.to_dict()
