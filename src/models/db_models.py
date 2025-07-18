import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Enum, Float
from src.db.database import Base
from src.models.enums.measurement_unit import MeasurementUnit


class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False, unique=True)
    unit = Column(Enum(MeasurementUnit), nullable=False)
    unit_value = Column(Float, nullable=False)
    purchase_place = Column(String(200), nullable=False)
    image_url = Column(String(300), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updatedAt = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc),
                       onupdate=lambda: datetime.now(timezone.utc))
