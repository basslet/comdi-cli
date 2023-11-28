import pprint


class InstallmentLoan(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "installment_loan_id": "str",
        "product_display_id": "str",
        "credit_amount": "AmountValue",
        "net_credit_amount": "AmountValue",
        "paid_out_amount": "AmountValue",
        "installment_amount": "AmountValue",
        "contract_period_in_months": "int",
        "effective_interest": "str",
        "nominal_interest": "str",
        "contract_conclusion_date": "str",
    }

    attribute_map = {
        "installment_loan_id": "installmentLoanId",
        "product_display_id": "productDisplayId",
        "credit_amount": "creditAmount",
        "net_credit_amount": "netCreditAmount",
        "paid_out_amount": "paidOutAmount",
        "installment_amount": "installmentAmount",
        "contract_period_in_months": "contractPeriodInMonths",
        "effective_interest": "effectiveInterest",
        "nominal_interest": "nominalInterest",
        "contract_conclusion_date": "contractConclusionDate",
    }

    def __init__(
        self,
        installment_loan_id=None,
        product_display_id=None,
        credit_amount=None,
        net_credit_amount=None,
        paid_out_amount=None,
        installment_amount=None,
        contract_period_in_months=None,
        effective_interest=None,
        nominal_interest=None,
        contract_conclusion_date=None,
    ):
        """InstallmentLoan"""

        self._installment_loan_id = None
        self._product_display_id = None
        self._credit_amount = None
        self._net_credit_amount = None
        self._paid_out_amount = None
        self._installment_amount = None
        self._contract_period_in_months = None
        self._effective_interest = None
        self._nominal_interest = None
        self._contract_conclusion_date = None

        if installment_loan_id is not None:
            self.installment_loan_id = installment_loan_id
        if product_display_id is not None:
            self.product_display_id = product_display_id
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if net_credit_amount is not None:
            self.net_credit_amount = net_credit_amount
        if paid_out_amount is not None:
            self.paid_out_amount = paid_out_amount
        if installment_amount is not None:
            self.installment_amount = installment_amount
        if contract_period_in_months is not None:
            self.contract_period_in_months = contract_period_in_months
        if effective_interest is not None:
            self.effective_interest = effective_interest
        if nominal_interest is not None:
            self.nominal_interest = nominal_interest
        if contract_conclusion_date is not None:
            self.contract_conclusion_date = contract_conclusion_date

    @property
    def installment_loan_id(self):
        """Gets the installment_loan_id of this InstallmentLoan.

        Installment loan identifier (UUID).

        :return: The installment_loan_id of this InstallmentLoan.
        :rtype: str
        """
        return self._installment_loan_id

    @installment_loan_id.setter
    def installment_loan_id(self, installment_loan_id):
        """Sets the installment_loan_id of this InstallmentLoan.

        Installment loan identifier (UUID).

        :param installment_loan_id: The installment_loan_id of this InstallmentLoan.
        :type: str
        """

        self._installment_loan_id = installment_loan_id

    @property
    def product_display_id(self):
        """Gets the product_display_id of this InstallmentLoan.

        SWK number of the installment loan.

        :return: The product_display_id of this InstallmentLoan.
        :rtype: str
        """
        return self._product_display_id

    @product_display_id.setter
    def product_display_id(self, product_display_id):
        """Sets the product_display_id of this InstallmentLoan.

        SWK number of the installment loan.

        :param product_display_id: The product_display_id of this InstallmentLoan.
        :type: str
        """

        self._product_display_id = product_display_id

    @property
    def credit_amount(self):
        """Gets the credit_amount of this InstallmentLoan.

        Approved loan amount of the initial conclusion of the loan in EUR, including residual debt insurance and interest.

        :return: The credit_amount of this InstallmentLoan.
        :rtype: AmountValue
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this InstallmentLoan.

        Approved loan amount of the initial conclusion of the loan in EUR, including residual debt insurance and interest.

        :param credit_amount: The credit_amount of this InstallmentLoan.
        :type: AmountValue
        """

        self._credit_amount = credit_amount

    @property
    def net_credit_amount(self):
        """Gets the net_credit_amount of this InstallmentLoan.

        Approved loan amount of the initial conclusion of the loan in EUR, before residual debt insurance and interest.

        :return: The net_credit_amount of this InstallmentLoan.
        :rtype: AmountValue
        """
        return self._net_credit_amount

    @net_credit_amount.setter
    def net_credit_amount(self, net_credit_amount):
        """Sets the net_credit_amount of this InstallmentLoan.

        Approved loan amount of the initial conclusion of the loan in EUR, before residual debt insurance and interest.

        :param net_credit_amount: The net_credit_amount of this InstallmentLoan.
        :type: AmountValue
        """

        self._net_credit_amount = net_credit_amount

    @property
    def paid_out_amount(self):
        """Gets the paid_out_amount of this InstallmentLoan.

        Paid out amount of the approved loan, can include additions or deductions for residual debt insurance or interest.

        :return: The paid_out_amount of this InstallmentLoan.
        :rtype: AmountValue
        """
        return self._paid_out_amount

    @paid_out_amount.setter
    def paid_out_amount(self, paid_out_amount):
        """Sets the paid_out_amount of this InstallmentLoan.

        Paid out amount of the approved loan, can include additions or deductions for residual debt insurance or interest.

        :param paid_out_amount: The paid_out_amount of this InstallmentLoan.
        :type: AmountValue
        """

        self._paid_out_amount = paid_out_amount

    @property
    def installment_amount(self):
        """Gets the installment_amount of this InstallmentLoan.

        Amount of the installment loan in EUR.

        :return: The installment_amount of this InstallmentLoan.
        :rtype: AmountValue
        """
        return self._installment_amount

    @installment_amount.setter
    def installment_amount(self, installment_amount):
        """Sets the installment_amount of this InstallmentLoan.

        Amount of the installment loan in EUR.

        :param installment_amount: The installment_amount of this InstallmentLoan.
        :type: AmountValue
        """

        self._installment_amount = installment_amount

    @property
    def contract_period_in_months(self):
        """Gets the contract_period_in_months of this InstallmentLoan.

        Runtime of the installment loan in months.

        :return: The contract_period_in_months of this InstallmentLoan.
        :rtype: int
        """
        return self._contract_period_in_months

    @contract_period_in_months.setter
    def contract_period_in_months(self, contract_period_in_months):
        """Sets the contract_period_in_months of this InstallmentLoan.

        Runtime of the installment loan in months.

        :param contract_period_in_months: The contract_period_in_months of this InstallmentLoan.
        :type: int
        """

        self._contract_period_in_months = contract_period_in_months

    @property
    def effective_interest(self):
        """Gets the effective_interest of this InstallmentLoan.

        Effective interest rate.

        :return: The effective_interest of this InstallmentLoan.
        :rtype: str
        """
        return self._effective_interest

    @effective_interest.setter
    def effective_interest(self, effective_interest):
        """Sets the effective_interest of this InstallmentLoan.

        Effective interest rate.

        :param effective_interest: The effective_interest of this InstallmentLoan.
        :type: str
        """

        self._effective_interest = effective_interest

    @property
    def nominal_interest(self):
        """Gets the nominal_interest of this InstallmentLoan.

        Nominal interest rate.

        :return: The nominal_interest of this InstallmentLoan.
        :rtype: str
        """
        return self._nominal_interest

    @nominal_interest.setter
    def nominal_interest(self, nominal_interest):
        """Sets the nominal_interest of this InstallmentLoan.

        Nominal interest rate.

        :param nominal_interest: The nominal_interest of this InstallmentLoan.
        :type: str
        """

        self._nominal_interest = nominal_interest

    @property
    def contract_conclusion_date(self):
        """Gets the contract_conclusion_date of this InstallmentLoan.

        Date of conclusion of the installment loan.

        :return: The contract_conclusion_date of this InstallmentLoan.
        :rtype: str
        """
        return self._contract_conclusion_date

    @contract_conclusion_date.setter
    def contract_conclusion_date(self, contract_conclusion_date):
        """Sets the contract_conclusion_date of this InstallmentLoan.

        Date of conclusion of the installment loan.

        :param contract_conclusion_date: The contract_conclusion_date of this InstallmentLoan.
        :type: str
        """

        self._contract_conclusion_date = contract_conclusion_date

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
        if issubclass(InstallmentLoan, dict):
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
        if not isinstance(other, InstallmentLoan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstallmentLoan):
            return True

        return self.to_dict() != other.to_dict()
