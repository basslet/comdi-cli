import requests
from cd_cli.deserialize import deserialize
from cd_cli.models import StandardErrorResponse, ListResourceDocument


from cd_cli.utils import get_colored_logger


class MessagesApi:
    def __init__(self, session):
        self._logger = get_colored_logger(__name__)
        self._session = session

        self.document_list = None

        self.raw_responses = {}

    def get_document_list(self, paging_count=None, paging_first=None):
        """
        Get a list of documents for the customer.
        """
        # todo: check right scope to be checked
        if not self._session.tokens_valid(scope="BANKING_RW"):
            self._logger.warning("Found no valid tokens. Cannot get documents list.")
            return

        user = "user"
        url = self._session.base_url + f"/messages/clients/{user}/v2/documents"

        headers = self._session.base_headers()

        params = {}

        if paging_count is not None:
            params["paging-count"] = paging_count
        if paging_first is not None:
            params["paging-first"] = paging_first

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
                "Could not retrieve documents list. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            self.raw_responses["document_list"] = response.json()
            document_list = deserialize(response, ListResourceDocument)
            self.document_list = document_list
            self._logger.info("Documents list was successfully retrieved.")
            self._logger.debug("Object: %s", document_list)
            return

        self._logger.critical(
            "Could not retrieve documents list. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def get_document(self, document):
        """
        Get document.
        """
        # todo: check if this is the right scope
        if not self._session.tokens_valid(scope="MESSAGES_RO"):
            self._logger.warning(
                "Found no valid tokens. Cannot get account transactions."
            )
            return

        url = self._session.base_url + f"/messages/v2/documents/{document.document_id}"

        headers = self._session.base_headers()
        headers["Accept"] = document.mime_type

        response = requests.get(
            url=url,
            headers=headers,
            timeout=self._session.requests_timeout,
        )

        # self._logger.debug("Response: %s", response.text)

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
            self._logger.info(
                'Document "%s" was successfully retrieved.', document.name
            )
            return response.content

        self._logger.critical(
            "Could not retrieve account transactions. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )
