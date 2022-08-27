from unittest import mock

from pendo import Pendo
from pendo.types import PendoTrackEvent


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"})
    ),
)
def test_pendo(
    mock_post: mock.MagicMock, pendo_client: Pendo, pendo_track_event: PendoTrackEvent
) -> None:
    response = pendo_client.track(event=pendo_track_event)
    assert response.status_code == 200
    assert response.body == {"status": "ok"}


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"})
    ),
)
def test_pendo_with_extra_headers(
    mock_post: mock.MagicMock,
    pendo_client_extra_headers: Pendo,
    pendo_track_event: PendoTrackEvent,
) -> None:
    response = pendo_client_extra_headers.track(event=pendo_track_event)
    assert response.status_code == 200
    assert response.body == {"status": "ok"}


@mock.patch(
    "pendo.main.requests.post",
    return_value=mock.Mock(
        status_code=200, json=mock.Mock(return_value={"status": "ok"})
    ),
)
def test_pendo_track_event_with_props_and_context(
    mock_post: mock.MagicMock,
    pendo_client: Pendo,
    pendo_track_event_with_props_and_context: PendoTrackEvent,
) -> None:
    response = pendo_client.track(event=pendo_track_event_with_props_and_context)
    assert response.status_code == 200
    assert response.body == {"status": "ok"}
