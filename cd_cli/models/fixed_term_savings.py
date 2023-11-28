import pprint


class FixedTermSavings(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "fixed_term_savings_id": "str",
        "savings_amount": "AmountValue",
        "interest_rate": "str",
        "fixed_term_savings_type": "str",
        "fixed_term_savings_display_name": "str",
        "contract_period_in_months": "int",
        "creation_date": "str",
        "expiration_date": "str",
        "prolongation_amount": "AmountValue",
        "extendable": "bool",
    }

    attribute_map = {
        "fixed_term_savings_id": "fixedTermSavingsId",
        "savings_amount": "savingsAmount",
        "interest_rate": "interestRate",
        "fixed_term_savings_type": "fixedTermSavingsType",
        "fixed_term_savings_display_name": "fixedTermSavingsDisplayName",
        "contract_period_in_months": "contractPeriodInMonths",
        "creation_date": "creationDate",
        "expiration_date": "expirationDate",
        "prolongation_amount": "prolongationAmount",
        "extendable": "extendable",
    }

    def __init__(
        self,
        fixed_term_savings_id=None,
        savings_amount=None,
        interest_rate=None,
        fixed_term_savings_type=None,
        fixed_term_savings_display_name=None,
        contract_period_in_months=None,
        creation_date=None,
        expiration_date=None,
        prolongation_amount=None,
        extendable=False,
    ):
        """FixedTermSavings"""

        self._fixed_term_savings_id = None
        self._savings_amount = None
        self._interest_rate = None
        self._fixed_term_savings_type = None
        self._fixed_term_savings_display_name = None
        self._contract_period_in_months = None
        self._creation_date = None
        self._expiration_date = None
        self._prolongation_amount = None
        self._extendable = None

        if fixed_term_savings_id is not None:
            self.fixed_term_savings_id = fixed_term_savings_id
        if savings_amount is not None:
            self.savings_amount = savings_amount
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if fixed_term_savings_type is not None:
            self.fixed_term_savings_type = fixed_term_savings_type
        if fixed_term_savings_display_name is not None:
            self.fixed_term_savings_display_name = fixed_term_savings_display_name
        if contract_period_in_months is not None:
            self.contract_period_in_months = contract_period_in_months
        if creation_date is not None:
            self.creation_date = creation_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if prolongation_amount is not None:
            self.prolongation_amount = prolongation_amount
        if extendable is not None:
            self.extendable = extendable

    @property
    def fixed_term_savings_id(self):
        """Gets the fixed_term_savings_id of this FixedTermSavings.

        UUID of the deposit account.

        :return: The fixed_term_savings_id of this FixedTermSavings.
        :rtype: str
        """
        return self._fixed_term_savings_id

    @fixed_term_savings_id.setter
    def fixed_term_savings_id(self, fixed_term_savings_id):
        """Sets the fixed_term_savings_id of this FixedTermSavings.

        UUID of the deposit account.

        :param fixed_term_savings_id: The fixed_term_savings_id of this FixedTermSavings.
        :type: str
        """

        self._fixed_term_savings_id = fixed_term_savings_id

    @property
    def savings_amount(self):
        """Gets the savings_amount of this FixedTermSavings.

        Total of investment.

        :return: The savings_amount of this FixedTermSavings.
        :rtype: AmountValue
        """
        return self._savings_amount

    @savings_amount.setter
    def savings_amount(self, savings_amount):
        """Sets the savings_amount of this FixedTermSavings.

        Total of investment.

        :param savings_amount: The savings_amount of this FixedTermSavings.
        :type: AmountValue
        """

        self._savings_amount = savings_amount

    @property
    def interest_rate(self):
        """Gets the interest_rate of this FixedTermSavings.

        Interest rate of the deposit account.

        :return: The interest_rate of this FixedTermSavings.
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this FixedTermSavings.

        Interest rate of the deposit account.

        :param interest_rate: The interest_rate of this FixedTermSavings.
        :type: str
        """

        self._interest_rate = interest_rate

    @property
    def fixed_term_savings_type(self):
        """Gets the fixed_term_savings_type of this FixedTermSavings.

        Type of the deposit account.

        :return: The fixed_term_savings_type of this FixedTermSavings.
        :rtype: str
        """
        return self._fixed_term_savings_type

    @fixed_term_savings_type.setter
    def fixed_term_savings_type(self, fixed_term_savings_type):
        """Sets the fixed_term_savings_type of this FixedTermSavings.

        Type of the deposit account.

        :param fixed_term_savings_type: The fixed_term_savings_type of this FixedTermSavings.
        :type: str
        """
        allowed_values = ["SHORT_TERM", "LONG_TERM"]
        if fixed_term_savings_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fixed_term_savings_type` ({0}), must be one of {1}".format(
                    fixed_term_savings_type, allowed_values
                )
            )

        self._fixed_term_savings_type = fixed_term_savings_type

    @property
    def fixed_term_savings_display_name(self):
        """Gets the fixed_term_savings_display_name of this FixedTermSavings.

        Name of the deposit account.

        :return: The fixed_term_savings_display_name of this FixedTermSavings.
        :rtype: str
        """
        return self._fixed_term_savings_display_name

    @fixed_term_savings_display_name.setter
    def fixed_term_savings_display_name(self, fixed_term_savings_display_name):
        """Sets the fixed_term_savings_display_name of this FixedTermSavings.

        Name of the deposit account.

        :param fixed_term_savings_display_name: The fixed_term_savings_display_name of this FixedTermSavings.
        :type: str
        """

        self._fixed_term_savings_display_name = fixed_term_savings_display_name

    @property
    def contract_period_in_months(self):
        """Gets the contract_period_in_months of this FixedTermSavings.

        Contract period of the deposit account in months.

        :return: The contract_period_in_months of this FixedTermSavings.
        :rtype: int
        """
        return self._contract_period_in_months

    @contract_period_in_months.setter
    def contract_period_in_months(self, contract_period_in_months):
        """Sets the contract_period_in_months of this FixedTermSavings.

        Contract period of the deposit account in months.

        :param contract_period_in_months: The contract_period_in_months of this FixedTermSavings.
        :type: int
        """

        self._contract_period_in_months = contract_period_in_months

    @property
    def creation_date(self):
        """Gets the creation_date of this FixedTermSavings.

        Start date of investment.

        :return: The creation_date of this FixedTermSavings.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this FixedTermSavings.

        Start date of investment.

        :param creation_date: The creation_date of this FixedTermSavings.
        :type: str
        """

        self._creation_date = creation_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this FixedTermSavings.

        End date of investment.

        :return: The expiration_date of this FixedTermSavings.
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this FixedTermSavings.

        End date of investment.

        :param expiration_date: The expiration_date of this FixedTermSavings.
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def prolongation_amount(self):
        """Gets the prolongation_amount of this FixedTermSavings.

        Amount of money for prolongation.

        :return: The prolongation_amount of this FixedTermSavings.
        :rtype: AmountValue
        """
        return self._prolongation_amount

    @prolongation_amount.setter
    def prolongation_amount(self, prolongation_amount):
        """Sets the prolongation_amount of this FixedTermSavings.

        Amount of money for prolongation.

        :param prolongation_amount: The prolongation_amount of this FixedTermSavings.
        :type: AmountValue
        """

        self._prolongation_amount = prolongation_amount

    @property
    def extendable(self):
        """Gets the extendable of this FixedTermSavings.

        Indicates whether the investment can be extended.

        :return: The extendable of this FixedTermSavings.
        :rtype: bool
        """
        return self._extendable

    @extendable.setter
    def extendable(self, extendable):
        """Sets the extendable of this FixedTermSavings.

        Indicates whether the investment can be extended.

        :param extendable: The extendable of this FixedTermSavings.
        :type: bool
        """

        self._extendable = extendable

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
        if issubclass(FixedTermSavings, dict):
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
        if not isinstance(other, FixedTermSavings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FixedTermSavings):
            return True

        return self.to_dict() != other.to_dict()
