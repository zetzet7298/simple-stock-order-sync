from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models, schemas
from app.database import get_db

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome!"}


@app.get("/products", response_model=List[schemas.ProductSchema])
async def get_products(db: AsyncSession = Depends(get_db)) -> List[models.Product]:
    stmt = select(models.Product)
    result = await db.execute(stmt)
    products = result.scalars().all()
    return list(products)
