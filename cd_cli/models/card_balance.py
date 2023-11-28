import pprint


class CardBalance(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "card_id": "str",
        "card": "Card",
        "balance": "AmountValue",
        "available_cash_amount": "AmountValue",
    }

    attribute_map = {
        "card_id": "cardId",
        "card": "card",
        "balance": "balance",
        "available_cash_amount": "availableCashAmount",
    }

    def __init__(
        self, card_id=None, card=None, balance=None, available_cash_amount=None
    ):
        """CardBalance"""

        self._card_id = None
        self._card = None
        self._balance = None
        self._available_cash_amount = None

        if card_id is not None:
            self.card_id = card_id
        if card is not None:
            self.card = card
        if balance is not None:
            self.balance = balance
        if available_cash_amount is not None:
            self.available_cash_amount = available_cash_amount

    @property
    def card_id(self):
        """Gets the card_id of this CardBalance.

        Card identifier (UUID).

        :return: The card_id of this CardBalance.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this CardBalance.

        Card identifier (UUID).

        :param card_id: The card_id of this CardBalance.
        :type: str
        """

        self._card_id = card_id

    @property
    def card(self):
        """Gets the card of this CardBalance.

        Master data of the card.

        :return: The card of this CardBalance.
        :rtype: Card
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this CardBalance.

        Master data of the card.

        :param card: The card of this CardBalance.
        :type: Card
        """

        self._card = card

    @property
    def balance(self):
        """Gets the balance of this CardBalance.

        Current balance.

        :return: The balance of this CardBalance.
        :rtype: AmountValue
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CardBalance.

        Current balance.

        :param balance: The balance of this CardBalance.
        :type: AmountValue
        """

        self._balance = balance

    @property
    def available_cash_amount(self):
        """Gets the available_cash_amount of this CardBalance.

        Sum of current account balance + credit limit - sum of scheduled amounts which are not booked yet. This is the maximum cash limit.

        :return: The available_cash_amount of this CardBalance.
        :rtype: AmountValue
        """
        return self._available_cash_amount

    @available_cash_amount.setter
    def available_cash_amount(self, available_cash_amount):
        """Sets the available_cash_amount of this CardBalance.

        Sum of current account balance + credit limit - sum of scheduled amounts which are not booked yet. This is the maximum cash limit.

        :param available_cash_amount: The available_cash_amount of this CardBalance.
        :type: AmountValue
        """

        self._available_cash_amount = available_cash_amount

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
        if issubclass(CardBalance, dict):
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
        if not isinstance(other, CardBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardBalance):
            return True

        return self.to_dict() != other.to_dict()
