from requests import PreparedRequest
from requests.auth import AuthBase


class PendoAuth(AuthBase):
    def __init__(self, pendo_integration_key: str) -> None:
        self.pendo_integration_key = pendo_integration_key

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers["x-pendo-integration-key"] = self.pendo_integration_key
        return r
