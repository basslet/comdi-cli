import pprint


class DocumentMetadata(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "archived": "bool",
        "date_read": "str",
        "already_read": "bool",
        "predocument_exists": "bool",
    }

    attribute_map = {
        "archived": "archived",
        "date_read": "dateRead",
        "already_read": "alreadyRead",
        "predocument_exists": "predocumentExists",
    }

    def __init__(
        self,
        archived=False,
        date_read=None,
        already_read=False,
        predocument_exists=False,
    ):
        """DocumentMetadata"""

        self._archived = None
        self._date_read = None
        self._already_read = None
        self._predocument_exists = None

        if archived is not None:
            self.archived = archived
        if date_read is not None:
            self.date_read = date_read
        if already_read is not None:
            self.already_read = already_read
        if predocument_exists is not None:
            self.predocument_exists = predocument_exists

    @property
    def archived(self):
        """Gets the archived of this DocumentMetadata.

        Is document archived?

        :return: The archived of this DocumentMetadata.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this DocumentMetadata.

        Is document archived?

        :param archived: The archived of this DocumentMetadata.
        :type: bool
        """

        self._archived = archived

    @property
    def date_read(self):
        """Gets the date_read of this DocumentMetadata.

        Date on which the document was read.

        :return: The date_read of this DocumentMetadata.
        :rtype: str
        """
        return self._date_read

    @date_read.setter
    def date_read(self, date_read):
        """Sets the date_read of this DocumentMetadata.

        Date on which the document was read.

        :param date_read: The date_read of this DocumentMetadata.
        :type: str
        """

        self._date_read = date_read

    @property
    def already_read(self):
        """Gets the already_read of this DocumentMetadata.

        Has the document been read?

        :return: The already_read of this DocumentMetadata.
        :rtype: bool
        """
        return self._already_read

    @already_read.setter
    def already_read(self, already_read):
        """Sets the already_read of this DocumentMetadata.

        Has the document been read?

        :param already_read: The already_read of this DocumentMetadata.
        :type: bool
        """

        self._already_read = already_read

    @property
    def predocument_exists(self):
        """Gets the predocument_exists of this DocumentMetadata.


        :return: The predocument_exists of this DocumentMetadata.
        :rtype: bool
        """
        return self._predocument_exists

    @predocument_exists.setter
    def predocument_exists(self, predocument_exists):
        """Sets the predocument_exists of this DocumentMetadata.


        :param predocument_exists: The predocument_exists of this DocumentMetadata.
        :type: bool
        """

        self._predocument_exists = predocument_exists

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
        if issubclass(DocumentMetadata, dict):
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
        if not isinstance(other, DocumentMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentMetadata):
            return True

        return self.to_dict() != other.to_dict()
