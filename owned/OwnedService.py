from sanic import json, text

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
                if OwnedModel.find({"user": request.json["userId"], "game": request.json["gameId"]}):
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


