"""Модуль, содержащий сервисы."""

import requests
import datetime
import xml.etree.ElementTree as etree
from django.conf import settings
from django.db import transaction
from apps.coins.models import Value, Rate


def get_rates() -> list[dict[str, str | int]]:
    keys: dict[str, str] = {
        'Name': 'name',
        'Nominal': 'nominal',
        'ParentCode': 'code'
    }
    url: str = settings.EXTERNAL_URLS['rates']
    response = requests.get(url)
    rates_path = settings.BASE_DIR / 'apps' / 'coins' / 'management' / 'seed' / 'rates.xml'
    if response.status_code != 200:
        with open(rates_path) as f:
            content = f.read()
    else:
        content = response.text
        with open(rates_path, 'w+') as f:
            f.write(content)
    root = etree.fromstring(content)
    rates: list[dict[str, str | int]] = [
        {
            keys[element.tag]: element.text.strip() for element in item if element.tag in keys
        } for item in root.findall('Item')
    ]
    return rates


def get_values(d: datetime.date):
    """Проверяем наличие записей в БД или подгружаем по API."""
    count = Value.objects.filter(date=d).count()
    if count == 0:
        keys: dict[str, str] = {
            'NumCode': 'num_code',
            'CharCode': 'char_code',
            'Value': 'value',
        }
        url: str = settings.EXTERNAL_URLS["coins"] % d.strftime('%d/%m/%Y')
        response = requests.get(url)
        if response.status_code != 200:
            return
        rates = {rate['code']: rate['id'] for rate in Rate.objects.values('id', 'code')}
        root = etree.fromstring(response.text)
        date = datetime.datetime\
            .strptime(root.attrib.get('Date', d.strftime('%d.%m.%Y')), '%d.%m.%Y')
        with transaction.atomic():
            for coin in root.findall('Valute'):
                rate_id = rates.get(coin.attrib['ID'])
                if rate_id is None:
                    continue
                value = {
                    keys[element.tag]: element.text.strip()
                    if element.tag != 'Value'
                    else float(element.text.strip().replace(',', '.'))
                    for element in coin if element.tag in keys
                }
                Value.objects.update_or_create(date=date, rate_id=rate_id, defaults=value)
