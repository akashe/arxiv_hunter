from datetime import datetime, timedelta
from typing import Any

from fastapi import HTTPException, Security, status
from fastapi import security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
import jwt

class AuthHandler:
    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"])
    secret = "secretkey"
    algorithm = "HS256"

    def get_password_hash(self,password:str) -> str:
        return self.password_context.hash(secret=password)
    
    def verify_password(self,password,hashed_password) -> bool:
        return self.password_context.verify(secret=password, hash=hashed_password)
    
    def encode_token(self, user_id) -> str:
        payload: dict[str,Any] = {
            "exp": datetime.utcnow() + timedelta(hours=8),
            "iat": datetime.utcnow(),
            "sub": user_id
        }
        return jwt.encode(payload=payload, key=self.secret, algorithm=self.algorithm)

    def decode_token(self, token) -> Any:
        try:
            payload = jwt.decode(jwt=token, key=self.secret, algorithms=[self.algorithm])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Expired Signature"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            )
    def auth_wrapper(self, auth:HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)