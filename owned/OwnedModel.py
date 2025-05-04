from typing import List

from beanie import Document, Link

from User.UserModel import User
from game.GameModel import GameModel


class OwnedModel(Document):
    user: Link[User]  # Reference to the User collection
    game: Link[GameModel]  # Reference to the GameModel collection
    playTime: int = 0
    rating: int = 0
    comment: List[dict] = []

    class Settings:
        name = "owneds"


    def to_dict(self) -> dict:
        return {
            "id": str(self.id),  # Convert to string to make it JSON serializable
            "user": str(self.user.ref.id),
            "game": str(self.game.ref.id),
            "playTime": self.playTime,
            "rating": self.rating,
            "comment": self.comment
        }


    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(
            user= data["userId"],
            game= data["gameId"],
            playTime=data.get("playTime", 0),
            rating=data.get("rating", 0),
            comment=data.get("comment", [])
        )

"""
Pycharm'ın autocompete özelliğiyle oluşturulmuş bir örnek JSON.
{
    "userId": "68169d748e21406fe36eb7cf",
    "gameId": "68169d748e21406fe36eb7cf",
    "playTime": 130,
    "rating": 5,
    "comment": [
        {
            "username": "username"
            "text": "Great game!",
        }
    ]
}
"""