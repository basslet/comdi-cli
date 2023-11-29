import pprint


class Document(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "document_id": "str",
        "name": "str",
        "date_creation": "str",
        "mime_type": "str",
        "deletable": "bool",
        "advertisement": "bool",
        "document_meta_data": "DocumentMetadata",
    }

    attribute_map = {
        "document_id": "documentId",
        "name": "name",
        "date_creation": "dateCreation",
        "mime_type": "mimeType",
        "deletable": "deletable",
        "advertisement": "advertisement",
        "document_meta_data": "documentMetaData",
    }

    def __init__(
        self,
        document_id=None,
        name=None,
        date_creation=None,
        mime_type=None,
        deletable=False,
        advertisement=False,
        document_meta_data=None,
    ):
        """Document"""

        self._document_id = None
        self._name = None
        self._date_creation = None
        self._mime_type = None
        self._deletable = None
        self._advertisement = None
        self._document_meta_data = None

        if document_id is not None:
            self.document_id = document_id
        if name is not None:
            self.name = name
        if date_creation is not None:
            self.date_creation = date_creation
        if mime_type is not None:
            self.mime_type = mime_type
        if deletable is not None:
            self.deletable = deletable
        if advertisement is not None:
            self.advertisement = advertisement
        if document_meta_data is not None:
            self.document_meta_data = document_meta_data

    @property
    def document_id(self):
        """Gets the document_id of this Document.

        Unique ID of the document (UUID)

        :return: The document_id of this Document.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Document.

        Unique ID of the document (UUID)

        :param document_id: The document_id of this Document.
        :type: str
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this Document.

        Name or description of the document.

        :return: The name of this Document.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.

        Name or description of the document.

        :param name: The name of this Document.
        :type: str
        """
        # if name is not None and len(name) > 50:
        #     raise ValueError(
        #         "Invalid value for `name`, length must be less than or equal to `50`"
        #     )
        # if name is not None and len(name) < 0:
        #     raise ValueError(
        #         "Invalid value for `name`, length must be greater than or equal to `0`"
        #     )

        self._name = name

    @property
    def date_creation(self):
        """Gets the date_creation of this Document.

        Date at which the Document was assigned to the client.

        :return: The date_creation of this Document.
        :rtype: str
        """
        return self._date_creation

    @date_creation.setter
    def date_creation(self, date_creation):
        """Sets the date_creation of this Document.

        Date at which the Document was assigned to the client.

        :param date_creation: The date_creation of this Document.
        :type: str
        """

        self._date_creation = date_creation

    @property
    def mime_type(self):
        """Gets the mime_type of this Document.

        The native mimeType of the document.

        :return: The mime_type of this Document.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this Document.

        The native mimeType of the document.

        :param mime_type: The mime_type of this Document.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def deletable(self):
        """Gets the deletable of this Document.

        Is the client allowed to delete the document?

        :return: The deletable of this Document.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this Document.

        Is the client allowed to delete the document?

        :param deletable: The deletable of this Document.
        :type: bool
        """

        self._deletable = deletable

    @property
    def advertisement(self):
        """Gets the advertisement of this Document.

        Is the document advertising comdirect products?

        :return: The advertisement of this Document.
        :rtype: bool
        """
        return self._advertisement

    @advertisement.setter
    def advertisement(self, advertisement):
        """Sets the advertisement of this Document.

        Is the document advertising comdirect products?

        :param advertisement: The advertisement of this Document.
        :type: bool
        """

        self._advertisement = advertisement

    @property
    def document_meta_data(self):
        """Gets the document_meta_data of this Document.

        Object containing optional information about the document. Available information will differ between categories.

        :return: The document_meta_data of this Document.
        :rtype: DocumentMetadata
        """
        return self._document_meta_data

    @document_meta_data.setter
    def document_meta_data(self, document_meta_data):
        """Sets the document_meta_data of this Document.

        Object containing optional information about the document. Available information will differ between categories.

        :param document_meta_data: The document_meta_data of this Document.
        :type: DocumentMetadata
        """

        self._document_meta_data = document_meta_data

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()
