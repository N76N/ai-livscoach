from pydantic import BaseModel

class SignupModel(BaseModel):
    email: str
    lösenord: str

class LoginModel(BaseModel):
    email: str
    lösenord: str