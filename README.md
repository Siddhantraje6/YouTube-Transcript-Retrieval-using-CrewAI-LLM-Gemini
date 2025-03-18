# YouTube Transcript Retrieval using CrewAI (LLM-Gemini)

This project aims at automating the proccess of fetching YouTube Video Transcripts with the help of CrewAI library

The project makes use of custom tool which queries the YouTube regarding the specified input, gets the video details as well as Transcripts, and then stores them in an output file.

## Demo


https://github.com/user-attachments/assets/b55d09ef-0d89-49ab-9b25-3202edf5ffa7


## Run Locally

Clone the project

```bash
  git clone https://github.com/Siddhantraje6/YouTube-Transcript-Retrieval-using-CrewAI-LLM-Gemini
```

Install poetry
- [Installation guide (for pipx)](https://python-poetry.org/docs/#installing-with-pipx)
```bash
python -m pip install --user pipx 
python -m pipx ensurepath # Add pipx to PATH
pipx install poetry 
pipx inject poetry poetry-plugin-shell
```

Install dependencies from pyproject.toml with poetry

```bash
  poetry install --no-root
```

Finally run the command

```bash
  crewai run
```




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MODEL`

`GEMINI_API_KEY`

`YOUTUBE_API_KEY`




## API Reference
By default all of the CrewAI agents and tools use OPENAI as their LLM provider (paid only) but this can be changed by specificaly 
mentioning Gemini as our LLM provider.
We can generate our api keys from Google cloud console, Google has its own free tier.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `GEMINI_API_KEY` | `string` | **Required**. LLM provider  |


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `YOUTUBE_API_KEY`      | `string` | **Required**. For Transcription |



## Appendix

It is important to know that to run the project successfully, one needs to configure the environment appropriately without any errors (even I struggled a lot with setting up right environment), sometimes installation and execution may take very long time.

Based upon the query (input), the tool finds the most relevant 20 videos (you can change this param), not all might have transcripts enabled, in that case
the transcript field shall be left empty.



## Support

For support, email siddhant.raje.5g@gmail.com

## Acknowledgements

 - [bhancockio](https://github.com/bhancockio)
