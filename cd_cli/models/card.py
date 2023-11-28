import pprint


class Card(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "card_id": "str",
        "card_type": "EnumText",
        "client_id": "str",
        "participant_id": "str",
        "holder_name": "str",
        "settlement_account_id": "str",
        "card_display_id": "str",
        "card_validity": "str",
        "card_image": "VisaCardImage",
        "primary_account_number_suffix": "str",
        "card_limit": "AmountValue",
        "status": "str",
    }

    attribute_map = {
        "card_id": "cardId",
        "card_type": "cardType",
        "client_id": "clientId",
        "participant_id": "participantId",
        "holder_name": "holderName",
        "settlement_account_id": "settlementAccountId",
        "card_display_id": "cardDisplayId",
        "card_validity": "cardValidity",
        "card_image": "cardImage",
        "primary_account_number_suffix": "primaryAccountNumberSuffix",
        "card_limit": "cardLimit",
        "status": "status",
    }

    def __init__(
        self,
        card_id=None,
        card_type=None,
        client_id=None,
        participant_id=None,
        holder_name=None,
        settlement_account_id=None,
        card_display_id=None,
        card_validity=None,
        card_image=None,
        primary_account_number_suffix=None,
        card_limit=None,
        status=None,
    ):
        """Card"""

        self._card_id = None
        self._card_type = None
        self._client_id = None
        self._participant_id = None
        self._holder_name = None
        self._settlement_account_id = None
        self._card_display_id = None
        self._card_validity = None
        self._card_image = None
        self._primary_account_number_suffix = None
        self._card_limit = None
        self._status = None

        if card_id is not None:
            self.card_id = card_id
        if card_type is not None:
            self.card_type = card_type
        if client_id is not None:
            self.client_id = client_id
        if participant_id is not None:
            self.participant_id = participant_id
        if holder_name is not None:
            self.holder_name = holder_name
        if settlement_account_id is not None:
            self.settlement_account_id = settlement_account_id
        if card_display_id is not None:
            self.card_display_id = card_display_id
        if card_validity is not None:
            self.card_validity = card_validity
        if card_image is not None:
            self.card_image = card_image
        if primary_account_number_suffix is not None:
            self.primary_account_number_suffix = primary_account_number_suffix
        if card_limit is not None:
            self.card_limit = card_limit
        if status is not None:
            self.status = status

    @property
    def card_id(self):
        """Gets the card_id of this Card.

        Card identifier (UUID).

        :return: The card_id of this Card.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this Card.

        Card identifier (UUID).

        :param card_id: The card_id of this Card.
        :type: str
        """

        self._card_id = card_id

    @property
    def card_type(self):
        """Gets the card_type of this Card.

        Type of the card. 'key' contains the card type, 'text' a description

        :return: The card_type of this Card.
        :rtype: EnumText
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this Card.

        Type of the card. 'key' contains the card type, 'text' a description

        :param card_type: The card_type of this Card.
        :type: EnumText
        """

        self._card_type = card_type

    @property
    def client_id(self):
        """Gets the client_id of this Card.

        Client connection uniquely assigned to the credit card account.

        :return: The client_id of this Card.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Card.

        Client connection uniquely assigned to the credit card account.

        :param client_id: The client_id of this Card.
        :type: str
        """

        self._client_id = client_id

    @property
    def participant_id(self):
        """Gets the participant_id of this Card.

        Contract code of the client uniquely assigned to the credit card account.

        :return: The participant_id of this Card.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this Card.

        Contract code of the client uniquely assigned to the credit card account.

        :param participant_id: The participant_id of this Card.
        :type: str
        """

        self._participant_id = participant_id

    @property
    def holder_name(self):
        """Gets the holder_name of this Card.

        Name of the card holder

        :return: The holder_name of this Card.
        :rtype: str
        """
        return self._holder_name

    @holder_name.setter
    def holder_name(self, holder_name):
        """Sets the holder_name of this Card.

        Name of the card holder

        :param holder_name: The holder_name of this Card.
        :type: str
        """

        self._holder_name = holder_name

    @property
    def settlement_account_id(self):
        """Gets the settlement_account_id of this Card.

        Default settlement account number uniquely assigned to the credit card account. In this case, it has to be the current account.

        :return: The settlement_account_id of this Card.
        :rtype: str
        """
        return self._settlement_account_id

    @settlement_account_id.setter
    def settlement_account_id(self, settlement_account_id):
        """Sets the settlement_account_id of this Card.

        Default settlement account number uniquely assigned to the credit card account. In this case, it has to be the current account.

        :param settlement_account_id: The settlement_account_id of this Card.
        :type: str
        """

        self._settlement_account_id = settlement_account_id

    @property
    def card_display_id(self):
        """Gets the card_display_id of this Card.

        Partially masked credit card number.

        :return: The card_display_id of this Card.
        :rtype: str
        """
        return self._card_display_id

    @card_display_id.setter
    def card_display_id(self, card_display_id):
        """Sets the card_display_id of this Card.

        Partially masked credit card number.

        :param card_display_id: The card_display_id of this Card.
        :type: str
        """

        self._card_display_id = card_display_id

    @property
    def card_validity(self):
        """Gets the card_validity of this Card.

        validity of the card. Format: MM/YY

        :return: The card_validity of this Card.
        :rtype: str
        """
        return self._card_validity

    @card_validity.setter
    def card_validity(self, card_validity):
        """Sets the card_validity of this Card.

        validity of the card. Format: MM/YY

        :param card_validity: The card_validity of this Card.
        :type: str
        """

        self._card_validity = card_validity

    @property
    def card_image(self):
        """Gets the card_image of this Card.

        Image of the card.

        :return: The card_image of this Card.
        :rtype: VisaCardImage
        """
        return self._card_image

    @card_image.setter
    def card_image(self, card_image):
        """Sets the card_image of this Card.

        Image of the card.

        :param card_image: The card_image of this Card.
        :type: VisaCardImage
        """

        self._card_image = card_image

    @property
    def primary_account_number_suffix(self):
        """Gets the primary_account_number_suffix of this Card.

        Last 4 digits of the credit card number

        :return: The primary_account_number_suffix of this Card.
        :rtype: str
        """
        return self._primary_account_number_suffix

    @primary_account_number_suffix.setter
    def primary_account_number_suffix(self, primary_account_number_suffix):
        """Sets the primary_account_number_suffix of this Card.

        Last 4 digits of the credit card number

        :param primary_account_number_suffix: The primary_account_number_suffix of this Card.
        :type: str
        """

        self._primary_account_number_suffix = primary_account_number_suffix

    @property
    def card_limit(self):
        """Gets the card_limit of this Card.

        Card limit if available. Will be 0.00 EUR if card has no limit.

        :return: The card_limit of this Card.
        :rtype: AmountValue
        """
        return self._card_limit

    @card_limit.setter
    def card_limit(self, card_limit):
        """Sets the card_limit of this Card.

        Card limit if available. Will be 0.00 EUR if card has no limit.

        :param card_limit: The card_limit of this Card.
        :type: AmountValue
        """

        self._card_limit = card_limit

    @property
    def status(self):
        """Gets the status of this Card.

        Status of the card.

        :return: The status of this Card.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Card.

        Status of the card.

        :param status: The status of this Card.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "IN_CHANGE", "UNKNOWN"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(
                    status, allowed_values
                )
            )

        self._status = status

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
        if issubclass(Card, dict):
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
        if not isinstance(other, Card):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Card):
            return True

        return self.to_dict() != other.to_dict()
