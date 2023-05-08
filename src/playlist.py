from datetime import timedelta
import isodate
import os
from googleapiclient.discovery import build
import json


class PlayList:
    api_key: str = os.getenv("API_KEY")
    YOUTUBE = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.playlist_videos1 = playlist_videos1 = self.YOUTUBE.playlists().list(id=self.video_id,
                                                                                 part='snippet',
                                                                                 maxResults=100
                                                                                 ).execute()
        self.title = self.playlist_videos1['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.video_id

        self.video = self.get_service()
        # print(type(self.video))
        # self.printj(self.video)
        # self.name = self.video['items'][1]['snippet']['title']

    def __str__(self):
        return self.title

    # def __repr__(self):
    #     return self.title

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def get_playlist_info(self):
        playlist_videos1 = self.YOUTUBE.playlists().list(id=self.video_id,
                                                         part='snippet',
                                                         maxResults=100
                                                         ).execute()
        # print(playlist_videos1['items'][0]['snippet']['title'])
        return playlist_videos1['items'][0]['snippet']['title']

    def get_service(self):
        urls = []

        playlist_items = self.YOUTUBE.playlistItems().list(
            part='snippet, contentDetails',
            playlistId=self.video_id,
            maxResults=500  # Максимальное количество результатов
        ).execute()
        for i in playlist_items['items']:
            # print(i['contentDetails']["videoId"])
            urls.append(i['contentDetails']["videoId"])

        return urls

    def get_video(self):
        urls = self.get_service()
        videos = []
        for i in urls:
            video_response = self.YOUTUBE.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=i
                                                        ).execute()
            videos.append(video_response)

        return videos

    @property
    def total_duration(self):
        '''Функуция выдает общую длительность видеозаписей'''
        r = self.get_video()
        duration = timedelta()
        for video in r:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video["items"][0]['contentDetails']['duration']
            duration1 = isodate.parse_duration(iso_8601_duration)
            duration += duration1
        # print(duration)
        return duration

    def show_best_video(self):
        likes_list = []
        likes = self.get_video()
        for i in likes:
            likes_list.append(int(i["items"][0]['statistics']['likeCount']))
        max_likes = max(likes_list)
        for j in likes:
            if int(j["items"][0]['statistics']['likeCount']) == max_likes:
                max_likes_video = 'https://youtu.be/' + j["items"][0]['id']
        return max_likes_video


