import pprint


class AccountTransaction(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "reference": "str",
        "booking_status": "str",
        "booking_date": "date",
        "amount": "AmountValue",
        "remitter": "AccountInformation",
        "deptor": "AccountInformation",
        "creditor": "AccountInformation",
        "valuta_date": "date",
        "direct_debit_creditor_id": "str",
        "direct_debit_mandate_id": "str",
        "end_to_end_reference": "str",
        "new_transaction": "bool",
        "remittance_info": "str",
        "transaction_type": "EnumText",
    }

    attribute_map = {
        "reference": "reference",
        "booking_status": "bookingStatus",
        "booking_date": "bookingDate",
        "amount": "amount",
        "remitter": "remitter",
        "deptor": "deptor",
        "creditor": "creditor",
        "valuta_date": "valutaDate",
        "direct_debit_creditor_id": "directDebitCreditorId",
        "direct_debit_mandate_id": "directDebitMandateId",
        "end_to_end_reference": "endToEndReference",
        "new_transaction": "newTransaction",
        "remittance_info": "remittanceInfo",
        "transaction_type": "transactionType",
    }

    def __init__(
        self,
        reference=None,
        booking_status=None,
        booking_date=None,
        amount=None,
        remitter=None,
        deptor=None,
        creditor=None,
        valuta_date=None,
        direct_debit_creditor_id=None,
        direct_debit_mandate_id=None,
        end_to_end_reference=None,
        new_transaction=False,
        remittance_info=None,
        transaction_type=None,
    ):
        """AccountTransaction"""

        self._reference = None
        self._booking_status = None
        self._booking_date = None
        self._amount = None
        self._remitter = None
        self._deptor = None
        self._creditor = None
        self._valuta_date = None
        self._direct_debit_creditor_id = None
        self._direct_debit_mandate_id = None
        self._end_to_end_reference = None
        self._new_transaction = None
        self._remittance_info = None
        self._transaction_type = None

        if reference is not None:
            self.reference = reference
        if booking_status is not None:
            self.booking_status = booking_status
        if booking_date is not None:
            self.booking_date = booking_date
        if amount is not None:
            self.amount = amount
        if remitter is not None:
            self.remitter = remitter
        if deptor is not None:
            self.deptor = deptor
        if creditor is not None:
            self.creditor = creditor
        if valuta_date is not None:
            self.valuta_date = valuta_date
        if direct_debit_creditor_id is not None:
            self.direct_debit_creditor_id = direct_debit_creditor_id
        if direct_debit_mandate_id is not None:
            self.direct_debit_mandate_id = direct_debit_mandate_id
        if end_to_end_reference is not None:
            self.end_to_end_reference = end_to_end_reference
        if new_transaction is not None:
            self.new_transaction = new_transaction
        if remittance_info is not None:
            self.remittance_info = remittance_info
        if transaction_type is not None:
            self.transaction_type = transaction_type

    @property
    def reference(self):
        """Gets the reference of this AccountTransaction.

        unique reference code of the transaction

        :return: The reference of this AccountTransaction.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this AccountTransaction.

        unique reference code of the transaction

        :param reference: The reference of this AccountTransaction.
        :type: str
        """

        self._reference = reference

    @property
    def booking_status(self):
        """Gets the booking_status of this AccountTransaction.

        Status of transaction

        :return: The booking_status of this AccountTransaction.
        :rtype: str
        """
        return self._booking_status

    @booking_status.setter
    def booking_status(self, booking_status):
        """Sets the booking_status of this AccountTransaction.

        Status of transaction

        :param booking_status: The booking_status of this AccountTransaction.
        :type: str
        """
        allowed_values = ["BOOKED", "NOTBOOKED"]
        if booking_status not in allowed_values:
            raise ValueError(
                "Invalid value for `booking_status` ({0}), must be one of {1}".format(
                    booking_status, allowed_values
                )
            )

        self._booking_status = booking_status

    @property
    def booking_date(self):
        """Gets the booking_date of this AccountTransaction.

        The booking date

        :return: The booking_date of this AccountTransaction.
        :rtype: DateString
        """
        return self._booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        """Sets the booking_date of this AccountTransaction.

        The booking date

        :param booking_date: The booking_date of this AccountTransaction.
        :type: DateString
        """

        self._booking_date = booking_date

    @property
    def amount(self):
        """Gets the amount of this AccountTransaction.

        The amount

        :return: The amount of this AccountTransaction.
        :rtype: AmountValue
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountTransaction.

        The amount

        :param amount: The amount of this AccountTransaction.
        :type: AmountValue
        """

        self._amount = amount

    @property
    def remitter(self):
        """Gets the remitter of this AccountTransaction.

        Account information of name, IBAN and BIC of the remitter.

        :return: The remitter of this AccountTransaction.
        :rtype: AccountInformation
        """
        return self._remitter

    @remitter.setter
    def remitter(self, remitter):
        """Sets the remitter of this AccountTransaction.

        Account information of name, IBAN and BIC of the remitter.

        :param remitter: The remitter of this AccountTransaction.
        :type: AccountInformation
        """

        self._remitter = remitter

    @property
    def deptor(self):
        """Gets the deptor of this AccountTransaction.

        Account information of name, IBAN and BIC of the debtor

        :return: The deptor of this AccountTransaction.
        :rtype: AccountInformation
        """
        return self._deptor

    @deptor.setter
    def deptor(self, deptor):
        """Sets the deptor of this AccountTransaction.

        Account information of name, IBAN and BIC of the debtor

        :param deptor: The deptor of this AccountTransaction.
        :type: AccountInformation
        """

        self._deptor = deptor

    @property
    def creditor(self):
        """Gets the creditor of this AccountTransaction.

        includes the account information of the name, IBAN and BIC from the creditor

        :return: The creditor of this AccountTransaction.
        :rtype: AccountInformation
        """
        return self._creditor

    @creditor.setter
    def creditor(self, creditor):
        """Sets the creditor of this AccountTransaction.

        includes the account information of the name, IBAN and BIC from the creditor

        :param creditor: The creditor of this AccountTransaction.
        :type: AccountInformation
        """

        self._creditor = creditor

    @property
    def valuta_date(self):
        """Gets the valuta_date of this AccountTransaction.

        Availability date (yyyy-mm-dd). Could be an invalid date e.g. 2019-12-32

        :return: The valuta_date of this AccountTransaction.
        :rtype: str
        """
        return self._valuta_date

    @valuta_date.setter
    def valuta_date(self, valuta_date):
        """Sets the valuta_date of this AccountTransaction.

        Availability date (yyyy-mm-dd). Could be an invalid date e.g. 2019-12-32

        :param valuta_date: The valuta_date of this AccountTransaction.
        :type: str
        """

        self._valuta_date = valuta_date

    @property
    def direct_debit_creditor_id(self):
        """Gets the direct_debit_creditor_id of this AccountTransaction.

        Gives back the creditor identifier of an account transaction, if it is a direct debit.

        :return: The direct_debit_creditor_id of this AccountTransaction.
        :rtype: str
        """
        return self._direct_debit_creditor_id

    @direct_debit_creditor_id.setter
    def direct_debit_creditor_id(self, direct_debit_creditor_id):
        """Sets the direct_debit_creditor_id of this AccountTransaction.

        Gives back the creditor identifier of an account transaction, if it is a direct debit.

        :param direct_debit_creditor_id: The direct_debit_creditor_id of this AccountTransaction.
        :type: str
        """

        self._direct_debit_creditor_id = direct_debit_creditor_id

    @property
    def direct_debit_mandate_id(self):
        """Gets the direct_debit_mandate_id of this AccountTransaction.

        Gives back the mandateId of an account transaction, if it is a direct debit.

        :return: The direct_debit_mandate_id of this AccountTransaction.
        :rtype: str
        """
        return self._direct_debit_mandate_id

    @direct_debit_mandate_id.setter
    def direct_debit_mandate_id(self, direct_debit_mandate_id):
        """Sets the direct_debit_mandate_id of this AccountTransaction.

        Gives back the mandateId of an account transaction, if it is a direct debit.

        :param direct_debit_mandate_id: The direct_debit_mandate_id of this AccountTransaction.
        :type: str
        """

        self._direct_debit_mandate_id = direct_debit_mandate_id

    @property
    def end_to_end_reference(self):
        """Gets the end_to_end_reference of this AccountTransaction.

        Gives back the end-to-end-reference of an account transaction, if it is a direct debit.

        :return: The end_to_end_reference of this AccountTransaction.
        :rtype: str
        """
        return self._end_to_end_reference

    @end_to_end_reference.setter
    def end_to_end_reference(self, end_to_end_reference):
        """Sets the end_to_end_reference of this AccountTransaction.

        Gives back the end-to-end-reference of an account transaction, if it is a direct debit.

        :param end_to_end_reference: The end_to_end_reference of this AccountTransaction.
        :type: str
        """

        self._end_to_end_reference = end_to_end_reference

    @property
    def new_transaction(self):
        """Gets the new_transaction of this AccountTransaction.

        Shows whether the client has seen the account transaction in web.

        :return: The new_transaction of this AccountTransaction.
        :rtype: bool
        """
        return self._new_transaction

    @new_transaction.setter
    def new_transaction(self, new_transaction):
        """Sets the new_transaction of this AccountTransaction.

        Shows whether the client has seen the account transaction in web.

        :param new_transaction: The new_transaction of this AccountTransaction.
        :type: bool
        """

        self._new_transaction = new_transaction

    @property
    def remittance_info(self):
        """Gets the remittance_info of this AccountTransaction.

        remittance information of the transaction. This can be more then one line with a length of 35 symbols. The lines will be numbered in case of an already booked transaction.

        :return: The remittance_info of this AccountTransaction.
        :rtype: str
        """
        return self._remittance_info

    @remittance_info.setter
    def remittance_info(self, remittance_info):
        """Sets the remittance_info of this AccountTransaction.

        remittance information of the transaction. This can be more then one line with a length of 35 symbols. The lines will be numbered in case of an already booked transaction.

        :param remittance_info: The remittance_info of this AccountTransaction.
        :type: str
        """

        self._remittance_info = remittance_info

    @property
    def transaction_type(self):
        """Gets the transaction_type of this AccountTransaction.

        Definition of account transaction type.

        :return: The transaction_type of this AccountTransaction.
        :rtype: EnumText
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this AccountTransaction.

        Definition of account transaction type.

        :param transaction_type: The transaction_type of this AccountTransaction.
        :type: EnumText
        """

        self._transaction_type = transaction_type

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
        if issubclass(AccountTransaction, dict):
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
        if not isinstance(other, AccountTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTransaction):
            return True

        return self.to_dict() != other.to_dict()
