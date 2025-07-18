import os
from sqlalchemy import create_engine
from testcontainers.postgres import PostgresContainer


class PostgresTestContainer:
    postgres_container: PostgresContainer = None
    connection_string: str = None
    port: int = None

    def __init__(self):
        self.port = int(os.environ["DB_PORT"])
        self.postgres_container = PostgresContainer(
            port=self.port,
            username=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            dbname=os.environ["DB_NAME"],
        ).with_exposed_ports(self.port)

    def start(self) -> None:
        self.postgres_container.start()
        self.connection_string = self.postgres_container.get_connection_url()
        print(f"PostgresTestContainer connection string: {self.connection_string}")
        os.environ["DB_PORT"] = str(self.postgres_container.get_exposed_port(self.port))

    def get_database_engine(self) -> create_engine:
        engine = create_engine(self.connection_string, echo=True)

        return engine

    def stop(self) -> None:
        self.postgres_container.stop()
