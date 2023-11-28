import pprint


class Session(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "session_id": "int",
        "identifier": "str",
        "session_tan_active": "bool",
        "activated2_fa": "bool",
    }

    attribute_map = {
        "session_id": "id",
        "identifier": "identifier",
        "session_tan_active": "sessionTanActive",
        "activated2_fa": "activated2FA",
    }

    def __init__(
        self,
        session_id=None,
        identifier=None,
        session_tan_active=False,
        activated2_fa=False,
    ):
        """Session"""

        self._session_id = None
        self._identifier = None
        self._session_tan_active = None
        self._activated2_fa = None

        if session_id is not None:
            self.session_id = session_id
        if identifier is not None:
            self.identifier = identifier
        if session_tan_active is not None:
            self.session_tan_active = session_tan_active
        if activated2_fa is not None:
            self.activated2_fa = activated2_fa

    @property
    def session_id(self):
        """Gets the id of this Session.


        :return: The id of this Session.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the id of this Session.


        :param id: The id of this Session.
        :type: int
        """

        self._session_id = session_id

    @property
    def identifier(self):
        """Gets the identifier of this Session.

        Identifier of the session

        :return: The identifier of this Session.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Session.

        Identifier of the session

        :param identifier: The identifier of this Session.
        :type: str
        """

        self._identifier = identifier

    @property
    def session_tan_active(self):
        """Gets the session_tan_active of this Session.

        This boolean is used to point out whether or not the current session has an active session TAN (transaction authentication number). With an active session TAN some use cases, that are genuinely TAN protected, might be callable without asking the client for a TAN. The validation method of session TAN ready use cases will return \"TAN_FREE\" as a TAN type while the session TAN is activated. The session TAN will be available after a refresh of tokens and dies with the last pair of tokens (access and refresh token).

        :return: The session_tan_active of this Session.
        :rtype: bool
        """
        return self._session_tan_active

    @session_tan_active.setter
    def session_tan_active(self, session_tan_active):
        """Sets the session_tan_active of this Session.

        This boolean is used to point out whether or not the current session has an active session TAN (transaction authentication number). With an active session TAN some use cases, that are genuinely TAN protected, might be callable without asking the client for a TAN. The validation method of session TAN ready use cases will return \"TAN_FREE\" as a TAN type while the session TAN is activated. The session TAN will be available after a refresh of tokens and dies with the last pair of tokens (access and refresh token).

        :param session_tan_active: The session_tan_active of this Session.
        :type: bool
        """

        self._session_tan_active = session_tan_active

    @property
    def activated2_fa(self):
        """Gets the activated2_fa of this Session.

        Boolean indicating whether a second factor is already added to this session

        :return: The activated2_fa of this Session.
        :rtype: bool
        """
        return self._activated2_fa

    @activated2_fa.setter
    def activated2_fa(self, activated2_fa):
        """Sets the activated2_fa of this Session.

        Boolean indicating whether a second factor is already added to this session

        :param activated2_fa: The activated2_fa of this Session.
        :type: bool
        """

        self._activated2_fa = activated2_fa

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
        if issubclass(Session, dict):
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
        if not isinstance(other, Session):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Session):
            return True

        return self.to_dict() != other.to_dict()
