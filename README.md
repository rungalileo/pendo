# pendo

An unofficial Python HTTP client for [Pendo](https://developers.pendo.io/docs).

## Requirements

Python 3.9+

## Installation

```shell
pip install pendo
```

## Usage

```python
from pendo import Pendo

client = Pendo(pendo_integration_key='YOUR_INTEGRATION_KEY')
response = client.track(event=PendoTrackEvent(
        event="MyEvent",
        visitorId="00000-0000-0000-0000",
        accountId="11111-1111-1111-1111",
        timestamp=int(time.time() * 1000),
    ))
assert response.status_code == 200
```

## Contributing

Read the [contributing guide](CONTRIBUTING.md).
