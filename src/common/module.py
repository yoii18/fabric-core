import requests

"""
API Structure:-
    base URL: https://api.data.gov.in/resource/
    resourceID: 27d9503c-ff52-4844-8092-d40f47a4677a      #### add "?" after
    params:
        API Key: api-key=579b464db66ec23bdd000001352b47ea49a5417760ddf8b92f4e415b
        Format: format=xml
        Limit: limit=count
"""

class APICreation:

    url=""

    def __init__(self, base_url = "https://api.data.gov.in/resource/",
                 resource_id = "27d9503c-ff52-4844-8092-d40f47a4677a",
                 api_key = "579b464db66ec23bdd000001352b47ea49a5417760ddf8b92f4e415b",
                 format = "json",
                 limit = "10"):
        self.base_url = base_url
        self.resource_id = resource_id
        self.api_key = api_key
        self.format = format
        self.limit = limit

        self.url = self.build_url()

    def build_url(self):
        return (
            self.base_url + self.resource_id
        )


class GetData:
    pass

class DataConversion:
    pass

class DataCleaning:
    pass


a1 = APICreation()

res = requests.get(
    a1.url,
    params={
        "api-key": a1.api_key,
        "format": a1.format,
        "limit": a1.limit
    },
    headers={
        "Accept": "application/json",
        "User-Agent": "fabric-core/0.1",
    },
)

payload = res.json()

print(payload.keys())
