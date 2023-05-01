
import os
from googleapiclient.discovery import build
import json


class Video:
    api_key: str = os.getenv("API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.url = 'https://youtu.be/' + self.video_id
        self.video = self.get_service()
        # print(type(self.video))
        # self.printj(self.video)
        self.views = self.video['items'][0]['statistics']['viewCount']
        self.likes = self.video['items'][0]['statistics']['likeCount']
        self.name = self.video['items'][0]['snippet']['title']

    def __str__(self):
        return self.name

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def get_service(self) -> None:
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=self.video_id
                                                    ).execute()
        return video_response


class PLVideo():
    api_key: str = os.getenv("API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id, PL_id):
        self.video_id = video_id
        self.url = 'https://youtu.be/' + self.video_id
        self.PL_id = PL_id
        self.video = self.get_service()
        # print(type(self.video))
        # self.printj(self.video)
        self.name = self.video['items'][1]['snippet']['title']

    def __str__(self):
        return self.name

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def get_service(self):
        # playlist_videos = self.YOUTUBE.playlists().list(id=self.PL_id,
        #                                                 part='snippet',
        #                                                 maxResults=100
        #                                                 ).execute()
        playlist_items = self.YOUTUBE.playlistItems().list(
            part='snippet',
            playlistId=self.PL_id,
            maxResults=50  # Максимальное количество результатов
        ).execute()

        return playlist_items
