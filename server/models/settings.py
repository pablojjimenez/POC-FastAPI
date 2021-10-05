from pydantic import BaseSettings


class Settings(BaseSettings):
    db: str
    mongo_url: str
    colec: str

    class Config:
        env_file = ".env"
