#custome tool

from typing import List, Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi


class VideoSearchResult(BaseModel):
    video_id: str
    title: str
    channel_id: str
    channel_title: str
    video_description: str
    transcript: str
    

class YoutubeVideoSearchToolInput(BaseModel):
    keyword: str = Field(..., description="The search keyword.")
    max_results: int = Field(20, description="The number of results to return.")


class YoutubeVideoSearchTool(BaseTool):
    name: str = "Search YouTube Videos"
    description: str = "Searches YouTube videos based on a keyword and returns a list of video search results."
    args_schema: Type[BaseModel] = YoutubeVideoSearchToolInput

    def _run(self, keyword: str, max_results: int = 20) -> List[VideoSearchResult]:
        api_key = os.getenv("YOUTUBE_API_KEY")
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        items = response.json().get("items", [])

        results = []
        for item in items:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            channel_id = item["snippet"]["channelId"]
            channel_title = item["snippet"]["channelTitle"]
            video_description = item["snippet"]["description"]
            transcript=""
            try:
                transcriptArr = YouTubeTranscriptApi.get_transcript(video_id)
                for line in transcriptArr:
                    transcript = transcript + line['text'] + " "
            except Exception as e:
                transcript = "Transcript not available"  
            results.append(VideoSearchResult(
                video_id=video_id,
                title=title,
                channel_id=channel_id,
                channel_title=channel_title,
                video_description=video_description,
                transcript=transcript
            ))
            
        #creating a new file and then append all of the output of the search tool to the file
        try:
            #give desired location
            path = "yourPath/result/report.txt"
            ptr = 1
            with open(path, 'a', encoding="utf-8") as file:
                for result in results:
                    file.write(str(ptr) + ". " + "Video ID: " + result.video_id)
                    file.write("\nVideo Title: "+ result.title)
                    file.write("\nYT Channel ID: "+ result.channel_id)
                    file.write("\nYT Channel Title: "+ result.channel_title)
                    file.write("\nVideo description: "+ result.video_description)
                    file.write("\nVideo Transcript: "+ result.transcript)
                    file.write("\n"+"-" * 20 + "\n\n\n\n")
                    ptr = ptr + 1
                file.close()
        except Exception as e:
            return e    

        return results
 
