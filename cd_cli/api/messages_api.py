from cd_cli.models import ListResourceDocument
from cd_cli.utils import get_colored_logger


class MessagesApi(object):
    def __init__(self, session):
        self._logger = get_colored_logger(__name__)
        self._session = session

    def get_document_list(self, paging_first=None, paging_count=None):
        """
        Get a list of documents for the customer.
        """
        # todo: check right scope to be checked
        scope = ["BANKING_RW", "BANKING_RO"]

        user = "user"
        path = f"/messages/clients/{user}/v2/documents"

        params = {}

        if paging_first is not None:
            params["paging-first"] = paging_first

        if paging_count is not None:
            params["paging-count"] = paging_count

        response, _ = self._session.comdirect_get(
            scope=scope,
            path=path,
            object_type=ListResourceDocument,
            additional_params=params,
        )

        return response

    def get_document(self, document):
        """
        Get document.
        """
        scope = ["MESSAGES_RO"]

        path = f"/messages/v2/documents/{document.document_id}"

        headers = {"Accept": document.mime_type}

        response, _ = self._session.comdirect_get(
            scope=scope,
            path=path,
            object_type=None,
            additional_headers=headers,
        )

        return response
