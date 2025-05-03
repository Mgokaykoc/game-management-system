from beanie import init_beanie
import motor.motor_asyncio

from User.UserModel import User
#from Game import GameModel

async def init_db():

    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://admin:admin@cluster0.moiqqfd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

    await init_beanie(database=client.db_name, document_models=[User])