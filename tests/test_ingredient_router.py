import os
import pytest
from tests.config.conftest import client
from src.db.database import Base
from tests.config.postgres_test_container import PostgresTestContainer

SECRET_TOKEN = os.getenv("SECRET_TOKEN")


class TestIngredientRouter:
    create_ingredient_payload = {
        "name": "Salt",
        "unit": "GRAM",
        "unit_value": 300,
        "purchase_place": "Supermarket",
        "image_url": "https://example.com/images/salt.jpg"
    }
    headers = {
        "Authorization": f"Bearer {SECRET_TOKEN}"
    }

    @pytest.fixture(scope="session", autouse=True)
    def postgres_test_container(self):
        postgres_test_container = PostgresTestContainer()
        postgres_test_container.start()
        yield postgres_test_container
        postgres_test_container.stop()

    @pytest.fixture(scope="function", autouse=True)
    def setup_teardown_function(self, postgres_test_container: PostgresTestContainer):
        print("\nBefore each test")
        engine = postgres_test_container.get_database_engine()
        Base.metadata.create_all(bind=engine)
        yield  # Tests execution
        Base.metadata.drop_all(bind=engine)
        print("\nAfter each test")

    def test_create_ingredient_bad_request(self):
        payload = {
            "name": "test"
        }
        response = client.post("/ingredients", json=payload, headers=self.headers)
        assert response.status_code == 400

    def test_create_existing_ingredient(self):
        success_response = client.post("/ingredients", json=self.create_ingredient_payload, headers=self.headers)
        fail_response = client.post("/ingredients", json=self.create_ingredient_payload, headers=self.headers)

        assert success_response.status_code == 201
        assert fail_response.status_code == 412

    def test_create_ingredient_success(self):
        response = client.post("/ingredients", json=self.create_ingredient_payload, headers=self.headers)
        assert response.status_code == 201
        assert "id" in response.json()
        assert "createdAt" in response.json()

    def test_get_ingredients_unauthorized(self):
        headers = {
            "Authorization": "Bearer invalid_token"
        }
        response = client.get("/ingredients", headers=headers)
        assert response.status_code == 401
        assert response.json() == {"message": "Token is invalid or has expired.", "version": os.environ["VERSION"]}

    def test_get_ingredients_forbidden(self):
        response = client.get("/ingredients")
        assert response.status_code == 403

    def test_get_ingredient_success(self):
        create_ingredient_response = client.post("/ingredients", json=self.create_ingredient_payload,
                                                 headers=self.headers)
        assert create_ingredient_response.status_code == 201

        get_ingredient_response = client.get(f"/ingredients/{create_ingredient_response.json()["id"]}",
                                             headers=self.headers)

        assert get_ingredient_response.status_code == 200
        assert "id" in get_ingredient_response.json()
        assert "createdAt" in get_ingredient_response.json()

    def test_get_ingredients_success(self):
        create_ingredient_response = client.post("/ingredients", json=self.create_ingredient_payload,
                                                 headers=self.headers)
        assert create_ingredient_response.status_code == 201

        response = client.get("/ingredients", headers=self.headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    def test_reset(self):
        response = client.post("/ingredients/reset", headers=self.headers)
        assert response.status_code == 200
        assert response.json() == {"msg": "All ingredients have been deleted"}
