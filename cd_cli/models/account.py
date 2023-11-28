import pprint


class Account(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "account_id": "str",
        "account_display_id": "str",
        "currency": "CurrencyString",
        "client_id": "str",
        "account_type": "EnumText",
        "iban": "str",
        "credit_limit": "AmountValue",
    }

    attribute_map = {
        "account_id": "accountId",
        "account_display_id": "accountDisplayId",
        "currency": "currency",
        "client_id": "clientId",
        "account_type": "accountType",
        "iban": "iban",
        "credit_limit": "creditLimit",
    }

    def __init__(
        self,
        account_id=None,
        account_display_id=None,
        currency=None,
        client_id=None,
        account_type=None,
        iban=None,
        credit_limit=None,
    ):
        """Account"""

        self._account_id = None
        self._account_display_id = None
        self._currency = None
        self._client_id = None
        self._account_type = None
        self._iban = None
        self._credit_limit = None

        if account_id is not None:
            self.account_id = account_id
        if account_display_id is not None:
            self.account_display_id = account_display_id
        if currency is not None:
            self.currency = currency
        if client_id is not None:
            self.client_id = client_id
        if account_type is not None:
            self.account_type = account_type
        if iban is not None:
            self.iban = iban
        if credit_limit is not None:
            self.credit_limit = credit_limit

    @property
    def account_id(self):
        """Gets the account_id of this Account.

        Account identifier (UUID)

        :return: The account_id of this Account.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Account.

        Account identifier (UUID)

        :param account_id: The account_id of this Account.
        :type: str
        """

        self._account_id = account_id

    @property
    def account_display_id(self):
        """Gets the account_display_id of this Account.

        Account identfier

        :return: The account_display_id of this Account.
        :rtype: str
        """
        return self._account_display_id

    @account_display_id.setter
    def account_display_id(self, account_display_id):
        """Sets the account_display_id of this Account.

        Account identfier

        :param account_display_id: The account_display_id of this Account.
        :type: str
        """

        self._account_display_id = account_display_id

    @property
    def currency(self):
        """Gets the currency of this Account.

        Account currency

        :return: The currency of this Account.
        :rtype: CurrencyString
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Account.

        Account currency

        :param currency: The currency of this Account.
        :type: CurrencyString
        """

        self._currency = currency

    @property
    def client_id(self):
        """Gets the client_id of this Account.

        Identification Code of the client (UUID)

        :return: The client_id of this Account.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Account.

        Identification Code of the client (UUID)

        :param client_id: The client_id of this Account.
        :type: str
        """

        self._client_id = client_id

    @property
    def account_type(self):
        """Gets the account_type of this Account.

        Account type. 'key' contains the product type, 'text' a description

        :return: The account_type of this Account.
        :rtype: EnumText
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this Account.

        Account type. 'key' contains the product type, 'text' a description

        :param account_type: The account_type of this Account.
        :type: EnumText
        """

        self._account_type = account_type

    @property
    def iban(self):
        """Gets the iban of this Account.

        IBAN (International bank account number), if available

        :return: The iban of this Account.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this Account.

        IBAN (International bank account number), if available

        :param iban: The iban of this Account.
        :type: str
        """

        self._iban = iban

    @property
    def credit_limit(self):
        """Gets the credit_limit of this Account.

        Credit limit, if available

        :return: The credit_limit of this Account.
        :rtype: AmountValue
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this Account.

        Credit limit, if available

        :param credit_limit: The credit_limit of this Account.
        :type: AmountValue
        """

        self._credit_limit = credit_limit

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Account):
            return True

        return self.to_dict() != other.to_dict()
