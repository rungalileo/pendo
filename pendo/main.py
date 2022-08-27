from typing import Dict, Optional

import requests

from pendo.const import PENDO_URL
from pendo.types import PendoResponse, PendoTrackEvent


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
        self, pendo_integration_key: str, extra_headers: Optional[Dict]
    ) -> None:
        self.pendo_integration_key = pendo_integration_key
        self.extra_headers = extra_headers

    def __headers(self) -> Dict:
        return {
            "Content-Type": "application/json; charset=utf-8",
            "x-pendo-integration-key": self.pendo_integration_key,
        }

    def headers(self) -> Dict:
        if self.extra_headers:
            return {**self.extra_headers, **self.__headers()}
        return self.__headers()

    def track(self, event: PendoTrackEvent, url: Optional[str] = None) -> PendoResponse:
        """Track an event.

        Args:
            event (PendoTrackEvent): The track event to be used as a POST request body.
            url (Optional[str]): The URL to send the POST request to. Defaults to the
                PENDO_URL constant. Defaults as None.

        Returns:
            PendoResponse: The response.
        """
        if url is None:
            url = PENDO_URL
        response = requests.post(url, json=event.dict(), headers=self.headers())
        return PendoResponse(status_code=response.status_code, body=response.json())
