import pprint


class FundDistribution(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "fund_status": "str",
        "fund_flags": "list[str]",
        "currency": "str",
        "regular_issue_surcharge": "str",
        "discount_issue_surcharge": "str",
        "reduced_issue_surcharge": "str",
        "individual_issue_surcharge": "str",
        "is_individual_issue_surcharge_corrected": "bool",
        "bonification": "str",
        "investment_category": "str",
        "total_expense_ratio": "str",
        "rating": "Rating",
    }

    attribute_map = {
        "fund_status": "fundStatus",
        "fund_flags": "fundFlags",
        "currency": "currency",
        "regular_issue_surcharge": "regularIssueSurcharge",
        "discount_issue_surcharge": "discountIssueSurcharge",
        "reduced_issue_surcharge": "reducedIssueSurcharge",
        "individual_issue_surcharge": "individualIssueSurcharge",
        "is_individual_issue_surcharge_corrected": "isIndividualIssueSurchargeCorrected",
        "bonification": "bonification",
        "investment_category": "investmentCategory",
        "total_expense_ratio": "totalExpenseRatio",
        "rating": "rating",
    }

    def __init__(
        self,
        fund_status=None,
        fund_flags=None,
        currency=None,
        regular_issue_surcharge=None,
        discount_issue_surcharge=None,
        reduced_issue_surcharge=None,
        individual_issue_surcharge=None,
        is_individual_issue_surcharge_corrected=False,
        bonification=None,
        investment_category=None,
        total_expense_ratio=None,
        rating=None,
    ):
        """FundDistribution"""

        self._fund_status = None
        self._fund_flags = None
        self._currency = None
        self._regular_issue_surcharge = None
        self._discount_issue_surcharge = None
        self._reduced_issue_surcharge = None
        self._individual_issue_surcharge = None
        self._is_individual_issue_surcharge_corrected = None
        self._bonification = None
        self._investment_category = None
        self._total_expense_ratio = None
        self._rating = None

        if fund_status is not None:
            self.fund_status = fund_status
        if fund_flags is not None:
            self.fund_flags = fund_flags
        if currency is not None:
            self.currency = currency
        if regular_issue_surcharge is not None:
            self.regular_issue_surcharge = regular_issue_surcharge
        if discount_issue_surcharge is not None:
            self.discount_issue_surcharge = discount_issue_surcharge
        if reduced_issue_surcharge is not None:
            self.reduced_issue_surcharge = reduced_issue_surcharge
        if individual_issue_surcharge is not None:
            self.individual_issue_surcharge = individual_issue_surcharge
        if is_individual_issue_surcharge_corrected is not None:
            self.is_individual_issue_surcharge_corrected = (
                is_individual_issue_surcharge_corrected
            )
        if bonification is not None:
            self.bonification = bonification
        if investment_category is not None:
            self.investment_category = investment_category
        if total_expense_ratio is not None:
            self.total_expense_ratio = total_expense_ratio
        if rating is not None:
            self.rating = rating

    @property
    def fund_status(self):
        """Gets the fund_status of this FundDistribution.

        Status of fund

        :return: The fund_status of this FundDistribution.
        :rtype: str
        """
        return self._fund_status

    @fund_status.setter
    def fund_status(self, fund_status):
        """Sets the fund_status of this FundDistribution.

        Status of fund

        :param fund_status: The fund_status of this FundDistribution.
        :type: str
        """
        allowed_values = ["A", "K", "P", "R", "V", "N", "L", "D", "F", "I", "M"]
        if fund_status not in allowed_values:
            raise ValueError(
                "Invalid value for `fund_status` ({0}), must be one of {1}".format(
                    fund_status, allowed_values
                )
            )

        self._fund_status = fund_status

    @property
    def fund_flags(self):
        """Gets the fund_flags of this FundDistribution.

        List of different features of funds

        :return: The fund_flags of this FundDistribution.
        :rtype: list[str]
        """
        return self._fund_flags

    @fund_flags.setter
    def fund_flags(self, fund_flags):
        """Sets the fund_flags of this FundDistribution.

        List of different features of funds

        :param fund_flags: The fund_flags of this FundDistribution.
        :type: list[str]
        """

        self._fund_flags = fund_flags

    @property
    def currency(self):
        """Gets the currency of this FundDistribution.

        currency of fund

        :return: The currency of this FundDistribution.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FundDistribution.

        currency of fund

        :param currency: The currency of this FundDistribution.
        :type: str
        """

        self._currency = currency

    @property
    def regular_issue_surcharge(self):
        """Gets the regular_issue_surcharge of this FundDistribution.

        Regular issue surcharge

        :return: The regular_issue_surcharge of this FundDistribution.
        :rtype: str
        """
        return self._regular_issue_surcharge

    @regular_issue_surcharge.setter
    def regular_issue_surcharge(self, regular_issue_surcharge):
        """Sets the regular_issue_surcharge of this FundDistribution.

        Regular issue surcharge

        :param regular_issue_surcharge: The regular_issue_surcharge of this FundDistribution.
        :type: str
        """

        self._regular_issue_surcharge = regular_issue_surcharge

    @property
    def discount_issue_surcharge(self):
        """Gets the discount_issue_surcharge of this FundDistribution.

        Discount issue surcharge

        :return: The discount_issue_surcharge of this FundDistribution.
        :rtype: str
        """
        return self._discount_issue_surcharge

    @discount_issue_surcharge.setter
    def discount_issue_surcharge(self, discount_issue_surcharge):
        """Sets the discount_issue_surcharge of this FundDistribution.

        Discount issue surcharge

        :param discount_issue_surcharge: The discount_issue_surcharge of this FundDistribution.
        :type: str
        """

        self._discount_issue_surcharge = discount_issue_surcharge

    @property
    def reduced_issue_surcharge(self):
        """Gets the reduced_issue_surcharge of this FundDistribution.

        Reduced issue surcharge

        :return: The reduced_issue_surcharge of this FundDistribution.
        :rtype: str
        """
        return self._reduced_issue_surcharge

    @reduced_issue_surcharge.setter
    def reduced_issue_surcharge(self, reduced_issue_surcharge):
        """Sets the reduced_issue_surcharge of this FundDistribution.

        Reduced issue surcharge

        :param reduced_issue_surcharge: The reduced_issue_surcharge of this FundDistribution.
        :type: str
        """

        self._reduced_issue_surcharge = reduced_issue_surcharge

    @property
    def individual_issue_surcharge(self):
        """Gets the individual_issue_surcharge of this FundDistribution.

        Individual issue surcharge

        :return: The individual_issue_surcharge of this FundDistribution.
        :rtype: str
        """
        return self._individual_issue_surcharge

    @individual_issue_surcharge.setter
    def individual_issue_surcharge(self, individual_issue_surcharge):
        """Sets the individual_issue_surcharge of this FundDistribution.

        Individual issue surcharge

        :param individual_issue_surcharge: The individual_issue_surcharge of this FundDistribution.
        :type: str
        """

        self._individual_issue_surcharge = individual_issue_surcharge

    @property
    def is_individual_issue_surcharge_corrected(self):
        """Gets the is_individual_issue_surcharge_corrected of this FundDistribution.

        Is individual issue surcharge corrected

        :return: The is_individual_issue_surcharge_corrected of this FundDistribution.
        :rtype: bool
        """
        return self._is_individual_issue_surcharge_corrected

    @is_individual_issue_surcharge_corrected.setter
    def is_individual_issue_surcharge_corrected(
        self, is_individual_issue_surcharge_corrected
    ):
        """Sets the is_individual_issue_surcharge_corrected of this FundDistribution.

        Is individual issue surcharge corrected

        :param is_individual_issue_surcharge_corrected: The is_individual_issue_surcharge_corrected of this FundDistribution.
        :type: bool
        """

        self._is_individual_issue_surcharge_corrected = (
            is_individual_issue_surcharge_corrected
        )

    @property
    def bonification(self):
        """Gets the bonification of this FundDistribution.

        Bonification

        :return: The bonification of this FundDistribution.
        :rtype: str
        """
        return self._bonification

    @bonification.setter
    def bonification(self, bonification):
        """Sets the bonification of this FundDistribution.

        Bonification

        :param bonification: The bonification of this FundDistribution.
        :type: str
        """

        self._bonification = bonification

    @property
    def investment_category(self):
        """Gets the investment_category of this FundDistribution.

        Investment category

        :return: The investment_category of this FundDistribution.
        :rtype: str
        """
        return self._investment_category

    @investment_category.setter
    def investment_category(self, investment_category):
        """Sets the investment_category of this FundDistribution.

        Investment category

        :param investment_category: The investment_category of this FundDistribution.
        :type: str
        """

        self._investment_category = investment_category

    @property
    def total_expense_ratio(self):
        """Gets the total_expense_ratio of this FundDistribution.

        Total expense ratio

        :return: The total_expense_ratio of this FundDistribution.
        :rtype: str
        """
        return self._total_expense_ratio

    @total_expense_ratio.setter
    def total_expense_ratio(self, total_expense_ratio):
        """Sets the total_expense_ratio of this FundDistribution.

        Total expense ratio

        :param total_expense_ratio: The total_expense_ratio of this FundDistribution.
        :type: str
        """

        self._total_expense_ratio = total_expense_ratio

    @property
    def rating(self):
        """Gets the rating of this FundDistribution.

        Rating

        :return: The rating of this FundDistribution.
        :rtype: Rating
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this FundDistribution.

        Rating

        :param rating: The rating of this FundDistribution.
        :type: Rating
        """

        self._rating = rating

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
        if issubclass(FundDistribution, dict):
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
        if not isinstance(other, FundDistribution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundDistribution):
            return True

        return self.to_dict() != other.to_dict()
