import base64

from cd_cli.api import BankingApi, MessagesApi, SessionApi
from cd_cli.utils import get_colored_logger


class ComdirectApiClient(object):
    def __init__(self, client_id, client_secret, username, password):
        self._logger = get_colored_logger(__name__)
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password

        self.session = None
        self.banking = None
        self.messages = None

    def login(self):
        if self.session is not None:
            self._logger.warning("Runnig session found. New login not possible.")
            return

        cd_session = SessionApi(
            self._client_id, self._client_secret, self._username, self._password
        )
        cd_session.request_tokens_using_password()
        cd_session.get_session()
        cd_session.validate_session()

        if cd_session.authentication_info.typ == "M_TAN":
            print()
            tan = input("Enter TAN (sent to your mobile phone): ")
            print()
            cd_session.activate_session_tan(tan)
        elif cd_session.authentication_info.typ == "P_TAN":
            with open("phototan.png", "wb") as file:
                file.write(base64.b64decode(cd_session.authentication_info.challenge))
            print()
            tan = input('Enter TAN (check "phototan.png"): ')
            print()
            cd_session.activate_session_tan(tan)
        elif cd_session.authentication_info.typ == "P_TAN_PUSH":
            print()
            input("Press ENTER when you have confirmed the login in the photoTAN app.")
            print()
            cd_session.activate_session_tan()

        cd_session.request_tokens_using_cd_secondary()

        self.session = cd_session

    def logout(self):
        if self.session is None:
            self._logger.warning("No open session. Logout not possible.")
        else:
            self.session.revoke_tokens()

    def get_account_balances(self):
        if self.banking is not None:
            self._logger.debug("BankingAPI object exists. Skip instantiation.")
        else:
            cd_banking = BankingApi(self.session)
            self.banking = cd_banking

        return self.banking.get_account_balances()

    def get_account_transactions(
        self, account_id, start_date=None, end_date=None, paging_count=None
    ):
        if self.banking is not None:
            self._logger.debug("BankingAPI object exists. Skip instantiation.")
        else:
            cd_banking = BankingApi(self.session)
            self.banking = cd_banking

        return self.banking.get_account_transactions(
            account_id,
            start_date=start_date,
            end_date=end_date,
            paging_count=paging_count,
        )

    def get_document_list(self, **kwargs):
        if self.messages is not None:
            self._logger.debug("MessagesAPI object exitsts. Skip instantiation.")
        else:
            cd_messages = MessagesApi(self.session)
            self.messages = cd_messages

        return self.messages.get_document_list(**kwargs)

    def get_document(self, document):
        if self.messages is not None:
            self._logger.debug("MessagesAPI object exitsts. Skip instantiation.")
        else:
            cd_messages = MessagesApi(self.session)
            self.messages = cd_messages

        return self.messages.get_document(document)
