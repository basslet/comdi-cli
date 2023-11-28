import pprint


class TimestampString(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"timestamp": "datetime"}

    attribute_map = {"timestamp": "timestamp"}

    def __init__(self, timestamp=None):
        """TimestampString"""

        self._timestamp = None

        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def timestamp(self):
        """Gets the timestamp of this TimestampString.

        Date and time with following format: 'yyyy-MM-dd'T'HH:mm:ss,SSSSSSX'

        :return: The timestamp of this TimestampString.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TimestampString.

        Date and time with following format: 'yyyy-MM-dd'T'HH:mm:ss,SSSSSSX'

        :param timestamp: The timestamp of this TimestampString.
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(TimestampString, dict):
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
        if not isinstance(other, TimestampString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimestampString):
            return True

        return self.to_dict() != other.to_dict()
