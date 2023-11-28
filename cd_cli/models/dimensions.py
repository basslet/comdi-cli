import pprint


class Dimensions(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"venues": "list[Venue]"}

    attribute_map = {"venues": "venues"}

    def __init__(self, venues=None):
        """Dimensions"""

        self._venues = None

        if venues is not None:
            self.venues = venues

    @property
    def venues(self):
        """Gets the venues of this Dimensions.


        :return: The venues of this Dimensions.
        :rtype: list[Venue]
        """
        return self._venues

    @venues.setter
    def venues(self, venues):
        """Sets the venues of this Dimensions.


        :param venues: The venues of this Dimensions.
        :type: list[Venue]
        """

        self._venues = venues

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
        if issubclass(Dimensions, dict):
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
        if not isinstance(other, Dimensions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Dimensions):
            return True

        return self.to_dict() != other.to_dict()
