from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database.database import get_session
from app.schemas.currency import Converter
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Users
from app.core.config import settings
from app.utils.currency_data import get_currency_list, get_actual_rates_data, convert_currency

router_currency = APIRouter(prefix="/currency", tags=['Currency'])

@router_currency.get("/list")
async def get_currency():
    currency_list = get_currency_list()

    return {
        "message": "Available currencies for conversion",
        "currency": currency_list.get('currencies', {})
    }

@router_currency.get("/actual_rates")
async def get_actual_rates():
    curruncy_live = get_actual_rates_data()
    return {
        "message": "Available currencies for conversion",
        "currency": curruncy_live.get('quotes', {})
    }

@router_currency.post("/converter")
async def currency_converter(data: Converter):
    convert = convert_currency(data.to_currency, data.from_currency, data.amount)

    return {
        "amount": data.amount,
        "from": data.from_currency,
        "to": data.to_currency,
        "result": convert.get('result')
    }