import json
import uuid
from datetime import datetime
from time import sleep

import requests

from cd_cli.utils import get_colored_logger
from cd_cli.deserialize import deserialize
from cd_cli.models import StandardErrorResponse, Tokens, Session, AuthenticationInfo


class SessionApi:
    def __init__(self, client_id, client_secret, username, password):
        self._logger = get_colored_logger(__name__)
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._password = password

        self._oauth_url = "https://api.comdirect.de"
        self.base_url = "https://api.comdirect.de/api"

        self._session_timeout = 300
        self.requests_timeout = 30

        self.session_id = self._create_session_id()

        self.tokens = None
        self.session = None
        self.authentication_info = None

    def _request_limiter(self):
        """
        Limit the API requests.

        The comdirect REST API allows 10 requests per second.
        """
        sleep(0.1)

    def _create_session_id(self):
        """
        Create a Session-ID.

        The Session-ID represents a user session. The client
        must generate a corresponding session ID before the first request
        before the first request and send it in all subsequent requests. The
        definition of a user session depends on the client. A
        client in the form of a mobile app starts the user session by
        the start of the app and ends it when the app is closed.
        app.

        Returns:
            str: A Session-ID.
        """
        # create uuid without dashes
        ret = str(uuid.uuid4()).replace("-", "")
        self._logger.debug("Created Session-ID: %s", ret)
        return ret

    def _create_request_id(self):
        """
        Create a Request-ID.

        The Request-ID makes the request unique within the user session
        and can, for example, consist of a timestamp in the format HHmmssSSS.

        Returns:
            str: A Request-ID.
        """

        ret = datetime.now().strftime("%H%M%S%f")[:-3]
        self._logger.debug("Created Request-ID: %s", ret)
        return ret

    def create_client_request_id(self):
        """
        Create a Client Requiest-ID.

        The Client Request-ID must be transmitted by clients
        in the HTTP header "x-http-request-info".

        Returns:
            str: A Client Request-ID.
        """
        request_id = self._create_request_id()
        ret = json.dumps(
            {
                "clientRequestId": {
                    "sessionId": f"{self.session_id}",
                    "requestId": f"{request_id}",
                }
            }
        )
        self._logger.debug("Client Request-ID: %s", ret)
        return ret

    def base_headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.tokens.access_token}",
            "x-http-request-info": self.create_client_request_id(),
        }

    def tokens_valid(self, scope=None):
        """
        Check if tokens are valid.

        Tokens must exist and must be valid for at least 60s.

        Args:
            scope (optional): Access right that the access token must have. Defaults to None.

        Returns:
            bool: Validity of the tokens.
        """
        if self.tokens is None:
            self._logger.debug(
                "Cannot check validity of tokens since no tokens are available."
            )
            return False
        current_time = datetime.now()
        expire_in_seconds = round((self.tokens.expires - current_time).total_seconds())
        if expire_in_seconds <= 0:
            self._logger.critical("Tokens expired %ss ago.", abs(expire_in_seconds))
            return False
        if expire_in_seconds <= 60:
            self.refresh_tokens(skip_check=True)
        if scope is not None:
            valid_scope = False
            for s in scope:
                if s in self.tokens.scope:
                    valid_scope = True
                    break

            if valid_scope is False:
                self._logger.critical(
                    "Required access right(s) (%s) not in scope of tokens (%s).",
                    ", ".join(scope),
                    self.tokens.scope,
                )
                return False

        self._logger.debug("Tokens are valid. They expire in %ss.", expire_in_seconds)
        return True

    def request_tokens_using_password(self):
        """
        Request OAuth2 tokens.

        Use for the "OAuth2 Resource Owner Password Credentials Flow".
        """
        if self.tokens_valid():
            self._logger.info("Valid tokens available. Skip.")
            return

        url = self._oauth_url + "/oauth/token"
        data = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "username": self._username,
            "password": self._password,
            "grant_type": "password",
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self._request_limiter()
        response = requests.post(
            url=url, data=data, headers=headers, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not retrieve OAuth2 tokens. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            tokens = deserialize(response, Tokens)
            self.tokens = tokens
            self._logger.info("Tokens were successfully retrieved.")
            self._logger.debug("Object: %s", tokens)
            return

        self._logger.critical(
            "Could not retrieve OAuth2 tokens. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def request_tokens_using_cd_secondary(self):
        """
        Request OAuth2 tokens.

        Use for the "CD Secondary Flow".
        """
        if not self.tokens_valid():
            self._logger.warning(
                'Found no valid tokens. Cannot request tokens for the "CD Secondary Flow"'
            )
            return

        url = self._oauth_url + "/oauth/token"
        data = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "token": self.tokens.access_token,
            "grant_type": "cd_secondary",
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self._request_limiter()
        response = requests.post(
            url=url, data=data, headers=headers, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                'Could not retrieve OAuth2 tokens for the "CD Secondary Flow". Status code %s. '
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            tokens = deserialize(response, Tokens)
            self.tokens = tokens
            self._logger.info("Tokens were successfully retrieved.")
            self._logger.debug("Object: %s", tokens)
            self._logger.info("You are fully logged in.")
            return

        self._logger.critical(
            'Could not retrieve OAuth2 tokens for the "CD Secondary Flow". Status code %s.',
            response.status_code,
        )

    def refresh_tokens(self, skip_check=False):
        """
        Refresh OAuth2 tokens.
        """
        if not skip_check:
            if not self.tokens_valid():
                self._logger.warning("No valid tokens. Refresh not possible.")
                return

        url = self._oauth_url + "/oauth/token"
        data = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.tokens.refresh_token,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self._request_limiter()
        response = requests.post(
            url=url, data=data, headers=headers, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not refresh OAuth2 tokens. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            tokens = deserialize(response, Tokens)
            self.tokens = tokens
            self._logger.info("Tokens were successfully refreshed.")
            self._logger.debug("Object: %s", tokens)
            return

        self._logger.critical(
            "Could not refresh OAuth2 tokens. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def revoke_tokens(self):
        """
        Revoke OAuth2 tokens.
        """
        if not self.tokens_valid():
            self._logger.warning(
                "There are no tokens that can be revoked or they have already expired."
            )
            return

        url = self._oauth_url + "/oauth/revoke"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.tokens.access_token}",
        }
        self._request_limiter()
        response = requests.delete(
            url=url, headers=headers, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not revoke tokens. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 204:
            self.tokens = None
            self._logger.info("Tokens were successfully revoked.")
            return

        self._logger.critical(
            "Could not revoke tokens. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def get_session(self):
        """
        Get a session object.

        In order to request a session TAN, the session object
        must first be requested.

        """
        if self.session is not None:
            self._logger.warning("Found session. Cannot get new session.")
            return

        if not self.tokens_valid(scope="TWO_FACTOR"):
            self._logger.warning("Found no valid tokens. Cannot get session.")
            return

        client_id = "user"
        url = self.base_url + f"/session/clients/{client_id}/v1/sessions"

        headers = self.base_headers()

        self._request_limiter()
        response = requests.get(url=url, headers=headers, timeout=self.requests_timeout)

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not get session. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            session = deserialize(response.json()[0], Session)
            self.session = session
            self._logger.info("Session object was successfully requested.")
            self._logger.debug("Object: %s", session)
            return

        self._logger.critical(
            "Could not get session. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def validate_session(self):
        """
        Request TAN challange.

        A TAN challenge is requested for the session object.

        Raises:
            RuntimeError: In case the TAN challange request failed.

        Returns:
            TAN method and challenge
        """
        if self.session is None:
            self._logger.warning("Found no session. Cannot validate.")
            return

        client_id = "user"
        session_id = self.session.identifier
        url = (
            self.base_url
            + f"/session/clients/{client_id}/v1/sessions/{session_id}/validate"
        )
        self._logger.debug(url)

        headers = self.base_headers()

        data = json.dumps(
            {
                "identifier": session_id,
                "sessionTanActive": "True",
                "activated2FA": "True",
            }
        )

        self._request_limiter()
        response = requests.post(
            url=url, headers=headers, data=data, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not validate session. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 201:
            session = deserialize(response.json(), Session)
            self.session = session
            self._logger.debug("Session updated.")
            self._logger.debug("Object: %s", self.session)

            self.authentication_info = deserialize(
                json.loads(response.headers["x-once-authentication-info"]),
                AuthenticationInfo,
            )
            self._logger.info("TAN challange was successfully requested.")
            self._logger.debug("Object: %s", self.authentication_info)
            return

        self._logger.critical(
            "Could not validate session. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def activate_session_tan(self, tan=None):
        """
        Activate session TAN.

        Args:
            tan: The TAN. Defaults to None. (Only valid for P_TAN_PUSH method.)
        """
        if self.authentication_info is None:
            self._logger.warning(
                "Found no valid challenge. Cannot activate session TAN."
            )
            return
        if tan is None and self.authentication_info.typ != "P_TAN_PUSH":
            self._logger.warning(
                "You have not provided a TAN for method %s. Cannot activate session TAN.",
                self.authentication_info.typ,
            )
            return

        client_id = "user"
        session_id = self.session.identifier
        url = self.base_url + f"/session/clients/{client_id}/v1/sessions/{session_id}"

        headers = self.base_headers()

        headers["x-once-authentication-info"] = json.dumps(
            {"id": f"{self.authentication_info.authentication_info_id}"}
        )

        if tan is not None:
            headers["x-once-authentication"] = f"{tan}"

        data = json.dumps(
            {
                "identifier": session_id,
                "sessionTanActive": "true",
                "activated2FA": "true",
            }
        )
        self._request_limiter()
        response = requests.patch(
            url=url, headers=headers, data=data, timeout=self.requests_timeout
        )

        self._logger.debug("Response: %s", response.text)

        if response.status_code == 422:
            standard_error_response = deserialize(response, StandardErrorResponse)
            self._logger.critical(
                "Could not activate session TAN. Status code %s. "
                + 'Error: "%s" / Message: "%s"',
                standard_error_response.code,
                standard_error_response.messages[0].key,
                standard_error_response.messages[0].message,
            )
            return

        if response.status_code == 200:
            session = deserialize(response.json(), Session)
            self.session = session
            self._logger.debug("Session updated.")
            self._logger.debug("Object: %s", self.session)
            self._logger.info("Session TAN was successfully activated!")
            return

        self._logger.critical(
            "Could not activate session TAN. Status code %s. "
            + 'Error: "%s" / Error description: "%s"',
            response.status_code,
            response.json()["error"] or "n.a.",
            response.json()["error_description"] or "n.a.",
        )

    def comdirect_get(
        self,
        path,
        object_type,
        additional_params=None,
        additional_headers=None,
        scope=None,
    ):
        """
        Send a get request to comdirect REST API.
        """

        if scope is not None:
            if not self.tokens_valid(scope=scope):
                return None, None
        else:
            if not self.tokens_valid():
                return None, None

        url = self.base_url + path

        headers = self.base_headers()
        if additional_headers is not None:
            headers.update(additional_headers)

        params = {}
        if additional_params is not None:
            params.update(additional_params)

        self._request_limiter()
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=self.requests_timeout,
        )

        if "x-http-response-info" in response.headers:
            standard_error_response = deserialize(
                json.loads(response.headers["x-http-response-info"]),
                StandardErrorResponse,
            )

            for message in standard_error_response.messages:
                if message.severity == "INFO":
                    self._logger.debug(
                        "%s: %s - %s", message.severity, message.key, message.message
                    )
                else:
                    self._logger.warning(
                        "%s: %s - %s", message.severity, message.key, message.message
                    )

        # self._logger.debug("Response: %s", response.text)

        if response.status_code == 200:
            if object_type is None:
                return response.content, response.text
            else:
                obj = deserialize(response, object_type)
                return obj, response.json()

        self._logger.critical(
            "Request failed with tatus code %s.", response.status_code
        )
        return None, None
