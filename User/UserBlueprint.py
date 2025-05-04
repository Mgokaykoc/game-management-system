from sanic import Blueprint, response

from User import UserServices
from User.UserServices import create_user, get_all_users, update_user,delete_user

# Blueprint tanımı
user_blueprint = Blueprint("user_blueprint", url_prefix="/api/users")



@user_blueprint.get("/getAll")
async def read_users(request):
    return await get_all_users(request)
    # Example: GET /getAll

@user_blueprint.route("/getById", methods=["GET"])
async def get_user_by_id(request):
    # Example: GET /getById?id=68169d4e8e21406fe36eb7ce
    return await UserServices.get_user_by_id(request)

@user_blueprint.post("/add")
async def create_new_user(request):
   return await create_user(request)
"""
 
"""

@user_blueprint.put("/update")
async def update_existing_user(request):
   return await update_user(request)
"""
Sadece "id" girilmesi şart, diğerleri güncellenecekse girilecek.
Example JSON body:
{
    "id": "68169d4e8e21406fe36eb7ce",
    "username": "updated username",
    "password": "updated password",
    "total_play_time": 123,
    "most_played_game": "updated game name"
}
"""

@user_blueprint.delete("/delete")
async def delete_existing_user(request):
 return await delete_user(request)
# Example: DELETE /delete?id=68169d4e8e21406fe36eb7ce

@user_blueprint.get("/checkuser")
async def checkuser(request):
    return await check_user(request)