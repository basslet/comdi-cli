import pprint
from datetime import datetime, timedelta


class Tokens(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "access_token": "str",
        "token_type": "str",
        "refresh_token": "str",
        "expires_in": "int",
        "scope": "str",
        "kdnr": "str",
        "bpid": "str",
        "kontakt_id": "str",
    }

    attribute_map = {
        "access_token": "access_token",
        "token_type": "token_type",
        "refresh_token": "refresh_token",
        "expires_in": "expires_in",
        "scope": "scope",
        "kdnr": "kdnr",
        "bpid": "bpid",
        "kontakt_id": "kontaktId",
    }

    def __init__(
        self,
        access_token=None,
        token_type=None,
        refresh_token=None,
        expires_in=None,
        scope=None,
        kdnr=None,
        bpid=None,
        kontakt_id=None,
    ):
        """Tokens"""

        self._access_token = None
        self._token_type = None
        self._refresh_token = None
        self._expires_in = None
        self._scope = None
        self._kdnr = None
        self._bpid = None
        self._kontakt_id = None
        # absolute utc expiration date time, not part of the response
        self._expires = None

        if access_token is not None:
            self.access_token = access_token
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if expires_in is not None:
            self.expires_in = expires_in
            self.expires = expires_in
        if scope is not None:
            self.scope = scope
        if kdnr is not None:
            self.kdnr = kdnr
        if bpid is not None:
            self.bpid = bpid
        if kontakt_id is not None:
            self.kontakt_id = kontakt_id

    @property
    def access_token(self):
        """Gets the access_token of this Tokens.

        authentication token

        :return: The access_token of this Tokens.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Tokens.

        authentication token

        :param access_token: The access_token of this Tokens.
        :type: str
        """

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this Tokens.

        type of token (bearer)

        :return: The token_type of this Tokens.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this Tokens.

        type of token (bearer)

        :param token_type: The token_type of this Tokens.
        :type: str
        """

        self._token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this Tokens.

        refresh token

        :return: The refresh_token of this Tokens.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this Tokens.

        refresh token

        :param refresh_token: The refresh_token of this Tokens.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def expires_in(self):
        """Gets the expires_in of this Tokens.

        token validity in seconds (599)

        :return: The expires_in of this Tokens.
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this Tokens.

        token validity in seconds (599)

        :param expires_in: The expires_in of this Tokens.
        :type: str
        """

        self._expires_in = expires_in

    @property
    def expires(self):
        """Gets the expires of this Tokens.

        absolute expiration date time

        :return: The expires_in of this Tokens.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires_in):
        """Sets the expires of this Tokens.

        absolute expiration date time

        :param expires_in: The expires_in of this Tokens.
        :type: str
        """

        self._expires = datetime.utcnow() + timedelta(seconds=expires_in)

    @property
    def scope(self):
        """Gets the scope of this Tokens.

        access rights (TWO_FACTOR)

        :return: The scope of this Tokens.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Tokens.

        access rights (TWO_FACTOR)

        :param scope: The scope of this Tokens.
        :type: str
        """

        self._scope = scope

    @property
    def kdnr(self):
        """Gets the kdnr of this Tokens.

        customer number

        :return: The kdnr of this Tokens.
        :rtype: str
        """
        return self._kdnr

    @kdnr.setter
    def kdnr(self, kdnr):
        """Sets the kdnr of this Tokens.

        customer number

        :param kdnr: The kdnr of this Tokens.
        :type: str
        """

        self._kdnr = kdnr

    @property
    def bpid(self):
        """Gets the bpid of this Tokens.

        internal identification number

        :return: The bpid of this Tokens.
        :rtype: str
        """
        return self._bpid

    @bpid.setter
    def bpid(self, bpid):
        """Sets the bpid of this Tokens.

        internal identification number

        :param bpid: The bpid of this Tokens.
        :type: str
        """

        self._bpid = bpid

    @property
    def kontakt_id(self):
        """Gets the kontakt_id of this Tokens.

        internal identification number

        :return: The kontakt_id of this Tokens.
        :rtype: str
        """
        return self._kontakt_id

    @kontakt_id.setter
    def kontakt_id(self, kontakt_id):
        """Sets the kontakt_id of this Tokens.

        internal identification number

        :param kontakt_id: The kontakt_id of this Tokens.
        :type: str
        """

        self._kontakt_id = kontakt_id

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
        if issubclass(Tokens, dict):
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
        if not isinstance(other, Tokens):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tokens):
            return True

        return self.to_dict() != other.to_dict()
