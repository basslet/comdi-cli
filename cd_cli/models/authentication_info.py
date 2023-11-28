import pprint


class AuthenticationInfo(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "authentication_info_id": "str",
        "typ": "str",
        "challenge": "str",
        "available_types": "list[str]",
    }

    attribute_map = {
        "authentication_info_id": "id",
        "typ": "typ",
        "challenge": "challenge",
        "available_types": "availableTypes",
    }

    def __init__(
        self,
        authentication_info_id=None,
        typ=None,
        challenge=None,
        available_types=None,
    ):
        """AuthenticationInfo"""

        self._authentication_info_id = None
        self._typ = None
        self._challenge = None
        self._available_types = None

        if authentication_info_id is not None:
            self.authentication_info_id = authentication_info_id
        if typ is not None:
            self.typ = typ
        if challenge is not None:
            self.balance = challenge
        if available_types is not None:
            self.available_types = available_types

    @property
    def authentication_info_id(self):
        """Gets the authentication_info_id of this AuthenticationInfo.

        ID of the TAN challenge

        :return: The authentication_info_id of this AuthenticationInfo.
        :rtype: str
        """
        return self._authentication_info_id

    @authentication_info_id.setter
    def authentication_info_id(self, authentication_info_id):
        """Sets the authentication_info_id of this AuthenticationInfo.

        ID of the TAN challenge

        :param authentication_info_id: The authentication_info_id of this AuthenticationInfo.
        :type: str
        """

        self._authentication_info_id = authentication_info_id

    @property
    def typ(self):
        """Gets the typ of this AuthenticationInfo.

        the TAN type; possible values are M_TAN, P_TAN, P_TAN_PUSH

        :return: The typ of this AuthenticationInfo.
        :rtype: str
        """
        return self._typ

    @typ.setter
    def typ(self, typ):
        """Sets the typ of this AuthenticationInfo.

        the TAN type; possible values are M_TAN, P_TAN, P_TAN_PUSH

        :param typ: The typ of this AuthenticationInfo.
        :type: str
        """

        self._typ = typ

    @property
    def challenge(self):
        """Gets the challenge of this AuthenticationInfo.

        challenge: different specifications are made for each TAN procedure; for P_TAN, the
        photoTAN graphic in PNG format (Base64-encoded), for MTAN the phone number to which the mobileTAN was sent

        :return: The challenge of this AuthenticationInfo.
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this AuthenticationInfo.

        challenge: different specifications are made for each TAN procedure; for P_TAN, the
        photoTAN graphic in PNG format (Base64-encoded), for MTAN the phone number to which the mobileTAN was sent

        :param challenge: The challenge of this AuthenticationInfo.
        :type: str
        """

        self._challenge = challenge

    @property
    def available_types(self):
        """Gets the available_types of this AuthenticationInfo.

        available TAN methods

        :return: The available_types of this AuthenticationInfo.
        :rtype: list[str]
        """
        return self._available_types

    @available_types.setter
    def available_types(self, available_types):
        """Sets the available_types of this AuthenticationInfo.

        available TAN methods

        :param available_types: The available_types of this AuthenticationInfo.
        :type: list[str]
        """

        self._available_types = available_types

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
        if issubclass(AuthenticationInfo, dict):
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
        if not isinstance(other, AuthenticationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationInfo):
            return True

        return self.to_dict() != other.to_dict()
