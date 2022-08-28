# pendo

An unofficial Python HTTP client for [Pendo](https://developers.pendo.io/docs).

## Features

* Server Side Track Events

## Requirements

Python 3.9+

## Installation

```shell
pip install pendo
```

## Usage

#### [Server Side Track Events](https://support.pendo.io/hc/en-us/articles/360032294291-Track-Events-Configuration#server-side-0-7)

A Pendo Admin can access the `pendo_integration_key` in your app settings via: Subscription Settings > Choose your App > App Details.

```python
from pendo import Pendo

client = Pendo(pendo_integration_key="<YOUR_INTEGRATION_KEY>")
response = client.track({
    "event": "MyEvent",
    "visitorId": "00000-0000-0000-0000",
    "accountId": "11111-1111-1111-1111",
    "timestamp": int(time.time() * 1000),
})
assert response.status_code == 200
```

## Contributing

Read the [contributing guide](CONTRIBUTING.md).
