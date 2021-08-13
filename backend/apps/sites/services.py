import requests
from requests.exceptions import ConnectionError, ConnectTimeout


def get_site_availability(url: str) -> bool:
    """
    Проверка доступности сайта
    """
    try:
        return bool(requests.get(url))
    except (ConnectTimeout, ConnectionError):
        return False
