from sanic import json, text

from game.OwnedModel import OwnedModel

class OwnedService:

    @staticmethod
    async def get_all_games(request):
            results = await OwnedModel.find_all().to_list()
            games = [game.to_dict() for game in results]
            return json(games)


    @staticmethod
    async def get_by_id(request):
            try:
                id = str(request.args.get("id"))
                game = await OwnedModel.get(id)
                if not game:
                    return json({"status": "error", "message": "OwnedModel not found"})
                return json(game.to_dict())
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def add_game(request):
            try:
                data = request.json
                new_game = OwnedModel.from_dict(data)
                await new_game.insert()
                return text("OwnedModel added successfully")
            except Exception as e:
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))


    @staticmethod
    async def update_game(request):
        try:
            data = request.json
            game_id = data["id"]
            game = await OwnedModel.get(game_id)
            if not game:
                return text("OwnedModel not found")
            for key, value in data.items():
                if hasattr(game, key) and key != "id":  # Avoid updating the ID
                    setattr(game, key, value)
            await game.replace()  # Save the updated game object
            return text("OwnedModel updated successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


    @staticmethod
    async def delete_game(request):
        try:
            game = await OwnedModel.get(str(request.args.get("id")))
            if not game:
                return text("OwnedModel not found")
            await game.delete()
            return text("OwnedModel deleted successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


