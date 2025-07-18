from sqlalchemy import create_engine
import os


def get_standard_postgres_connection() -> str:
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASSWORD"]
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]

    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


def get_database_engine() -> create_engine:
    db_url = get_standard_postgres_connection()
    engine = create_engine(db_url, echo=True)

    return engine
