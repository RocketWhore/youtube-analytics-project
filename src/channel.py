import os
from googleapiclient.discovery import build
import json

import printj
class Channel:
    """Класс для ютуб-канала"""
# api_key: str = os.getenv("API_KEY")
# print(api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.chanell_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv("API_KEY")
        print(api_key)
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.chanell_id, part='snippet,statistics').execute()

        printj(channel)


def printj(dict_to_print: dict):
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))