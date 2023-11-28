import pprint


class Depot(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "depot_id": "str",
        "depot_display_id": "str",
        "client_id": "str",
        "default_settlement_account_id": "str",
        "settlement_account_ids": "list[str]",
    }

    attribute_map = {
        "depot_id": "depotId",
        "depot_display_id": "depotDisplayId",
        "client_id": "clientId",
        "default_settlement_account_id": "defaultSettlementAccountId",
        "settlement_account_ids": "settlementAccountIds",
    }

    def __init__(
        self,
        depot_id=None,
        depot_display_id=None,
        client_id=None,
        default_settlement_account_id=None,
        settlement_account_ids=None,
    ):
        """Depot"""

        self._depot_id = None
        self._depot_display_id = None
        self._client_id = None
        self._default_settlement_account_id = None
        self._settlement_account_ids = None

        if depot_id is not None:
            self.depot_id = depot_id
        if depot_display_id is not None:
            self.depot_display_id = depot_display_id
        if client_id is not None:
            self.client_id = client_id
        if default_settlement_account_id is not None:
            self.default_settlement_account_id = default_settlement_account_id
        if settlement_account_ids is not None:
            self.settlement_account_ids = settlement_account_ids

    @property
    def depot_id(self):
        """Gets the depot_id of this Depot.

        Securities account Identifier (UUID)

        :return: The depot_id of this Depot.
        :rtype: str
        """
        return self._depot_id

    @depot_id.setter
    def depot_id(self, depot_id):
        """Sets the depot_id of this Depot.

        Securities account Identifier (UUID)

        :param depot_id: The depot_id of this Depot.
        :type: str
        """

        self._depot_id = depot_id

    @property
    def depot_display_id(self):
        """Gets the depot_display_id of this Depot.

        Securities account Number

        :return: The depot_display_id of this Depot.
        :rtype: str
        """
        return self._depot_display_id

    @depot_display_id.setter
    def depot_display_id(self, depot_display_id):
        """Sets the depot_display_id of this Depot.

        Securities account Number

        :param depot_display_id: The depot_display_id of this Depot.
        :type: str
        """

        self._depot_display_id = depot_display_id

    @property
    def client_id(self):
        """Gets the client_id of this Depot.

        Identification code of the client uniquely assigned to the securities account

        :return: The client_id of this Depot.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Depot.

        Identification code of the client uniquely assigned to the securities account

        :param client_id: The client_id of this Depot.
        :type: str
        """

        self._client_id = client_id

    @property
    def default_settlement_account_id(self):
        """Gets the default_settlement_account_id of this Depot.

        Default settlement account number uniquely assigned to the securities account

        :return: The default_settlement_account_id of this Depot.
        :rtype: str
        """
        return self._default_settlement_account_id

    @default_settlement_account_id.setter
    def default_settlement_account_id(self, default_settlement_account_id):
        """Sets the default_settlement_account_id of this Depot.

        Default settlement account number uniquely assigned to the securities account

        :param default_settlement_account_id: The default_settlement_account_id of this Depot.
        :type: str
        """

        self._default_settlement_account_id = default_settlement_account_id

    @property
    def settlement_account_ids(self):
        """Gets the settlement_account_ids of this Depot.

        List of other settlement account identification numbers assigned to the securities account

        :return: The settlement_account_ids of this Depot.
        :rtype: list[str]
        """
        return self._settlement_account_ids

    @settlement_account_ids.setter
    def settlement_account_ids(self, settlement_account_ids):
        """Sets the settlement_account_ids of this Depot.

        List of other settlement account identification numbers assigned to the securities account

        :param settlement_account_ids: The settlement_account_ids of this Depot.
        :type: list[str]
        """

        self._settlement_account_ids = settlement_account_ids

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
        if issubclass(Depot, dict):
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
        if not isinstance(other, Depot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Depot):
            return True

        return self.to_dict() != other.to_dict()
