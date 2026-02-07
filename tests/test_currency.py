from unittest.mock import MagicMock
import requests

from app.utils.currency_data import get_currency_list, get_actual_rates_data, convert_currency


def test_get_currency_list():
    mock_response = MagicMock()
    mock_response.json.return_value = {"currencies": {"AED": "Dirham", "AFN": "Afghani"}}

    requests.request = MagicMock(return_value = mock_response)

    assert get_currency_list() == {"currencies": {"AED": "Dirham", "AFN": "Afghani"}}

def test_get_actual_rates_data():
    mock_response = MagicMock()
    mock_response.json.return_value = {"quotes": {"USDAED": 3.6725, "USDAFN": 65.499871, "USDALL": 81.893517}}
    
    requests.request = MagicMock(return_value = mock_response)

    assert get_actual_rates_data() == {"quotes": {"USDAED": 3.6725, "USDAFN": 65.499871, "USDALL": 81.893517}}

def test_convert_currency():
    mock_response = MagicMock()
    mock_response.json.return_value = {"info": {"quote": 0.012987,"timestamp": 1770383464},"query": {"amount": 100,"from": "RUB","to": "USD"},"result": 1.2987,"success": True }

    requests.request = MagicMock(return_value = mock_response)

    assert convert_currency(first="RUB", second="USD", amount="100") == {"info": {"quote": 0.012987,"timestamp": 1770383464},"query": {"amount": 100,"from": "RUB","to": "USD"},"result": 1.2987,"success": True }
