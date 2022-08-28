import time
from unittest import mock

import pytest

from pendo import Pendo
from pendo.exc import PendoException
from pendo.types import PendoTrackEvent


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"}), ok=True
    ),
)
def test_pendo(
    mock_post: mock.MagicMock, pendo_client: Pendo, pendo_track_event: PendoTrackEvent
) -> None:
    response = pendo_client.track(event=pendo_track_event)
    assert response.status_code == 200


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=500,
        reason="Internal Server Error",
        ok=False,
    ),
)
def test_pendo_catch_exception(
    mock_post: mock.MagicMock, pendo_client: Pendo, pendo_track_event: PendoTrackEvent
) -> None:
    with pytest.raises(PendoException) as exc_info:
        pendo_client.track(event=pendo_track_event)
    assert (
        exc_info.value.args[0]
        == "Request exited with status 500: Internal Server Error"
    )


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"}), ok=True
    ),
)
def test_pendo_with_extra_headers(
    mock_post: mock.MagicMock,
    pendo_client_extra_headers: Pendo,
    pendo_track_event: PendoTrackEvent,
) -> None:
    response = pendo_client_extra_headers.track(event=pendo_track_event)
    assert response.status_code == 200


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"}), ok=True
    ),
)
def test_pendo_track_event_with_props_and_context(
    mock_post: mock.MagicMock,
    pendo_client: Pendo,
    pendo_track_event_with_props_and_context: PendoTrackEvent,
) -> None:
    response = pendo_client.track(event=pendo_track_event_with_props_and_context)
    assert response.status_code == 200


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"}), ok=True
    ),
)
def test_pendo_track_event_dict_input(
    mock_post: mock.MagicMock,
    pendo_client: Pendo,
) -> None:
    response = pendo_client.track(
        {
            "event": "TestEvent",
            "visitorId": "TestVisitorId",
            "accountId": "TestAccountId",
            "timestamp": int(time.time() * 1000),
        }
    )
    assert response.status_code == 200


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"}), ok=True
    ),
)
def test_pendo_track_event_custom_event(
    mock_post: mock.MagicMock,
    pendo_client: Pendo,
) -> None:
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
    assert response.status_code == 200
