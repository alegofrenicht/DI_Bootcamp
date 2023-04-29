from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def api_func():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
        'start': '1',
        'limit': '20',
        'listing_status': 'active',
        'sort': 'cmc_rank',
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e
