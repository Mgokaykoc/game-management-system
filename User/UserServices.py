from sanic import json, text
from typing import Dict, Any
from bson import ObjectId
from sanic.response import JSONResponse

from User.UserModel import User, to_dict, from_dict
from typing import List



async def create_user(request):
    try:
        data = request.json
        new_user = from_dict(data)
        await new_user.insert()
        return text("User created successfully")
    except Exception as e:
        return text(str(e), status=400)


async def get_all_users(request) -> JSONResponse:
    users = await User.find_all().to_list()
    userlist = [to_dict(user) for user in users]
    return json(userlist)


async def get_user_by_id(request):

        try:
            user_id = str(request.args.get("id"))
            user = await User.get(user_id)
            if user:
                result = to_dict(user)
                return json(result)
            return json({"status": "error", "message": "UserEntity not found"})
        except Exception as e:
            return json({"status": "error", "message": str(e)})


async def update_user(request):
    user_id = request.json.get("id")
    update_data = request.json
    try:
        # Kullanıcıyı ID'sine göre bul
        user = await User.get(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}

        # "update_data"dan None değerleri filtrele (isteğe bağlı)
        update_data = {key: value for key, value in update_data.items()}

        # Güncelleme işlemi (MongoDB $set kullanılarak)
        await user.update({"$set": update_data})

        # Güncellenmiş kullanıcıyı döndür
        updated_user = await User.get(user_id)
        return text("User informations updated successfully")

    except Exception as e:
        return {"status": "error", "message": str(e)}



async def delete_user(request):
#deleteuserbyid
    user_id = str(request.json.get("id"))
    print(user_id)

    try:

        response=await User.get(user_id)
        if response is None:
            return text("User not found")

        if response:
            await response.delete()
            return  text("User deleted successfully")


    except Exception as e:
        return {"status": "error", "message": str(e)}