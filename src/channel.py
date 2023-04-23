import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.chanell_id = channel_id
        self.title = None
        self.video_count = None
        self.url = None


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel = youtube.channels().list(id=self.chanell_id, part='snippet,statistics').execute()
        print(json.dumps(channel['items']['snippet']['title'], indent=2, ensure_ascii=False))
        # print(channel['items'][0]['snippet']['title'])
        # print(channel['items'][0]['statistics']['videoCount'])
        # print(f'https://www.youtube.com/channel/{self.chanell_id}')


    def to_json(self, filename):
        data = {"chanell_id": self.chanell_id, "title": self.title, "video_count": self.video_count, "url": self.url}
        with open(filename, "w") as f:
            json.dump(data, f)

    @classmethod
    def get_service(cls, chanel_id: str) -> None:
        channel = youtube.channels().list(id=chanel_id, part='snippet,statistics').execute()
        title = channel['items'][0]['snippet']['title']
        video_count = channel['items'][1]['statistics']['title']
        url = f'https://www.youtube.com/channel/{chanel_id}'
        channel_instance = cls(chanel_id)
        channel_instance.title = title
        channel_instance.video_count = video_count
        channel_instance.url = url
        channel_instance.to_json("channel.json")

    # channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        # title = channel['items'][0]['snippet']['title']
        # video_count = channel['items'][1]['statistics']['title']
        # url = f'https://www.youtube.com/channel/{channel_id}'



