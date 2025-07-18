import os
from dotenv import load_dotenv

load_dotenv(override=True if os.environ.get("ENV", "development") == "development" else False)

from fastapi import FastAPI
from src.models import db_models
from src.db.database_util import get_database_engine
from src.errors.exception_handlers import setup_exception_handlers
from src.routers.ingredient_router import ingredient_router
from src.routers.health_check_router import health_check_router

if os.environ.get("ENV", "development") == "development":
    db_models.Base.metadata.create_all(bind=get_database_engine())  # pragma: no cover

app = FastAPI()
app.title = "RECIPE BOOK API"
app.version = os.environ.get("VERSION", "1.0")

app.include_router(router=ingredient_router)
app.include_router(router=health_check_router)
setup_exception_handlers(app)
