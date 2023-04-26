import os
from googleapiclient.discovery import build
import json

api_key: str = os.getenv("API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv("API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']


    def __add__(self, other):
        return f'{int(self.viewCount) + int(other.viewCount)}  {self.viewCount}  {other.viewCount}'

    def __sub__(self, other):
        return f'{int(self.viewCount) - int(other.viewCount)}  {self.viewCount}  {other.viewCount}'


    def __gt__(self, other):
        return f'{int(self.viewCount) > int(other.viewCount)}'

    def __ge__(self, other):
        return f'{int(self.viewCount) >= int(other.viewCount)}'

    def __lt__(self, other):
        return f'{int(self.viewCount) < int(other.viewCount)}'

    def __le__(self, other):
        return f'{int(self.viewCount) <= int(other.viewCount)}'

    def __str__(self):
        return f'https://www.youtube.com/channel/{self.channel_id}'

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel['items']['snippet']['title'], indent=2, ensure_ascii=False))
        # print(channel['items'][0]['snippet']['title'])
        # print(channel['items'][0]['statistics']['videoCount'])
        # print(f'https://www.youtube.com/channel/{self.chanell_id}')


    def to_json(self, filename):
        data = {"chanell_id": self.channel_id, "title": self.title, "video_count": self.video_count, "url": self.url}
        with open(filename, "w") as f:
            json.dump(data, f, ensure_ascii=False)

    @classmethod
    def get_service(cls) -> None:
        chanel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
        channel = youtube.channels().list(id=chanel_id, part='snippet,statistics').execute()
        title = channel['items'][0]['snippet']['title']
        video_count = channel['items'][0]['statistics']['videoCount']
        url = f'https://www.youtube.com/channel/{chanel_id}'
        channel_instance = cls(chanel_id)
        channel_instance.title = title
        channel_instance.video_count = video_count
        channel_instance.url = url
        channel_instance.to_json("channel.json")
        return youtube

    # channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        # title = channel['items'][0]['snippet']['title']
        # video_count = channel['items'][1]['statistics']['title']
        # url = f'https://www.youtube.com/channel/{channel_id}'



