from server.routes.vegetable import router as VegetableRouter
from fastapi import FastAPI

app = FastAPI()
app.include_router(VegetableRouter, tags=["vegetables"], prefix="/vegetables")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
