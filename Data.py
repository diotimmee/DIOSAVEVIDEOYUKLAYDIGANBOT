import requests


def post_instagram_video(video_url):
    url = ""
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "video_url": video_url
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


