import requests

from app.core.config import settings
from app.errors.currency import ApiError

url_list = "https://api.apilayer.com/currency_data/list"
url_live = "https://api.apilayer.com/currency_data/live?source=USD&currencies="

headers= {
  "apikey": settings.API_KEY
}


def get_currency_list():
    try:
        response = requests.request("GET", url_list, headers=headers)
        return response.json()
    except:
        raise ApiError(detail="ошибка внешнего апи")

def get_actual_rates_data():
    try:
        response = requests.request("GET", url_live, headers=headers)

        return response.json()
    except:
        raise ApiError(detail="ошибка внешнего апи")
    
def convert_currency(first, second, amount):
    try:
        response = requests.request("GET", url=f"https://api.apilayer.com/currency_data/convert?to={first}&from={second}&amount={amount}", headers=headers)

        return response.json()
    except:
        raise ApiError(detail="ошибка внешнего апи")