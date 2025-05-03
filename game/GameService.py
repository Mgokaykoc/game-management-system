from sanic import json, text

from game.GameModel import GameModel

class GameService:

    @staticmethod
    async def get_all_games(request):
        with SessionLocal() as session:
            results = session.query(GameModel).all()
            games = [game.to_dict() for game in results]
            return json(games)

    @staticmethod
    async def find_by_id(id):
        with SessionLocal() as session:
            game = session.query(GameModel).filter(GameModel.id == id).first()
            return game

    @staticmethod
    async def get_game_by_id(request):
        with SessionLocal() as session:
            try:
                game_id = int(request.args.get("id"))
                game = await GameService.find_by_id(game_id)
                if game:
                    result = game.to_dict()
                    return json(result)
                return json({"status": "error", "message": "GameModel not found"})
            except Exception as e:
                return json({"status": "error", "message": str(e)})

    @staticmethod
    async def add_game(request):
        with SessionLocal() as session:
            try:
                data = request.json #bu fonksiyon json payload'ını alıp python dict'ine dönüştürüyormuş
                new_game = GameModel.from_dict(data)
                session.add(new_game)
                session.commit()
                return text("status: success, message" "GameModel added successfully")
            except Exception as e:
                session.rollback()
                return text("Bir hata oldu, yaptığın kayıt edilmedi", str(e))
            finally:
                session.close()

    @staticmethod
    async def update_game(request):
        session = SessionLocal()
        try:
            data = request.json
            game_id = data["id"]
            game = session.query(GameModel).filter_by(id=game_id).first()
            if not game:
                return text("GameModel not found")

            for key, value in data.items():
                if hasattr(game, key):
                    setattr(game, key, value)
            session.commit()
            return text("{)status: success, message: GameModel updated successfully")
        except Exception as e:
            session.rollback()
            return text(str(e))
        finally:
            session.close()

    @staticmethod
    async def delete_game(request):
        session = SessionLocal()
        try:
            game_id = int(request.args.get("id"))
            game = session.query(GameModel).filter_by(id=game_id).first()
            if not game:
                return json({"status": "error", "message": "GameModel not found"})
            session.delete(game)
            session.commit()
            return json({"status": "success", "message": "GameModel deleted successfully"})
        except Exception as e:
            session.rollback()
            return json({"status": "error", "message": str(e)})
        finally:
            session.close()


