import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String, func
from sqlalchemy import Enum as PyEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PROCESSING = "prosessing"
    COMPLETED = "completed"
    FAILED = "failed"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[Optional[str]]
    stock_quantity: Mapped[int] = mapped_column(default=0)
    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    product_sku: Mapped[str] = mapped_column(String, index=True)
    quantity: Mapped[int]
    status: Mapped[OrderStatus] = mapped_column(
        PyEnum(OrderStatus), default=OrderStatus.PENDING
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
