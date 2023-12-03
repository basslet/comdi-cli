"""
A BankingApi class.
"""
from cd_cli.models import (
    ListResourceAccountBalance,
    ListResourceAccountTransaction,
)

from cd_cli.utils import get_colored_logger


class BankingApi:
    def __init__(self, session):
        self._logger = get_colored_logger(__name__)
        self._session = session
        self.account_balances = None
        self.account_transactions = None
        self.raw_responses = {}

    def get_account_balances(self):
        """
        Get account balances.
        """
        scope = ["BANKING_RW", "BANKING_RO"]

        client_id = "user"
        path = f"/banking/clients/{client_id}/v2/accounts/balances"

        response_obj, response_json = self._session.comdirect_get(
            scope=scope,
            path=path,
            object_type=ListResourceAccountBalance,
        )

        return response_obj, response_json

    def get_account_transactions(
        self, account_id, start_date=None, end_date=None, paging_count=None
    ):
        """
        Get account transactions.
        """
        scope = ["BANKING_RW", "BANKING_RO"]

        path = f"/banking/v1/accounts/{account_id}/transactions"

        params = {}

        if paging_count is not None:
            params["paging-count"] = paging_count

        if start_date is not None:
            start_date_str = start_date.strftime("%Y-%m-%d")
            params["min-bookingDate"] = start_date_str

        if end_date is not None:
            end_date_str = end_date.strftime("%Y-%m-%d")
            params["max-bookingDate"] = end_date_str

        response_obj, response_json = self._session.comdirect_get(
            scope=scope,
            path=path,
            object_type=ListResourceAccountTransaction,
            additional_params=params,
        )

        return response_obj, response_json
