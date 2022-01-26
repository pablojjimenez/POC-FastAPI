from fastapi import Body
from fastapi.encoders import jsonable_encoder
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from server.services.database import (
    get_vegetables,
    add_vegetable,
    get_vegetable,
    update_vegetable,
    delete_vegetable,
)
from server.models.vegetable import (
    ErrorResponseModel,
    VegetableSchema,
    UpdateVegetableModel,
    VegetableModel,
)

router = InferringRouter()


@cbv(router)
class Vegetables:
    @router.post("/", response_description="Vegetable data added into the database", status_code=201)
    async def Sadd_vegetable_data(self, vegetable: VegetableSchema = Body(...)):
        vegetable = jsonable_encoder(vegetable)
        new_vegetable = await add_vegetable(vegetable)
        return VegetableModel(new_vegetable, "Vegetable added successfully.")

    @router.get("/", response_description="vegetables retrieved")
    async def Sget_vegetables(self, ):
        vegetables = await get_vegetables()
        if vegetables:
            return VegetableModel(vegetables, "vegetables data retrieved successfully")
        return VegetableModel(vegetables, "Empty list returned")

    @router.get("/{id}", response_description="vegetable data retrieved")
    async def Sget_vegetable_data(self, id):
        vegetable = await get_vegetable(id)
        if vegetable:
            return VegetableModel(vegetable, "vegetable data retrieved successfully")
        return ErrorResponseModel("An error occurred.", 404, "vegetable doesn't exist.")

    @router.put("/{id}")
    async def Supdate_vegetable_data(self, id: str, req: UpdateVegetableModel = Body(...)):
        req = {k: v for k, v in req.dict().items() if v is not None}
        updated_vegetable = await update_vegetable(id, req)
        if updated_vegetable:
            return VegetableModel(
                "vegetable with ID: {} name update is successful".format(id),
                "vegetable name updated successfully",
            )
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the vegetable data.",
        )

    @router.delete("/{id}", response_description="vegetable data deleted from the database")
    async def Sdelete_vegetable_data(self, id: str):
        deleted_vegetable = await delete_vegetable(id)
        if deleted_vegetable:
            return VegetableModel(
                "vegetable with ID: {} removed".format(id), "vegetable deleted successfully"
            )
        return ErrorResponseModel(
            "An error occurred", 404, "vegetable with id {0} doesn't exist".format(id)
        )
