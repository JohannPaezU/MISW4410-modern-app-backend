class ApiError(Exception):
    status_code = 500
    message = "Internal Server Error"

    def __init__(self, message: str):
        self.message = message


class UnauthorizedException(ApiError):
    status_code = 401


class ForbiddenException(ApiError):
    status_code = 403


class NotFoundException(ApiError):
    status_code = 404


class PreconditionFailedException(ApiError):
    status_code = 412
