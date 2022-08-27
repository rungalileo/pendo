from enum import Enum, unique
from typing import Dict, Union

from pydantic import BaseModel, StrictInt, StrictStr


@unique
class PendoEventType(str, Enum):
    track = "track"


class Event(BaseModel):
    ...


class PendoProperties(BaseModel):
    ...


class PendoContext(BaseModel):
    ...


class PendoTrackEvent(Event):
    event: StrictStr
    visitorId: StrictStr
    accountId: StrictStr
    timestamp: StrictInt
    type: PendoEventType = PendoEventType.track
    properties: Union[Dict, PendoProperties] = dict()
    context: Union[Dict, PendoContext] = dict()


class Response(BaseModel):
    status_code: StrictInt
    body: Dict


class PendoResponse(Response):
    pass
