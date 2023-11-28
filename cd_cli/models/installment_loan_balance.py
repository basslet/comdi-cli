import pprint


class InstallmentLoanBalance(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "installment_loan_id": "str",
        "installment_loan": "InstallmentLoan",
        "balance": "AmountValue",
    }

    attribute_map = {
        "installment_loan_id": "installmentLoanId",
        "installment_loan": "installmentLoan",
        "balance": "balance",
    }

    def __init__(self, installment_loan_id=None, installment_loan=None, balance=None):
        """InstallmentLoanBalance"""

        self._installment_loan_id = None
        self._installment_loan = None
        self._balance = None

        if installment_loan_id is not None:
            self.installment_loan_id = installment_loan_id
        if installment_loan is not None:
            self.installment_loan = installment_loan
        if balance is not None:
            self.balance = balance

    @property
    def installment_loan_id(self):
        """Gets the installment_loan_id of this InstallmentLoanBalance.

        Installment loan identifier (UUID).

        :return: The installment_loan_id of this InstallmentLoanBalance.
        :rtype: str
        """
        return self._installment_loan_id

    @installment_loan_id.setter
    def installment_loan_id(self, installment_loan_id):
        """Sets the installment_loan_id of this InstallmentLoanBalance.

        Installment loan identifier (UUID).

        :param installment_loan_id: The installment_loan_id of this InstallmentLoanBalance.
        :type: str
        """

        self._installment_loan_id = installment_loan_id

    @property
    def installment_loan(self):
        """Gets the installment_loan of this InstallmentLoanBalance.

        Master data of the installment loan.

        :return: The installment_loan of this InstallmentLoanBalance.
        :rtype: InstallmentLoan
        """
        return self._installment_loan

    @installment_loan.setter
    def installment_loan(self, installment_loan):
        """Sets the installment_loan of this InstallmentLoanBalance.

        Master data of the installment loan.

        :param installment_loan: The installment_loan of this InstallmentLoanBalance.
        :type: InstallmentLoan
        """

        self._installment_loan = installment_loan

    @property
    def balance(self):
        """Gets the balance of this InstallmentLoanBalance.

        Current balance of the installment loan in EUR, including residual debt insurance and interest.

        :return: The balance of this InstallmentLoanBalance.
        :rtype: AmountValue
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this InstallmentLoanBalance.

        Current balance of the installment loan in EUR, including residual debt insurance and interest.

        :param balance: The balance of this InstallmentLoanBalance.
        :type: AmountValue
        """

        self._balance = balance

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
        if issubclass(InstallmentLoanBalance, dict):
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
        if not isinstance(other, InstallmentLoanBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstallmentLoanBalance):
            return True

        return self.to_dict() != other.to_dict()
