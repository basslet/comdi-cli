import pprint


class Instrument(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "instrument_id": "str",
        "wkn": "str",
        "isin": "str",
        "mnemonic": "str",
        "name": "str",
        "short_name": "str",
        "static_data": "StaticData",
        "order_dimensions": "Dimensions",
        "funds_distribution": "FundDistribution",
        "derivative_data": "DerivativeData",
    }

    attribute_map = {
        "instrument_id": "instrumentId",
        "wkn": "wkn",
        "isin": "isin",
        "mnemonic": "mnemonic",
        "name": "name",
        "short_name": "shortName",
        "static_data": "staticData",
        "order_dimensions": "orderDimensions",
        "funds_distribution": "fundsDistribution",
        "derivative_data": "derivativeData",
    }

    def __init__(
        self,
        instrument_id=None,
        wkn=None,
        isin=None,
        mnemonic=None,
        name=None,
        short_name=None,
        static_data=None,
        order_dimensions=None,
        funds_distribution=None,
        derivative_data=None,
    ):
        """Instrument"""

        self._instrument_id = None
        self._wkn = None
        self._isin = None
        self._mnemonic = None
        self._name = None
        self._short_name = None
        self._static_data = None
        self._order_dimensions = None
        self._funds_distribution = None
        self._derivative_data = None

        if instrument_id is not None:
            self.instrument_id = instrument_id
        if wkn is not None:
            self.wkn = wkn
        if isin is not None:
            self.isin = isin
        if mnemonic is not None:
            self.mnemonic = mnemonic
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if static_data is not None:
            self.static_data = static_data
        if order_dimensions is not None:
            self.order_dimensions = order_dimensions
        if funds_distribution is not None:
            self.funds_distribution = funds_distribution
        if derivative_data is not None:
            self.derivative_data = derivative_data

    @property
    def instrument_id(self):
        """Gets the instrument_id of this Instrument.

        Instrument id (UUID), unique identification of an instrument (security, derivative, etc.) for future use

        :return: The instrument_id of this Instrument.
        :rtype: str
        """
        return self._instrument_id

    @instrument_id.setter
    def instrument_id(self, instrument_id):
        """Sets the instrument_id of this Instrument.

        Instrument id (UUID), unique identification of an instrument (security, derivative, etc.) for future use

        :param instrument_id: The instrument_id of this Instrument.
        :type: str
        """

        self._instrument_id = instrument_id

    @property
    def wkn(self):
        """Gets the wkn of this Instrument.

        WKN

        :return: The wkn of this Instrument.
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn):
        """Sets the wkn of this Instrument.

        WKN

        :param wkn: The wkn of this Instrument.
        :type: str
        """

        self._wkn = wkn

    @property
    def isin(self):
        """Gets the isin of this Instrument.

        ISIN

        :return: The isin of this Instrument.
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this Instrument.

        ISIN

        :param isin: The isin of this Instrument.
        :type: str
        """

        self._isin = isin

    @property
    def mnemonic(self):
        """Gets the mnemonic of this Instrument.

        Security symbol according to WM data-service

        :return: The mnemonic of this Instrument.
        :rtype: str
        """
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, mnemonic):
        """Sets the mnemonic of this Instrument.

        Security symbol according to WM data-service

        :param mnemonic: The mnemonic of this Instrument.
        :type: str
        """

        self._mnemonic = mnemonic

    @property
    def name(self):
        """Gets the name of this Instrument.

        Name of the instrument

        :return: The name of this Instrument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instrument.

        Name of the instrument

        :param name: The name of this Instrument.
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Instrument.

        Short name of the instrument

        :return: The short_name of this Instrument.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Instrument.

        Short name of the instrument

        :param short_name: The short_name of this Instrument.
        :type: str
        """

        self._short_name = short_name

    @property
    def static_data(self):
        """Gets the static_data of this Instrument.

        Static data of the instrument, e.g., notation, instrument type

        :return: The static_data of this Instrument.
        :rtype: StaticData
        """
        return self._static_data

    @static_data.setter
    def static_data(self, static_data):
        """Sets the static_data of this Instrument.

        Static data of the instrument, e.g., notation, instrument type

        :param static_data: The static_data of this Instrument.
        :type: StaticData
        """

        self._static_data = static_data

    @property
    def order_dimensions(self):
        """Gets the order_dimensions of this Instrument.

        List of the trading venues including the attributes (orderDimensions)

        :return: The order_dimensions of this Instrument.
        :rtype: Dimensions
        """
        return self._order_dimensions

    @order_dimensions.setter
    def order_dimensions(self, order_dimensions):
        """Sets the order_dimensions of this Instrument.

        List of the trading venues including the attributes (orderDimensions)

        :param order_dimensions: The order_dimensions of this Instrument.
        :type: Dimensions
        """

        self._order_dimensions = order_dimensions

    @property
    def funds_distribution(self):
        """Gets the funds_distribution of this Instrument.

        additional fund data, if the instrument is a fund

        :return: The funds_distribution of this Instrument.
        :rtype: FundDistribution
        """
        return self._funds_distribution

    @funds_distribution.setter
    def funds_distribution(self, funds_distribution):
        """Sets the funds_distribution of this Instrument.

        additional fund data, if the instrument is a fund

        :param funds_distribution: The funds_distribution of this Instrument.
        :type: FundDistribution
        """

        self._funds_distribution = funds_distribution

    @property
    def derivative_data(self):
        """Gets the derivative_data of this Instrument.

        additional data of a derivative

        :return: The derivative_data of this Instrument.
        :rtype: DerivativeData
        """
        return self._derivative_data

    @derivative_data.setter
    def derivative_data(self, derivative_data):
        """Sets the derivative_data of this Instrument.

        additional data of a derivative

        :param derivative_data: The derivative_data of this Instrument.
        :type: DerivativeData
        """

        self._derivative_data = derivative_data

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
        if issubclass(Instrument, dict):
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
        if not isinstance(other, Instrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Instrument):
            return True

        return self.to_dict() != other.to_dict()
