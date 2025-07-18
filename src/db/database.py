from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from src.db.database_util import get_database_engine

engine = None
Base = declarative_base()


def get_session_local() -> sessionmaker:
    global engine
    engine = get_database_engine()
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> scoped_session:
    session_local = get_session_local()
    db = session_local()
    try:
        yield db
    finally:
        db.close()
