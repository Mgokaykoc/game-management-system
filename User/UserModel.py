from typing import List, Optional
from uuid import uuid4

from beanie import Document
from pydantic import Field
from typing import List, Dict
from sanic import json, text


class User(Document):
    username: str
    password: str
    total_play_time: int = 0  # Tüm oyunlarda harcanan toplam süre
    most_played_game: str = None  # En çok oynanan oyun (isim)

    class Settings:
        name = "users"  # MongoDB’deki koleksiyon adı


def to_dict(user) -> dict:
    return {
        "id": str(user.id),  # Convert to string to make it JSON serializable
        "username": user.username,
        "password": user.password,
        "total_played_time": user.total_play_time,
        "most_played_game": user.most_played_game,
    }


def from_dict(data) -> User:
    return User(
        username=data["username"],
        password=data["password"],
        total_play_time=data.get("total_play_time", 0),
        most_played_game=data.get("most_played_game", None)
    )


"""
Pycharm'ın autocompete özelliğiyle oluşturulmuş bir örnek JSON. Post ederken kopyalamalık.
{
    "username": "example_user",
    "password": "example_password",
    "total_play_time": 120,
    "most_played_game": "Game Name"
}
"""
