import pprint


class Execution(object):
    # Attributes:
    #   attribute_types (dict): The key is attribute name
    #                           and the value is attribute type.
    #   attribute_map (dict):   The key is attribute name
    #                           and the value is json key in definition.
    attribute_types = {
        "execution_id": "str",
        "execution_number": "int",
        "executed_quantity": "AmountValue",
        "execution_price": "AmountValue",
        "execution_timestamp": "TimestampString",
    }

    attribute_map = {
        "execution_id": "executionId",
        "execution_number": "executionNumber",
        "executed_quantity": "executedQuantity",
        "execution_price": "executionPrice",
        "execution_timestamp": "executionTimestamp",
    }

    def __init__(
        self,
        execution_id=None,
        execution_number=None,
        executed_quantity=None,
        execution_price=None,
        execution_timestamp=None,
    ):
        """Execution"""

        self._execution_id = None
        self._execution_number = None
        self._executed_quantity = None
        self._execution_price = None
        self._execution_timestamp = None

        if execution_id is not None:
            self.execution_id = execution_id
        if execution_number is not None:
            self.execution_number = execution_number
        if executed_quantity is not None:
            self.executed_quantity = executed_quantity
        if execution_price is not None:
            self.execution_price = execution_price
        if execution_timestamp is not None:
            self.execution_timestamp = execution_timestamp

    @property
    def execution_id(self):
        """Gets the execution_id of this Execution.

        Execution ID (UUID)

        :return: The execution_id of this Execution.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this Execution.

        Execution ID (UUID)

        :param execution_id: The execution_id of this Execution.
        :type: str
        """
        if execution_id is not None and len(execution_id) > 40:
            raise ValueError(
                "Invalid value for `execution_id`, length must be less than or equal to `40`"
            )
        if execution_id is not None and len(execution_id) < 0:
            raise ValueError(
                "Invalid value for `execution_id`, length must be greater than or equal to `0`"
            )

        self._execution_id = execution_id

    @property
    def execution_number(self):
        """Gets the execution_number of this Execution.

        Position (by time) of the execution of an order

        :return: The execution_number of this Execution.
        :rtype: int
        """
        return self._execution_number

    @execution_number.setter
    def execution_number(self, execution_number):
        """Sets the execution_number of this Execution.

        Position (by time) of the execution of an order

        :param execution_number: The execution_number of this Execution.
        :type: int
        """

        self._execution_number = execution_number

    @property
    def executed_quantity(self):
        """Gets the executed_quantity of this Execution.

        Quantity of executed units or nominal amount

        :return: The executed_quantity of this Execution.
        :rtype: AmountValue
        """
        return self._executed_quantity

    @executed_quantity.setter
    def executed_quantity(self, executed_quantity):
        """Sets the executed_quantity of this Execution.

        Quantity of executed units or nominal amount

        :param executed_quantity: The executed_quantity of this Execution.
        :type: AmountValue
        """

        self._executed_quantity = executed_quantity

    @property
    def execution_price(self):
        """Gets the execution_price of this Execution.

        Execution price

        :return: The execution_price of this Execution.
        :rtype: AmountValue
        """
        return self._execution_price

    @execution_price.setter
    def execution_price(self, execution_price):
        """Sets the execution_price of this Execution.

        Execution price

        :param execution_price: The execution_price of this Execution.
        :type: AmountValue
        """

        self._execution_price = execution_price

    @property
    def execution_timestamp(self):
        """Gets the execution_timestamp of this Execution.

        Date/timestamp of the order entry in UTC in the following format: (MiFID II) YYYY-MM-DDThh:mm:ss,ffffff+zz

        :return: The execution_timestamp of this Execution.
        :rtype: TimestampString
        """
        return self._execution_timestamp

    @execution_timestamp.setter
    def execution_timestamp(self, execution_timestamp):
        """Sets the execution_timestamp of this Execution.

        Date/timestamp of the order entry in UTC in the following format: (MiFID II) YYYY-MM-DDThh:mm:ss,ffffff+zz

        :param execution_timestamp: The execution_timestamp of this Execution.
        :type: TimestampString
        """

        self._execution_timestamp = execution_timestamp

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
        if issubclass(Execution, dict):
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
        if not isinstance(other, Execution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Execution):
            return True

        return self.to_dict() != other.to_dict()
