from pydantic import BaseModel, EmailStr

# 회원가입 요청용
class SignupRequest(BaseModel):
    email: EmailStr
    username: str
    password: str

# 로그인 요청용
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# 로그인 응답용
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
