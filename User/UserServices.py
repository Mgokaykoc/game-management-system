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
            return json({"status": "error", "message": "User not found"})

        # databasede id _id olarak tutulduğu için bunu silmezsek bi dene daha id diye field açıyor
        update_data.pop("id")

        await user.update({"$set": update_data})

        return text("User informations updated successfully")

    except Exception as e:
        return json({"status": "error", "message": str(e)})


async def delete_user(request):
    user_id = str(request.args.get("id"))
    try:
        response = await User.get(user_id)
        if response:
            await response.delete()
            return  text("User deleted successfully")
        else:
            return json({"status": "error", "message": "User not found"})
    except Exception as e:
        return json({"status": "error", "message": str(e)})

    async def delete_user(request):
        user_id = str(request.args.get("id"))
        try:
            response = await User.get(user_id)
            if response:
                await response.delete()
                return text("User deleted successfully")
            else:
                return json({"status": "error", "message": "User not found"})
        except Exception as e:
            return json({"status": "error", "message": str(e)})

    async def check_user(request):
        user_id = str(request.args.get("id"))
        try:
            response = await User.get(user_id)
            if response:
                return  text("Kullanıcı Bulundu")
            else:
                return text("Kullanıcı Bulunamadı")
        except Exception as e:
            return json({"status": "error", "message": str(e)})

