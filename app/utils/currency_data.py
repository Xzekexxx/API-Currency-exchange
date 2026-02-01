import requests
from app.core.config import settings

url_list = "https://api.apilayer.com/currency_data/list"
url_live = "https://api.apilayer.com/currency_data/live?source=USD&currencies="

headers= {
  "apikey": settings.API_KEY
}


def get_currency_list():
    response = requests.request("GET", url_list, headers=headers)

    return response.json()

def get_actual_rates_data():
    response = requests.request("GET", url_live, headers=headers)

    return response.json()

def convert_currency(first, second, amount):
    response = requests.request("GET", url=f"https://api.apilayer.com/currency_data/convert?to={first}&from={second}&amount={amount}", headers=headers)

    return response.json()