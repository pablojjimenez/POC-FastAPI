import motor.motor_asyncio
from bson import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.euroinnova_educalms
vegetables_collection = database.get_collection("vegetables")


def convert_vegetable(veg) -> dict:
    return {
        "_id": str(veg["_id"]),
        "name": veg["name"],
        "color": veg["color"],
        "calories": veg["calories"],
        "vitamins": veg["vitamins"],
        "season": veg["season"],
        "origin": veg["origin"]
    }

# CRUD Operation

# Retrieve all students present in the database
async def get_vegetables():
    vegs = []
    async for vegetable in vegetables_collection.find():
        vegs.append(convert_vegetable(vegetable))
    return vegs


# Add a new student into to the database
async def add_vegetable(veg_data: dict) -> dict:
    veg = await vegetables_collection.insert_one(veg_data)
    new_veg = await vegetables_collection.find_one({"_id": veg.inserted_id})
    return convert_vegetable(new_veg)


# Retrieve a student with a matching ID
async def get_vegetable(id: str) -> dict:
    veg = await vegetables_collection.find_one({"_id": ObjectId(id)})
    if veg:
        return convert_vegetable(veg)


# Update a student with a matching ID
async def update_vegetable(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    veg = await vegetables_collection.find_one({"_id": ObjectId(id)})
    if veg:
        updated_veg = await vegetables_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_veg:
            return True
        return False


# Delete a student from the database
async def delete_vegetable(id: str):
    veg = await vegetables_collection.find_one({"_id": ObjectId(id)})
    if veg:
        await vegetables_collection.delete_one({"_id": ObjectId(id)})
        return True
