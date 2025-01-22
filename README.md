# YouTube Transcript Retrieval using CrewAI (LLM-Gemini)

This project aims at automating the proccess of fetching YouTube Video Transcripts with the help of CrewAI library

The project makes use of custom tool which queries the YouTube, gets the video details as well as Transcripts, and then stores them in an output file.

## Demo

https://github.com/user-attachments/assets/b55d09ef-0d89-49ab-9b25-3202edf5ffa7




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MODEL`

`GEMINI_API_KEY`

`YOUTUBE_API_KEY`




## API Reference

You can generate your api keys from Google cloud console, and most importantly Google does not charge for making api calls and using their LLM until its enterprise version.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `GEMINI_API_KEY` | `string` | **Required**. LLM provider  |


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `YOUTUBE_API_KEY`      | `string` | **Required**. For Transcription |


## Acknowledgements

 - [bhancockio](https://github.com/bhancockio)
