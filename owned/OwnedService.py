from beanie import PydanticObjectId
from beanie.odm.operators.find.logical import And
from sanic import json, text

from User.UserModel import User
from game.GameModel import GameModel
from owned.OwnedModel import OwnedModel

class OwnedService:

    @staticmethod
    async def get_all_owneds(request):
            results = await OwnedModel.find_all().to_list()
            owneds = [owned.to_dict() for owned in results]
            return json(owneds)


    @staticmethod
    async def get_by_id(request):
            try:
                id = str(request.args.get("id"))
                owned = await OwnedModel.get(id)
                if not owned:
                    return json({"status": "error", "message": "OwnedModel not found"})
                return json(owned.to_dict())
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def add_owned(request):
            try:
                user_id = PydanticObjectId(str(request.json["userId"]))
                game_id = PydanticObjectId(str(request.json["gameId"]))

                existing = await OwnedModel.find_one(
                    And(
                        OwnedModel.user.id == user_id,
                        OwnedModel.game.id == game_id
                    )
                )
                if existing:
                    return json({"status": "error", "message": "OwnedModel already exists"})

                data = request.json
                new_owned = OwnedModel.from_dict(data)
                await new_owned.insert()
                return text("OwnedModel added successfully")
            except Exception as e:
                return json({"status": "error", "message": str(e)})


    @staticmethod
    async def update_owned(request):
        try:
            data = request.json
            owned_id = data["id"]
            owned = await OwnedModel.get(owned_id)
            if not owned:
                return text("OwnedModel not found")
            for key, value in data.items():
                if hasattr(owned, key) and key != "id":  # Avoid updating the ID
                    setattr(owned, key, value)
            await owned.replace()  # Save the updated owned object
            return text("OwnedModel updated successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


    @staticmethod
    async def delete_owned(request):
        try:
            owned = await OwnedModel.get(str(request.args.get("id")))
            if not owned:
                return text("OwnedModel not found")
            await owned.delete()
            return text("OwnedModel deleted successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})


    @staticmethod
    async def play1hour_owned(request):
        try:
            # Evvelinde var mı böyle bişey ona bakıyon
            owned = await OwnedModel.get(str(request.args.get("id")))
            if not owned:
                return text("OwnedModel not found")

            owned.playTime += 1
            await owned.replace()

            game = await GameModel.get(owned.game.ref.id)
            game.playTimeOfGame += 1
            game.weightedSumOfPlayTimes += owned.rating
            await game.replace()

            user = await User.get(owned.user.ref.id)
            user.total_play_time += 1
            if owned.playTime >= user.hours_in_most_played_game:
                user.most_played_game = game.name
                user.hours_in_most_played_game = owned.playTime
                await user.replace()

            return text("Playtime updated successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})

    @staticmethod
    async def rate_owned(request):
        try:
            owned = await OwnedModel.get(str(request.args.get("id")))
            if not owned:
                return json({"status": "error", "message": "OwnedModel not found"})
            if owned.playTime < 1:
                return json({"status": "error", "message": "OwnedModel is played less than 1 hour"})

            game = await GameModel.get(owned.game.ref.id)
            game.weightedSumOfPlayTimes = game.weightedSumOfPlayTimes + (-owned.rating + int(request.args.get("rating"))* owned.playTime)
            await game.replace()

            owned.rating = int(request.args.get("rating"))
            await owned.replace()

            return text("Rating updated successfully")
        except Exception as e:
            return json({"status": "error", "message": str(e)})



