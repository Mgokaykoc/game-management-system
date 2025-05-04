from sanic import json, text

from game.GameModel import GameModel

class GameService:

    @staticmethod
    async def get_all_games(request):
            results = await GameModel.find_all().to_list()
            games = list(game.to_dict() for game in results)
            return json(games)


    @staticmethod
    async def get_by_id(request):
            try:
                id = str(request.args.get("id"))
                game = await GameModel.get(id)
                if not game:
                    return json({"status": "error", "message": "GameModel not found"})
                return json(game.to_dict())
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def add_game(request):
            try:
                data = request.json
                new_game = GameModel.from_dict(data)
                await new_game.insert()
                return text("GameModel added successfully")
            except Exception as e:
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))


    @staticmethod
    async def update_game(request):
        try:
            data = request.json
            game_id = data["id"]
            game = await GameModel.get(game_id)
            if not game:
                return text("GameModel not found")
            for key, value in data.items():
                if hasattr(game, key) and key != "id":  # Avoid updating the ID
                    setattr(game, key, value)
            await game.replace()  # Save the updated game object
            return text("GameModel updated successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


    @staticmethod
    async def delete_game(request):
        try:
            game = await GameModel.get(str(request.args.get("id")))
            if not game:
                return text("GameModel not found")
            await game.delete()
            return text("GameModel deleted successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


