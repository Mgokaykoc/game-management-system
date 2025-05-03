from sanic import Blueprint, response

from User import UserModel, UserServices
import json
from User.UserServices import create_user, get_all_users, get_user_by_id, update_user,delete_user
# Blueprint tanımı
user_blueprint = Blueprint("user_blueprint", url_prefix="/users")


# 1. Kullanıcı oluşturma (POST)
@user_blueprint.post("/")
async def create_new_user(request):
   return await create_user(request)


# 2. Tüm kullanıcıları listele (GET)
@user_blueprint.get("/allusers")
async def read_users(request):
    return await get_all_users(request)


# 3. Tek bir kullanıcıyı getir (GET)
@user_blueprint.route("/getbyid", methods=["GET"])
async def get_user_by_id(request):
    # Example: GET /getById?id=123
    return await UserServices.get_user_by_id(request)


# 4. Kullanıcı bilgilerini güncelle (PUT)
@user_blueprint.put("/updatebyid")
async def update_existing_user(request):
   return await update_user(request)

# 5. Kullanıcıyı sil (DELETE)
@user_blueprint.delete("/delete_user")
async def delete_existing_user(request):
 return await delete_user(request)