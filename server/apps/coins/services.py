""""Модуль содержащий сервисы."""

import requests
import xml.etree.ElementTree as etree
from django.conf import settings



def get_rates() -> list[dict[str, str | int]]:
    keys: dict[str, str] = {
        'Name': 'name',
        'Nominal': 'nominal',
        'ParentCode': 'code'
    }
    url: str = settings.EXTERNAL_URLS['rates']
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.RequestException()
    root = etree.fromstring(response.text)
    rates: list[dict[str, str | int]] = [
        {
            keys[element.tag]: element.text for element in item if element.tag in keys
        } for item in root.findall('Item')
    ]
    return rates
