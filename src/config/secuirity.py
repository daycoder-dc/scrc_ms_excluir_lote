from fastapi import Security, HTTPException, status, Depends
from src.config.settings import Settings, get_setting
from fastapi.security import APIKeyHeader
from typing import Annotated

API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def get_api_key(sttg: Annotated[Settings, Depends(get_setting)], api_key_header:str = Security(api_key_header)):
    if api_key_header == sttg.api_key_token:
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acceso no autoraizado"
    )
