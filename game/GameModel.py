from beanie import Document

class GameModel(Document):
    name: str
    genre: str
    photo: str
    playTimeOfGame: int = 0
    weightedSumOfPlayTimes: int = 0

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
            "TotalRating": self.weightedSumOfPlayTimes/self.playTimeOfGame if self.playTimeOfGame > 0 else 0,
        }


    @classmethod
    def from_dict(cls, data):
        #cls demek class'ın kendisi demek. JSON olarak gönderilen isteği
        #yorumun yarısı kesilmiş ama objeye dönüştürüyo diyecektim herhalde
        return cls(
            name=data["name"],
            genre=data["genre"],
            photo=data["photo"]
        )

"""
Pycharm'ın autocompete özelliğiyle oluşturulmuş bir örnek JSON. Post ederken kopyalamalık.
{
    "name": "game Name",
    "genre": "Action",
    "photo": "http://example.com/photo.jpg"
}
"""