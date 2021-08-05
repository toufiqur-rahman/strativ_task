import json

import requests
from rest_framework import status


def get_country_api_data():
    url = "https://restcountries.eu/rest/v2/all"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == status.HTTP_200_OK:
        return json.loads(response.text)
    return []