from app.errors.base import CustomExeption

class InvalidCurrencyCodeException(CustomExeption):
    def __init__(self, detail=None):
        super().__init__(detail=detail, status_code=400, message="Invalid code")

class ApiError(CustomExeption):
    def __init__(self, detail=None):
        super().__init__(detail=detail, status_code=500, message="sever error try later")