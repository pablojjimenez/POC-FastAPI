from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class VegetableSchema(BaseModel):
    name: str = Field(...)
    color: EmailStr = Field(...)
    calories: str = Field(...)
    vitamins: [str] = Field(...)
    season: [str] = Field(...)
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

            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
