from pydantic import BaseModel, Field, field_validator

currency_list = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BCH", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB",
    "BRL", "BSD", "BTC", "BTG", "BWP", "BZD", "CAD", "CDF", "CHF", "CLP",
    "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DASH", "DJF",
    "DKK", "DOP", "DZD", "EGP", "EOS", "ETB", "ETH", "EUR", "FJD", "GBP",
    "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK",
    "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK",
    "LBP", "LKR", "LRD", "LSL", "LTC", "LYD", "MAD", "MDL", "MKD", "MMK",
    "MOP", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO",
    "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN",
    "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG",
    "SEK", "SGD", "SLL", "SOS", "SRD", "SVC", "SZL", "THB", "TJS", "TMT",
    "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU",
    "UZS", "VND", "XAF", "XAG", "XAU", "XCD", "XLM", "XOF", "XRP", "YER",
    "ZAR", "ZMW"
]


class Converter(BaseModel):
    amount: int = 1
    from_currency: str = Field(to_upper = True)
    to_currency: str = Field(to_upper = True)

    @field_validator("from_currency")
    @classmethod
    def validate_first_currency(cls, currency: str):
        if currency not in currency_list:
            raise ValueError("Incorrect currency")
        return currency
    
    @field_validator("to_currency")
    @classmethod
    def validate_second_currency(cls, currency: str):
        if currency not in currency_list:
            raise ValueError("Incorrect currency")
        return currency