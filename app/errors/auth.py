from app.errors.base import CustomExeption

class UserNotFoundExeption(CustomExeption):
    def __init__(self, detail = None):
        super().__init__(status_code=404, message="User not found", detail = detail)

    
class UserAlreadyExistsException(CustomExeption):
    def __init__(self, detail = None):
        super().__init__(detail=detail, status_code=409, message="User already exists")

        

class InvalidCredentialsException(CustomExeption):
    def __init__(self, detail = None):
        super().__init__(detail = detail, status_code=401, message="Invalid credentials")