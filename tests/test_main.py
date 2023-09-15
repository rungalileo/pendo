import time
from http import HTTPStatus

import pytest

from pendo import Pendo
from pendo.exc import PendoException
from pendo.types import PendoTrackEvent


def test_live_pendo(pendo_client: Pendo, pendo_track_event: PendoTrackEvent) -> None:
    with pytest.raises(Exception):
        pendo_client.track(event=pendo_track_event)


@pytest.mark.usefixtures("ok_request")
def test_pendo(pendo_client: Pendo, pendo_track_event: PendoTrackEvent) -> None:
    response = pendo_client.track(event=pendo_track_event)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("error_request")
def test_pendo_catch_exception(
    pendo_client: Pendo, pendo_track_event: PendoTrackEvent
) -> None:
    with pytest.raises(PendoException) as exc_info:
        pendo_client.track(event=pendo_track_event)
    assert (
        exc_info.value.args[0]
        == "Request exited with status 500: Internal Server Error"
    )


@pytest.mark.usefixtures("ok_request")
def test_pendo_with_extra_headers(
    pendo_client_extra_headers: Pendo, pendo_track_event: PendoTrackEvent
) -> None:
    response = pendo_client_extra_headers.track(event=pendo_track_event)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("ok_request")
def test_pendo_track_event_with_props_and_context(
    pendo_client: Pendo, pendo_track_event_with_props_and_context: PendoTrackEvent
) -> None:
    response = pendo_client.track(event=pendo_track_event_with_props_and_context)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("ok_request")
def test_pendo_track_event_dict_input(pendo_client: Pendo) -> None:
    response = pendo_client.track(
        {
            "event": "TestEvent",
            "visitorId": "TestVisitorId",
            "accountId": "TestAccountId",
            "timestamp": int(time.time() * 1000),
        }
    )
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures("ok_request")
def test_pendo_track_event_custom_event(pendo_client: Pendo) -> None:
    response = pendo_client.track(
        {
            "event": "TestEvent",
            "visitorId": "TestVisitorId",
            "accountId": "TestAccountId",
            "timestamp": int(time.time() * 1000),
            "properties": {"test": "test", "more": "more"},
            "context": {"more": "more", "testing": "testing", "one": {"two": "three"}},
        }
    )
    assert response.status_code == HTTPStatus.OK
