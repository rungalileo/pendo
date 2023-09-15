import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

from requests import HTTPError, Session
from requests.compat import urljoin

from pendo.const import PENDO_URL
from pendo.types import PendoResponse, PendoTrackEvent

from .auth import PendoAuth
from .exc import PendoException


class Pendo(Session):
    """Pendo session.

    An unofficial Python package for server-side Pendo integrations.

    Attributes:
        auth (PendoAuth): The Pendo authentication handler.
        headers (Dict): The default headers to be sent with the request.
        host (str): The Pendo API URL. Defaults to PENDO_URL.
    """

    def __init__(
        self,
        pendo_integration_key: str,
        extra_headers: Optional[Dict] = dict(),
        url: str = PENDO_URL,
    ) -> None:
        """Pendo session constructor.

        Args:
            pendo_integration_key (str): The Pendo integration key.
            extra_headers (Optional[Dict], optional): Extra headers to add to each
                request. Defaults to dict().
            url (str, optional): The main URL used to access the Engage API corresponds
                to the region and web address that you use when logging into Pendo's UI.
                Defaults to PENDO_URL.
        """
        super().__init__()

        self.auth = PendoAuth(pendo_integration_key)
        self.headers.update(extra_headers)  # type: ignore[arg-type]
        self.host = url

    def request(  # type: ignore[override]
        self, method: str, path: str, *args: Any, **kwargs: Any
    ) -> PendoResponse:
        """Make a request.

        Args:
            method (str): The HTTP method.
            path (str): The endpoint to send the request to.
            *args: Positional arguments to be passed to the request.
            **kwargs: Keyword arguments to be passed to the request.

        Raises:
            PendoException: If the request fails.

        Returns:
            PendoResponse: The response.
        """
        path = urljoin(self.host, path)
        try:
            response = super().request(method, path, *args, **kwargs)
            response.raise_for_status()
        except HTTPError as exc:
            r = exc.response
            raise PendoException(
                f"Request exited with status {r.status_code}: {r.reason}"
            ) from exc

        try:
            data = response.json()
        except json.JSONDecodeError:
            data = {}

        return PendoResponse(status_code=HTTPStatus(response.status_code), data=data)

    def track(self, event: Union[Dict, PendoTrackEvent]) -> PendoResponse:
        """Track an event.

        Args:
            event (Union[Dict, PendoTrackEvent]): The track event to be used as a POST
                request body.

        Returns:
            PendoResponse: The response.
        """
        if isinstance(event, dict):
            event = PendoTrackEvent(**event)

        return self.post(  # type: ignore[return-value]
            "data/track", json=event.model_dump()
        )
