from fastapi import APIRouter, status
import socket


health_check_router = APIRouter(tags=["HealthCheck"], prefix="/health")


@health_check_router.get("", response_model=str, status_code=status.HTTP_200_OK)
async def health_check():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return f"Healthcheck from: {hostname} ({ip_address})"
