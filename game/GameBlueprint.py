from sanic import Sanic, Blueprint
from sanic.response import json

from game.GameService import GameService

# Define the Blueprint for Game entity
bp = Blueprint("GameBlueprint", url_prefix="/api/games")

#request.args.get("id")

@bp.route("/getAll", methods=["GET"])
async def get_games(request):
    # Example: GET /getAll
    return await GameService.get_all_games(request)


@bp.route("/getById", methods=["GET"])
async def get_game(request):
    # Example: GET /getById?id=123
    return await GameService.get_game_by_id(request)


@bp.route("/add", methods=["POST"])
async def add_game(request):
    # Example: POST /add
    # Request Body (JSON):
    # {
    #     "title": "New Game",
    #     "authors": "Jane Austen",
    #     "isbn": "0-061-96436-0",
    #     "publisher": "Publisher Name",
    #     "category": "Literature",
    #     "date":"1992-12-28",1.	Introduction
    #     "pages":192
    # }
    return await GameService.add_game(request)


@bp.route("/update", methods=["PUT"])
async def update_game(request):
    # Example: PUT /update
    # Request Body (JSON):
    # {
    #     "id": 123,
    #     "title": "Updated Game Title",
    #     "author": "Updated Author Name"
    # }
    return await GameService.update_game(request)


@bp.route("/delete", methods=["DELETE"])
async def delete_game(request):
    # Example: DELETE /delete?id=123
    return await GameService.delete_game(request)
