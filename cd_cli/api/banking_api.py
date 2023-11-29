import json
from datetime import datetime

import requests
from cd_cli.deserialize import deserialize
from cd_cli.models import (
    ListResourceAccountBalance,
    ListResourceAccountTransaction,
    StandardErrorResponse,
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
        if not self._session.tokens_valid(scope="BANKING_RW"):
            self._logger.warning("Found no valid tokens. Cannot get account balances.")
            return

        client_id = "user"
        url = (
            self._session.base_url
            + f"/banking/clients/{client_id}/v2/accounts/balances"
        )

        headers = self._session.base_headers()

        response = requests.get(
            url=url, headers=headers, timeout=self._session.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not retrieve account balances. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            self.raw_responses["account_balances"] = response.json()
            account_balances = deserialize(response, ListResourceAccountBalance)
            self.account_balances = account_balances
            self._logger.info("Account balances were successfully retrieved.")
            self._logger.debug("Object: %s", account_balances)
            return

        self._logger.critical(
            "Could not retrieve account balances. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def get_account_transactions(
        self, account_id, start_date=None, end_date=None, paging_count=500
    ):
        """
        Get account transactions.
        """
        if not self._session.tokens_valid(scope="BANKING_RW"):
            self._logger.warning(
                "Found no valid tokens. Cannot get account transactions."
            )
            return

        url = self._session.base_url + f"/banking/v1/accounts/{account_id}/transactions"

        headers = self._session.base_headers()

        # 500 is max (as of 2023/11/27)
        # if this is not sufficient anymore, check what can be done with paging-first und paging-count parameters
        params = {"paging-count": paging_count}

        if start_date is not None:
            start_date_str = start_date.strftime("%Y-%m-%d")
            params["min-bookingDate"] = start_date_str

        if end_date is not None:
            end_date_str = end_date.strftime("%Y-%m-%d")
            params["max-bookingDate"] = end_date_str

        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=self._session.requests_timeout,
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not retrieve account transactions. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            self.raw_responses["account_transactions"] = response.json()
            account_transactions = deserialize(response, ListResourceAccountTransaction)
            self.account_transactions = account_transactions
            self._logger.info("Account transactions were successfully retrieved.")
            self._logger.debug("Object: %s", account_transactions)
            return

        self._logger.critical(
            "Could not retrieve account transactions. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )
