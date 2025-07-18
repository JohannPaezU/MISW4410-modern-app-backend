from dotenv import load_dotenv, find_dotenv


def setup_test_environment():
    env_file = find_dotenv('../../.env.test')
    load_dotenv(env_file, override=True)


setup_test_environment()

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)
