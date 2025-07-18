import os
from fastapi import Request
from src.errors.errors import UnauthorizedException, ApiError, ForbiddenException


SECRET_TOKEN = os.getenv("SECRET_TOKEN")


def validate_token(request: Request) -> None:
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise ForbiddenException("Token is required.")
        token = token.split(" ")[-1]
        if token != SECRET_TOKEN:
            raise UnauthorizedException("Token is invalid or has expired.")
    except ForbiddenException:
        raise
    except UnauthorizedException:
        raise
    except Exception as e:
        raise ApiError(f"Failed to validate token {e}")
