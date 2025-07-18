from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.errors.errors import PreconditionFailedException
from src.routers.utils.dependencies import validate_token
from src.schemas.pydantic_schemas import (
    MessageResponseSchema,
    IngredientResponseSchema,
    IngredientCreateSchema
)
from src.services import ingredient_service


ingredient_router = APIRouter(tags=["Ingredient"], prefix="/ingredients")


@ingredient_router.get("", response_model=list[IngredientResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_ingredients(
    db: Session = Depends(get_db),
    _=Depends(validate_token)
) -> list[IngredientResponseSchema]:
    ingredients = ingredient_service.get_all_ingredients(db)

    return ingredients


@ingredient_router.post("", response_model=IngredientResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_ingredient(
    ingredient_create_schema: IngredientCreateSchema,
    db: Session = Depends(get_db),
    _=Depends(validate_token)
) -> IngredientResponseSchema:
    existing_ingredient = ingredient_service.get_ingredient_by_name(db, ingredient_create_schema.name)
    if existing_ingredient:
        raise PreconditionFailedException(f"Ingredient {ingredient_create_schema.name} already exists")

    db_ingredient = ingredient_service.create_db_ingredient(db, ingredient_create_schema)

    return db_ingredient


@ingredient_router.get("/{ingredient_id}", response_model=IngredientResponseSchema,
                       status_code=status.HTTP_200_OK)
async def get_ingredient(
    ingredient_id: str,
    db: Session = Depends(get_db),
    _=Depends(validate_token)
) -> IngredientResponseSchema:
    existing_ingredient = ingredient_service.get_ingredient_by_id(db, ingredient_id)

    return existing_ingredient


@ingredient_router.post("/reset", response_model=MessageResponseSchema, status_code=status.HTTP_200_OK)
async def reset(
    db: Session = Depends(get_db),
    _=Depends(validate_token)
) -> MessageResponseSchema:
    ingredient_service.delete_all_ingredients(db)

    return MessageResponseSchema(msg="All ingredients have been deleted")
