from typing import Dict, Optional, Union

import requests

from pendo.const import PENDO_URL
from pendo.types import PendoResponse, PendoTrackEvent

from .exc import PendoException


class Pendo:
    """Pendo.

    An unofficial Python package for server-side Pendo integrations.

    Attributes:
        pendo_integration_key (str): The Pendo integration key. A Pendo Admin can
            access this key in your app settings
            (Subscription Settings > Choose your App > App Details).
        extra_headers (Optional[Dict]): Extra headers to be sent with the request.
    """

    def __init__(
        self, pendo_integration_key: str, extra_headers: Optional[Dict] = dict()
    ) -> None:
        self.pendo_integration_key = pendo_integration_key
        self.extra_headers = extra_headers

    def __headers(self) -> Dict:
        """Private method to return the headers for the request.

        Returns:
            Dict: The private headers.
        """
        return {
            "Content-Type": "application/json; charset=utf-8",
            "x-pendo-integration-key": self.pendo_integration_key,
        }

    def headers(self) -> Dict:
        """Return the headers for the request.

        Returns:
            Dict: The headers.
        """
        if self.extra_headers:
            return {**self.extra_headers, **self.__headers()}
        return self.__headers()

    def track(
        self, event: Union[Dict, PendoTrackEvent], url: Optional[str] = None
    ) -> PendoResponse:
        """Track an event.

        Args:
            event (Union[Dict, PendoTrackEvent]): The track event to be used as a POST
                request body.
            url (Optional[str]): The URL to send the POST request to. Defaults to the
                PENDO_URL constant. Defaults as None.

        Returns:
            PendoResponse: The response.
        """
        if url is None:
            url = PENDO_URL
        if isinstance(event, dict):
            event = PendoTrackEvent(**event)
        response = requests.post(
            f"{url}/data/track", json=event.dict(), headers=self.headers()
        )
        if not response.ok:
            raise PendoException(
                f"Request exited with status {response.status_code}: {response.reason}"
            )
        return PendoResponse(status_code=response.status_code)
