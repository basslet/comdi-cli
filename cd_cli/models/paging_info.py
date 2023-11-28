import pprint


class PagingInfo(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {"index": "int", "matches": "int"}

    attribute_map = {"index": "index", "matches": "matches"}

    def __init__(self, index=None, matches=None):
        """PagingInfo"""

        self._index = None
        self._matches = None

        if index is not None:
            self.index = index
        if matches is not None:
            self.matches = matches

    @property
    def index(self):
        """Gets the index of this PagingInfo.


        :return: The index of this PagingInfo.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PagingInfo.


        :param index: The index of this PagingInfo.
        :type: int
        """

        self._index = index

    @property
    def matches(self):
        """Gets the matches of this PagingInfo.


        :return: The matches of this PagingInfo.
        :rtype: int
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this PagingInfo.


        :param matches: The matches of this PagingInfo.
        :type: int
        """

        self._matches = matches

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
        if issubclass(PagingInfo, dict):
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
        if not isinstance(other, PagingInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagingInfo):
            return True

        return self.to_dict() != other.to_dict()
