from enum import Enum, unique
from http import HTTPStatus
from typing import Dict, Union

from pydantic import BaseModel, StrictInt, StrictStr


@unique
class PendoEventType(str, Enum):
    track = "track"


class PendoProperties(BaseModel):
    ...


class PendoContext(BaseModel):
    ...


class PendoTrackEvent(BaseModel):
    event: StrictStr
    visitorId: StrictStr
    accountId: StrictStr
    timestamp: StrictInt
    type: PendoEventType = PendoEventType.track
    properties: Union[Dict, PendoProperties] = dict()
    context: Union[Dict, PendoContext] = dict()


class Response(BaseModel):
    status_code: HTTPStatus
    data: dict


class PendoResponse(Response):
    pass
