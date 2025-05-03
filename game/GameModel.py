from beanie import Document

class GameModel(Document):
    name: str
    genre: str
    photo: str
    playTimeOfGame: int
    totalRating: int = None
    allComments: list = None


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "genre": self.genre,
            "photo": self.photo,
            "playTimeOfGame": self.playTimeOfGame,
            "totalRating": self.totalRating,
            "allComments": self.allComments
        }

    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(
            name=data["name"],
            genre=data["genre"],
            photo=data["photo"],
            playTimeOfGame=data["playTimeOfGame"],
            totalRating=data.get("totalRating", None),
            allComments=data.get("allComments", None)
        )