from pydantic import BaseModel, EmailStr, Field
from typing import List

class VegetableSchema(BaseModel):
    name: str = Field(...)
    color: str = Field(...) # color: EmailStr
    calories: str = Field(...)
    vitamins: List[str] = Field(...)
    season: List[str] = Field(...)
    origin: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Tomato",
                "color": "RED",
                "calories": 33,
                "vitamins": [
                    "B2"
                ],
                "season": [
                    "WINTER",
                    "SPRING",
                    "SUMMER",
                    "AUTUMN"
                ],
                "origin": "Spain"
            }
        }


class UpdateVegetableModel(BaseModel):
    name: str = Field(...)
    calories: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Tomato",
                "calories": 33,
            }
        }


def VegetableModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
