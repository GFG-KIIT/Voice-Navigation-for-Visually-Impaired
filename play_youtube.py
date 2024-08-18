import googleapiclient.discovery as gacd
from dotenv import load_dotenv
import webbrowser
load_dotenv()
from os import environ
youtubeApiKey=environ['YOUTUBE_API_KEY']
client=gacd.build(
    'youtube',
    'v3',
    developerKey=youtubeApiKey
)
def search_video(client, searchItem):
    response=client.search().list(
        part="snippet",
        maxResults=10,
        q=searchItem,
        type="video"
    ).execute()
    return response
def play_video(topic):
    search_results=search_video(client, topic)
    webbrowser.open(f"https://www.youtube.com/watch?v={search_results['items'][0]['id']['videoId']}")