import pprint


class Rating(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"morningstar": "str", "moodys": "str"}

    attribute_map = {"morningstar": "morningstar", "moodys": "moodys"}

    def __init__(self, morningstar=None, moodys=None):
        """Rating"""

        self._morningstar = None
        self._moodys = None

        if morningstar is not None:
            self.morningstar = morningstar
        if moodys is not None:
            self.moodys = moodys

    @property
    def morningstar(self):
        """Gets the morningstar of this Rating.

        Funds Rating

        :return: The morningstar of this Rating.
        :rtype: str
        """
        return self._morningstar

    @morningstar.setter
    def morningstar(self, morningstar):
        """Sets the morningstar of this Rating.

        Funds Rating

        :param morningstar: The morningstar of this Rating.
        :type: str
        """

        self._morningstar = morningstar

    @property
    def moodys(self):
        """Gets the moodys of this Rating.

        Bonds Rating

        :return: The moodys of this Rating.
        :rtype: str
        """
        return self._moodys

    @moodys.setter
    def moodys(self, moodys):
        """Sets the moodys of this Rating.

        Bonds Rating

        :param moodys: The moodys of this Rating.
        :type: str
        """

        self._moodys = moodys

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
        if issubclass(Rating, dict):
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
        if not isinstance(other, Rating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rating):
            return True

        return self.to_dict() != other.to_dict()
