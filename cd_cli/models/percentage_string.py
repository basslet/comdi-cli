import pprint
import re


class PercentageString(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "pre_decimal_places": "str",
        "decimal_places": "str",
        "percent_string": "str",
    }

    attribute_map = {
        "pre_decimal_places": "preDecimalPlaces",
        "decimal_places": "decimalPlaces",
        "percent_string": "percentString",
    }

    def __init__(
        self, pre_decimal_places=None, decimal_places=None, percent_string=None
    ):
        """PercentageString"""

        self._pre_decimal_places = None
        self._decimal_places = None
        self._percent_string = None

        if pre_decimal_places is not None:
            self.pre_decimal_places = pre_decimal_places
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if percent_string is not None:
            self.percent_string = percent_string

    @property
    def pre_decimal_places(self):
        """Gets the pre_decimal_places of this PercentageString.

        Pre-decimal places

        :return: The pre_decimal_places of this PercentageString.
        :rtype: str
        """
        return self._pre_decimal_places

    @pre_decimal_places.setter
    def pre_decimal_places(self, pre_decimal_places):
        """Sets the pre_decimal_places of this PercentageString.

        Pre-decimal places

        :param pre_decimal_places: The pre_decimal_places of this PercentageString.
        :type: str
        """
        if pre_decimal_places is not None and len(pre_decimal_places) > 18:
            raise ValueError(
                "Invalid value for `pre_decimal_places`, length must be less than or equal to `18`"
            )
        if pre_decimal_places is not None and len(pre_decimal_places) < 0:
            raise ValueError(
                "Invalid value for `pre_decimal_places`, length must be greater than or equal to `0`"
            )
        if pre_decimal_places is not None and not re.search(
            r"^(0|[1-9][0-9]*)$", pre_decimal_places
        ):
            raise ValueError(
                r"Invalid value for `pre_decimal_places`, must be a follow pattern or equal to `/^(0|[1-9][0-9]*)$/`"
            )

        self._pre_decimal_places = pre_decimal_places

    @property
    def decimal_places(self):
        """Gets the decimal_places of this PercentageString.

        Decimal places

        :return: The decimal_places of this PercentageString.
        :rtype: str
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this PercentageString.

        Decimal places

        :param decimal_places: The decimal_places of this PercentageString.
        :type: str
        """
        if decimal_places is not None and not re.search(r"^[0-9]*$", decimal_places):
            raise ValueError(
                r"Invalid value for `decimal_places`, must be a follow pattern or equal to `/^[0-9]*$/`"
            )

        self._decimal_places = decimal_places

    @property
    def percent_string(self):
        """Gets the percent_string of this PercentageString.


        :return: The percent_string of this PercentageString.
        :rtype: str
        """
        return self._percent_string

    @percent_string.setter
    def percent_string(self, percent_string):
        """Sets the percent_string of this PercentageString.


        :param percent_string: The percent_string of this PercentageString.
        :type: str
        """

        self._percent_string = percent_string

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
        if issubclass(PercentageString, dict):
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
        if not isinstance(other, PercentageString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PercentageString):
            return True

        return self.to_dict() != other.to_dict()
