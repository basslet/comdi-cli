import pprint


class DateTimeString(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"date_time": "datetime"}

    attribute_map = {"date_time": "dateTime"}

    def __init__(self, date_time=None):
        """DateTimeString"""

        self._date_time = None

        if date_time is not None:
            self.date_time = date_time

    @property
    def date_time(self):
        """Gets the date_time of this DateTimeString.

        Time with format: 'yyyy-MM-dd'T'HH:mm:ssX'

        :return: The date_time of this DateTimeString.
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this DateTimeString.

        Time with format: 'yyyy-MM-dd'T'HH:mm:ssX'

        :param date_time: The date_time of this DateTimeString.
        :type: datetime
        """

        self._date_time = date_time

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
        if issubclass(DateTimeString, dict):
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
        if not isinstance(other, DateTimeString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DateTimeString):
            return True

        return self.to_dict() != other.to_dict()
