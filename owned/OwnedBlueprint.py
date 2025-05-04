from sanic import Blueprint

from owned.OwnedService import OwnedService

# Define the Blueprint for Owned entity
bp = Blueprint("OwnedBlueprint", url_prefix="/api/owneds")


"""
Olacak endpointler:
add
delete
play1hour
update (comment ve rate)
getByUser

"""

@bp.route("/getAll", methods=["GET"])
async def get_owneds(request):
    return await OwnedService.get_all_owneds(request)
    # Example: GET /getAll


@bp.route("/getById", methods=["GET"])
async def get_owned(request):
    return await OwnedService.get_by_id(request)
    # Example: GET /getById?id=68169d748e21406fe36eb7cf

@bp.route("/getByUser", methods=["GET"])
async def get_owned_by_user(request):
    return await OwnedService.get_owned_by_user(request)
    # Example: GET /getByUser?userId=68169d748e21406fe36eb7cf


@bp.route("/add", methods=["POST"])
async def add_owned(request):
    return await OwnedService.add_owned(request)
    """
    Example JSON body:
    {
        "userId": "68169d748e21406fe36eb7cf",
        "gameId": "68169d748e21406fe36eb7cf",
        "playTime": 130,
        "rating": 5,
        "comment": [
            {
                "username": "username",
                "text": "Great game!"
            }
        ]
    }
    """

@bp.route("/play1hour", methods=["PUT"])
async def play1hour_owned(request):
    return await OwnedService.play1hour_owned(request)
    # Example: PUT /play1hour?id=68169d748e21406fe36eb7cf

@bp.route("/rate", methods=["PUT"])
async def rate_owned(request):
    return await OwnedService.rate_owned(request)
    # Example: PUT /rate?id=68169d748e21406fe36eb7cf&rating=5

@bp.route("/update", methods=["PUT"])
async def update_owned(request):
    return await OwnedService.update_owned(request)
    """
    Sadece "id" girilmesi şart, diğerleri güncellenecekse girilecek.
    Example JSON body:
    {
        "id": "68169d748e21406fe36eb7cf",
        "playTime": 130,
        "rating": 5
    }
    """

@bp.route("/delete", methods=["DELETE"])
async def delete_owned(request):
    return await OwnedService.delete_owned(request)
    # Example: DELETE /delete?id=68169d748e21406fe36eb7cf
