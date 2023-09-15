import time
from http import HTTPStatus
from typing import Any, Generator

import pytest
from requests import Response

from pendo import Pendo
from pendo.types import PendoTrackEvent


@pytest.fixture(scope="function")
def pendo_client() -> Generator:
    pendo = Pendo(pendo_integration_key="test", extra_headers={})
    yield pendo


@pytest.fixture(scope="function")
def pendo_client_extra_headers() -> Generator:
    pendo = Pendo(pendo_integration_key="test", extra_headers={"x-test-header": "test"})
    yield pendo


@pytest.fixture()
def pendo_track_event() -> PendoTrackEvent:
    return PendoTrackEvent(
        event="TestEvent",
        visitorId="TestVisitorId",
        accountId="TestAccountId",
        timestamp=int(time.time() * 1000),
    )


@pytest.fixture()
def pendo_track_event_with_props_and_context(
    pendo_track_event: PendoTrackEvent,
) -> PendoTrackEvent:
    return PendoTrackEvent(
        event=pendo_track_event.event,
        visitorId=pendo_track_event.visitorId,
        accountId=pendo_track_event.accountId,
        timestamp=pendo_track_event.timestamp,
        properties={"test": "test"},
        context={"test": "test"},
    )


@pytest.fixture
def ok_request(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_request(*args: Any, **kwargs: Any) -> Response:
        response = Response()
        response.status_code = HTTPStatus.OK

        return response

    monkeypatch.setattr("requests.Session.request", mock_request)


@pytest.fixture
def error_request(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_request(*args: Any, **kwargs: Any) -> Response:
        response = Response()
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        response.reason = "Internal Server Error"

        return response

    monkeypatch.setattr("requests.Session.request", mock_request)


@pytest.fixture(autouse=True)
def guard_socket(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_socket(*args: Any, **kwargs: Any) -> None:
        raise Exception("No external network access allowed during tests.")

    monkeypatch.setattr("socket.socket", mock_socket)
