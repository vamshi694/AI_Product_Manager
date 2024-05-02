from dotenv import load_dotenv
from html_comps import avatar_html
import requests
import time
import os

load_dotenv(".env")

def generate_video(prompt, avatar_url):
    url = "https://api.d-id.com/talks"

    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization" : f"Basic {os.getenv('API_KEY_D_ID')}"
}
    payload = {
            "script": {
                # "type": "audio",
                # "audio_url": "https://path.to/audio.mp3",
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-US-AndrewMultilingualNeural"
                },
                "ssml": "false",
                "input": prompt
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0"
            },
            "source_url": avatar_url,
            
        }
    response = requests.post(url, json = payload, headers = headers)
    if response.status_code == 201:
        print(response.text)
        res = response.json()
        id = res["id"]
        status = "created"

        while status == "created":
            get_response = requests.get(f"{url}/{id}", headers = headers)
            print(get_response)

            if get_response.status_code == 200:
                status = res["status"]
                res = get_response.json()
                print(res)

                if res["status"] == "done":
                    video_url =  res["result_url"]
                else:
                    time.sleep(10)
            else:
                status = "error"
                video_url = "error"
    else:
            video_url = "error" 

    return avatar_html(video_url)