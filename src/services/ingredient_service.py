from sqlalchemy.orm import Session
from src.errors.errors import ApiError, NotFoundException
from src.models.db_models import Ingredient
from src.schemas.pydantic_schemas import IngredientCreateSchema


def get_ingredient_by_id(db: Session, ingredient_id: str) -> Ingredient:
    exiting_ingredient = db.query(Ingredient).filter_by(id=ingredient_id).first()
    if not exiting_ingredient:
        raise NotFoundException("Ingredient not found")

    return exiting_ingredient


def get_ingredient_by_name(db: Session, name: str) -> Ingredient | None:
    return db.query(Ingredient).filter_by(name=name).first()


def get_all_ingredients(db: Session) -> list[Ingredient]:
    try:
        ingredients = db.query(Ingredient).all()

        return ingredients or list()
    except Exception as e:
        raise ApiError(f"Failed to get all ingredients: {e}")


def create_db_ingredient(db: Session, ingredient_create_schema: IngredientCreateSchema) -> Ingredient:
    try:
        ingredient = Ingredient(
            name=ingredient_create_schema.name,
            unit=ingredient_create_schema.unit,
            unit_value=ingredient_create_schema.unit_value,
            purchase_place=ingredient_create_schema.purchase_place,
            image_url=str(ingredient_create_schema.image_url),
        )
        db.add(ingredient)
        db.flush()
        db.commit()
        db.refresh(ingredient)

        return ingredient
    except ApiError:
        raise
    except Exception as e:
        db.rollback()
        raise ApiError(f"Failed to create ingredient: {e}")


def delete_all_ingredients(db: Session) -> None:
    try:
        db.query(Ingredient).delete()
        db.commit()
    except Exception as e:
        raise Exception(f"Failed to delete all ingredients from database: {e}")
