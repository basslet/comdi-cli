import pprint


class AccountTransactionAggregate(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "account": "Account",
        "account_id": "str",
        "booking_date_latest_transaction": "date",
        "reference_latest_transaction": "str",
        "latest_transaction_included": "bool",
        "paging_timestamp": "datetime",
    }

    attribute_map = {
        "account": "account",
        "account_id": "accountId",
        "booking_date_latest_transaction": "bookingDateLatestTransaction",
        "reference_latest_transaction": "referenceLatestTransaction",
        "latest_transaction_included": "latestTransactionIncluded",
        "paging_timestamp": "pagingTimestamp",
    }

    def __init__(
        self,
        account=None,
        account_id=None,
        booking_date_latest_transaction=None,
        latest_transaction_included=None,
        paging_timestamp=None,
    ):
        """AccountTransactionAggregate"""
        self._account = None
        self._account_id = None
        self._booking_date_latest_transaction = None
        self._latest_transaction_included = None
        self._paging_timestamp = None

        if account is not None:
            self.account = account
        if account_id is not None:
            self.account_id = account_id
        if booking_date_latest_transaction is not None:
            self.booking_date_latest_transaction = booking_date_latest_transaction
        if latest_transaction_included is not None:
            self.latest_transaction_included = latest_transaction_included
        if paging_timestamp is not None:
            self.paging_timestamp = paging_timestamp

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def booking_date_latest_transaction(self):
        return self._booking_date_latest_transaction

    @booking_date_latest_transaction.setter
    def booking_date_latest_transaction(self, booking_date_latest_transaction):
        self._booking_date_latest_transaction = booking_date_latest_transaction

    @property
    def latest_transaction_included(self):
        return self._latest_transaction_included

    @latest_transaction_included.setter
    def latest_transaction_included(self, latest_transaction_included):
        self._latest_transaction_included = latest_transaction_included

    @property
    def paging_timestamp(self):
        return self._paging_timestamp

    @paging_timestamp.setter
    def reference(self, paging_timestamp):
        self._paging_timestamp = paging_timestamp

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
        if issubclass(AccountTransactionAggregate, dict):
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
        if not isinstance(other, AccountTransactionAggregate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTransactionAggregate):
            return True

        return self.to_dict() != other.to_dict()
