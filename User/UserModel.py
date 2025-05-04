
from typing import List, Optional
from uuid import uuid4

from beanie import Document
from pydantic import Field
from typing import List, Dict
from sanic import json, text



class User(Document):
    id: str = Field(default_factory=lambda: str(uuid4()))
    username: str  # Kullanıcı adı
    password: str
    total_played_time: Optional[int] = 0  # Tüm oyunlarda harcanan toplam süre
    owned_games: List[dict] # Sahip olunan oyunlar listesi (alt özellikler dahil)
    most_played_game: Optional[str] = None  # En çok oynanan oyunların ID'leri (isteğe bağlı)

    class Settings:
        name = "users"  # MongoDB’deki koleksiyon adı


def to_dict(user) -> dict:
    return {
        "id": user.id,  # Sözlük tipi yerine attribute erişimi kullanıldı
        "username": user.username,
        "password": user.password,
        "total_played_time": user.total_played_time,
        "owned_games": user.owned_games,
        "most_played_game": user.most_played_game,
    }


def from_dict(data) -> User:
    return User(
        username=data["username"],
        password=data["password"],
        total_played_time=data.get("total_played_time", 0),
        owned_games=data.get("owned_games", []),
        most_played_game=data.get("most_played_games", None),
    )


