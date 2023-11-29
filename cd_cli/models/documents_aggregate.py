import pprint


class DocumentsAggregate(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "unread_messages": "int",
        "date_oldest_entry": "date",
        "matches_in_this_response": "int",
        "allowed_to_see_all_documents": "bool",
    }

    attribute_map = {
        "unread_messages": "unreadMessages",
        "date_oldest_entry": "dateOldestEntry",
        "matches_in_this_response": "matchesInThisResponse",
        "allowed_to_see_all_documents": "allowedToSeeAllDocuments",
    }

    def __init__(
        self,
        unread_messages=None,
        date_oldest_entry=None,
        matches_in_this_response=None,
        allowed_to_see_all_documents=None,
    ):
        """DocumentsAggregate"""
        self._unread_messages = None
        self._date_oldest_entry = None
        self._matches_in_this_response = None
        self._allowed_to_see_all_documents = None

        if unread_messages is not None:
            self.unread_messages = unread_messages
        if date_oldest_entry is not None:
            self.date_oldest_entry = date_oldest_entry
        if matches_in_this_response is not None:
            self.matches_in_this_response = matches_in_this_response
        if allowed_to_see_all_documents is not None:
            self.allowed_to_see_all_documents = allowed_to_see_all_documents

    @property
    def unread_messages(self):
        return self._unread_messages

    @unread_messages.setter
    def unread_messages(self, unread_messages):
        self._unread_messages = unread_messages

    @property
    def date_oldest_entry(self):
        return self._date_oldest_entry

    @date_oldest_entry.setter
    def date_oldest_entry(self, date_oldest_entry):
        self._date_oldest_entry = date_oldest_entry

    @property
    def matches_in_this_response(self):
        return self._matches_in_this_response

    @matches_in_this_response.setter
    def matches_in_this_response(self, matches_in_this_response):
        self._matches_in_this_response = matches_in_this_response

    @property
    def allowed_to_see_all_documents(self):
        return self._allowed_to_see_all_documents

    @allowed_to_see_all_documents.setter
    def allowed_to_see_all_documents(self, allowed_to_see_all_documents):
        self._allowed_to_see_all_documents = allowed_to_see_all_documents

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
        if issubclass(DocumentsAggregate, dict):
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
        if not isinstance(other, DocumentsAggregate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentsAggregate):
            return True

        return self.to_dict() != other.to_dict()
