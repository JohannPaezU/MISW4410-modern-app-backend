import os

from tests.config.conftest import client

SECRET_TOKEN = os.getenv("SECRET_TOKEN")


class TestHealthCheckRouter:

    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert "Healthcheck" in response.json()
