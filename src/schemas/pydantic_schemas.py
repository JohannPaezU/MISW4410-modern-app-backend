from datetime import datetime

from pydantic import BaseModel, constr, Field, HttpUrl
from src.models.enums.measurement_unit import MeasurementUnit


class IngredientResponseSchema(BaseModel):
    id: str
    name: str
    unit: MeasurementUnit
    unit_value: float
    purchase_place: str
    image_url: str
    createdAt: datetime
    updatedAt: datetime


class IngredientCreateSchema(BaseModel):
    name: constr(min_length=1, max_length=100)
    unit: MeasurementUnit
    unit_value: float = Field(gt=0, description="Value must be greater than 0")
    purchase_place: str
    image_url: HttpUrl

    class Config:
        str_strip_whitespace = True
        use_enum_values = True


class MessageResponseSchema(BaseModel):
    msg: str
