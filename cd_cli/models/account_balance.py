import pprint


class AccountBalance(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "account": "Account",
        "account_id": "str",
        "balance": "AmountValue",
        "balance_eur": "AmountValue",
        "available_cash_amount": "AmountValue",
        "available_cash_amount_eur": "AmountValue",
    }

    attribute_map = {
        "account": "account",
        "account_id": "accountId",
        "balance": "balance",
        "balance_eur": "balanceEUR",
        "available_cash_amount": "availableCashAmount",
        "available_cash_amount_eur": "availableCashAmountEUR",
    }

    def __init__(
        self,
        account=None,
        account_id=None,
        balance=None,
        balance_eur=None,
        available_cash_amount=None,
        available_cash_amount_eur=None,
    ):
        """AccountBalance"""

        self._account = None
        self._account_id = None
        self._balance = None
        self._balance_eur = None
        self._available_cash_amount = None
        self._available_cash_amount_eur = None

        if account is not None:
            self.account = account
        if account_id is not None:
            self.account_id = account_id
        if balance is not None:
            self.balance = balance
        if balance_eur is not None:
            self.balance_eur = balance_eur
        if available_cash_amount is not None:
            self.available_cash_amount = available_cash_amount
        if available_cash_amount_eur is not None:
            self.available_cash_amount_eur = available_cash_amount_eur

    @property
    def account(self):
        """Gets the account of this AccountBalance.

        The master data of this account (attribute can be suppressed by using the parameter 'without-attr=account')

        :return: The account of this AccountBalance.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AccountBalance.

        The master data of this account (attribute can be suppressed by using the parameter 'without-attr=account')

        :param account: The account of this AccountBalance.
        :type: Account
        """

        self._account = account

    @property
    def account_id(self):
        """Gets the account_id of this AccountBalance.

        Account identifier (UUID)

        :return: The account_id of this AccountBalance.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountBalance.

        Account identifier (UUID)

        :param account_id: The account_id of this AccountBalance.
        :type: str
        """

        self._account_id = account_id

    @property
    def balance(self):
        """Gets the balance of this AccountBalance.

        Current balance

        :return: The balance of this AccountBalance.
        :rtype: AmountValue
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountBalance.

        Current balance

        :param balance: The balance of this AccountBalance.
        :type: AmountValue
        """

        self._balance = balance

    @property
    def balance_eur(self):
        """Gets the balance_eur of this AccountBalance.

        Current balance in EUR

        :return: The balance_eur of this AccountBalance.
        :rtype: AmountValue
        """
        return self._balance_eur

    @balance_eur.setter
    def balance_eur(self, balance_eur):
        """Sets the balance_eur of this AccountBalance.

        Current balance in EUR

        :param balance_eur: The balance_eur of this AccountBalance.
        :type: AmountValue
        """

        self._balance_eur = balance_eur

    @property
    def available_cash_amount(self):
        """Gets the available_cash_amount of this AccountBalance.

        Sum of current account balance + credit limit - sum of funds, which are already planned but not yet booked. This is the maximum cash limit

        :return: The available_cash_amount of this AccountBalance.
        :rtype: AmountValue
        """
        return self._available_cash_amount

    @available_cash_amount.setter
    def available_cash_amount(self, available_cash_amount):
        """Sets the available_cash_amount of this AccountBalance.

        Sum of current account balance + credit limit - sum of funds, which are already planned but not yet booked. This is the maximum cash limit

        :param available_cash_amount: The available_cash_amount of this AccountBalance.
        :type: AmountValue
        """

        self._available_cash_amount = available_cash_amount

    @property
    def available_cash_amount_eur(self):
        """Gets the available_cash_amount_eur of this AccountBalance.

        As 'availableCashAmount', but in EUR

        :return: The available_cash_amount_eur of this AccountBalance.
        :rtype: AmountValue
        """
        return self._available_cash_amount_eur

    @available_cash_amount_eur.setter
    def available_cash_amount_eur(self, available_cash_amount_eur):
        """Sets the available_cash_amount_eur of this AccountBalance.

        As 'availableCashAmount', but in EUR

        :param available_cash_amount_eur: The available_cash_amount_eur of this AccountBalance.
        :type: AmountValue
        """

        self._available_cash_amount_eur = available_cash_amount_eur

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
        if issubclass(AccountBalance, dict):
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
        if not isinstance(other, AccountBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalance):
            return True

        return self.to_dict() != other.to_dict()
