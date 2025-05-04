from beanie import Document

class GameModel(Document):
    name: str
    genre: str
    photo: str
    playTimeOfGame: int
    totalRating: int = 0

    class Settings:
        name = "game"
        # MongoDB’deki koleksiyon adı


    def to_dict(self) -> dict:
        return {
            "id": str(self.id),  # Convert to string to make it JSON serializable
            "name": self.name,
            "genre": self.genre,
            "photo": self.photo,
            "playTimeOfGame": self.playTimeOfGame,
            "totalRating": self.totalRating,
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
            totalRating=data.get("totalRating", 0)
        )

"""
Pycharm'ın autocompete özelliğiyle oluşturulmuş bir örnek JSON. Post ederken kopyalamalık.
{
    "name": "Game Name",
    "genre": "Action",
    "photo": "http://example.com/photo.jpg",
    "playTimeOfGame": 120,
}
"""