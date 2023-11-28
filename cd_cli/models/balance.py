import pprint


class Balance(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "account_balance": "AccountBalance",
        "card_balance": "CardBalance",
        "depot_aggregation": "DepotAggregation",
        "fixed_term_savings": "FixedTermSavings",
        "installment_loan_balance": "InstallmentLoanBalance",
    }

    attribute_map = {
        "account_balance": "accountBalance",
        "card_balance": "cardBalance",
        "depot_aggregation": "depotAggregation",
        "fixed_term_savings": "fixedTermSavings",
        "installment_loan_balance": "installmentLoanBalance",
    }

    def __init__(
        self,
        account_balance=None,
        card_balance=None,
        depot_aggregation=None,
        fixed_term_savings=None,
        installment_loan_balance=None,
    ):
        """Balance"""

        self._account_balance = None
        self._card_balance = None
        self._depot_aggregation = None
        self._fixed_term_savings = None
        self._installment_loan_balance = None

        if account_balance is not None:
            self.account_balance = account_balance
        if card_balance is not None:
            self.card_balance = card_balance
        if depot_aggregation is not None:
            self.depot_aggregation = depot_aggregation
        if fixed_term_savings is not None:
            self.fixed_term_savings = fixed_term_savings
        if installment_loan_balance is not None:
            self.installment_loan_balance = installment_loan_balance

    @property
    def account_balance(self):
        """Gets the account_balance of this Balance.

        Balance object for an account

        :return: The account_balance of this Balance.
        :rtype: AccountBalance
        """
        return self._account_balance

    @account_balance.setter
    def account_balance(self, account_balance):
        """Sets the account_balance of this Balance.

        Balance object for an account

        :param account_balance: The account_balance of this Balance.
        :type: AccountBalance
        """

        self._account_balance = account_balance

    @property
    def card_balance(self):
        """Gets the card_balance of this Balance.

        Balance object for a card

        :return: The card_balance of this Balance.
        :rtype: CardBalance
        """
        return self._card_balance

    @card_balance.setter
    def card_balance(self, card_balance):
        """Sets the card_balance of this Balance.

        Balance object for a card

        :param card_balance: The card_balance of this Balance.
        :type: CardBalance
        """

        self._card_balance = card_balance

    @property
    def depot_aggregation(self):
        """Gets the depot_aggregation of this Balance.

        Aggregation object for a depot

        :return: The depot_aggregation of this Balance.
        :rtype: DepotAggregation
        """
        return self._depot_aggregation

    @depot_aggregation.setter
    def depot_aggregation(self, depot_aggregation):
        """Sets the depot_aggregation of this Balance.

        Aggregation object for a depot

        :param depot_aggregation: The depot_aggregation of this Balance.
        :type: DepotAggregation
        """

        self._depot_aggregation = depot_aggregation

    @property
    def fixed_term_savings(self):
        """Gets the fixed_term_savings of this Balance.

        Balance object for a fixed term saving

        :return: The fixed_term_savings of this Balance.
        :rtype: FixedTermSavings
        """
        return self._fixed_term_savings

    @fixed_term_savings.setter
    def fixed_term_savings(self, fixed_term_savings):
        """Sets the fixed_term_savings of this Balance.

        Balance object for a fixed term saving

        :param fixed_term_savings: The fixed_term_savings of this Balance.
        :type: FixedTermSavings
        """

        self._fixed_term_savings = fixed_term_savings

    @property
    def installment_loan_balance(self):
        """Gets the installment_loan_balance of this Balance.

        Balance object for an installment loan

        :return: The installment_loan_balance of this Balance.
        :rtype: InstallmentLoanBalance
        """
        return self._installment_loan_balance

    @installment_loan_balance.setter
    def installment_loan_balance(self, installment_loan_balance):
        """Sets the installment_loan_balance of this Balance.

        Balance object for an installment loan

        :param installment_loan_balance: The installment_loan_balance of this Balance.
        :type: InstallmentLoanBalance
        """

        self._installment_loan_balance = installment_loan_balance

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
        if issubclass(Balance, dict):
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
        if not isinstance(other, Balance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Balance):
            return True

        return self.to_dict() != other.to_dict()
