import socket
import time
from typing import Any, Generator

import pytest

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
def pendo_track_event_with_props_and_context() -> PendoTrackEvent:
    return PendoTrackEvent(
        event="TestEvent",
        visitorId="TestVisitorId",
        accountId="TestAccountId",
        timestamp=int(time.time() * 1000),
        properties={"test": "test"},
        context={"test": "test"},
    )


def guard(*args: Any, **kwargs: Any) -> None:
    raise Exception(
        "No external network access allowed during tests."
    )  # pragma: no cover


socket.socket = guard  # type: ignore
