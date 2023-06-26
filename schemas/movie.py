from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=5, max_length=50)
    year: int = Field(le= 2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=50)
    class Config:
        schema_extra= {
            "example": {
                "id" : 1,
                "title" : "Titulo de mi película",
                "overview": "Descripción de mi película",
                "year": 2023,
                "rating": 10,
                "category": "Categoría de mi película"
            }
        }
