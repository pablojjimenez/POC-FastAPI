import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")


def student_helper(veg) -> dict:
    return {
        "_id": str(veg["_id"]),
        "name": veg["name"],
        "color": veg["color"],
        "calories": veg["calories"],
        "vitamins": veg["vitamins"],
        "season": veg["season"],
        "origin": veg["origin"]
    }
