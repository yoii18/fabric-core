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
    params = {}
    headers = {}

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
        self.build_params()
        self.build_headers()

    def build_url(self):
        return (
            self.base_url + self.resource_id
        )
    
    def build_params(self):
        self.params["api-key"] = self.api_key
        self.params["format"] = self.format
        self.params["limit"] = self.limit

    def build_headers(self):
        self.headers["Accept"] = "application/json"
        self.headers["User-Agent"] = "fabric-core/0.1"


class GetData:
    def __init__(self, url, params: dict, headers: dict):
        self.url = url
        self.params = params
        self.headers = headers
    
    def get_response(self):
        res = requests.get(
            url = self.url,
            params = self.params,
            headers = self.headers
        )

        return res
    
    def get_json_response(self, res):
        return res.json()
    
    def get_payload_keys(self, payload):
        '''
        payload should be in json format
        '''
        return payload.keys()


class DataConversion:
    pass

class DataCleaning:
    pass


######################################################### notebook code #########################################################
# gdp_data_api_obj = APICreation()

# gdp_data_get_obj = GetData(
#     gdp_data_api_obj.url,
#     gdp_data_api_obj.params,
#     gdp_data_api_obj.headers
# )

# res = gdp_data_get_obj.get_response()
# payload = gdp_data_get_obj.get_json_response(res)
# keys = gdp_data_get_obj.get_payload_keys(payload)

# print(payload["records"])