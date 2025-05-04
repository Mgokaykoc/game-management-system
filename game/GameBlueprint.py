from sanic import Blueprint

from game.GameService import GameService

# Define the Blueprint for game entity
bp = Blueprint("GameBlueprint", url_prefix="/api/games")


@bp.route("/getAll", methods=["GET"])
async def get_games(request):
    return await GameService.get_all_games(request)
    # Example: GET /getAll



@bp.route("/getById", methods=["GET"])
async def get_game(request):
    return await GameService.get_by_id(request)
    # Example: GET /getById?id=68169d748e21406fe36eb7cf


@bp.route("/add", methods=["POST"])
async def add_game(request):
    return await GameService.add_game(request)
    """
    Example JSON body:
    {
        "name": "game Name",
        "genre": "Action",
        "photo": "http://example.com/photo.jpg"
    }
    """


@bp.route("/update", methods=["PUT"])
async def update_game(request):
    return await GameService.update_game(request)
    """
    Sadece "id" girilmesi şart, diğerleri güncellenecekse girilecek.
    Example JSON body:
    {
        "id": "68169d748e21406fe36eb7cf",
        "name": "updated name",
        "genre": "updated genre", 
        "photo": "http://example.com/updatedphoto.jpg"
    }
    """

@bp.route("/delete", methods=["DELETE"])
async def delete_game(request):
    return await GameService.delete_game(request)
    # Example: DELETE /delete?id=68169d748e21406fe36eb7cf
