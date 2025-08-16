import requests
import os 
from dotenv import load_dotenv

load_dotenv()




def get_token():
    headers = {
             "Accept": "application/json",
             "Content-Type": "application/x-www-form-urlencoded",
        }


    data = {
            'client_id': os.getenv("client_id"),
            'client_secret': os.getenv("client_secret"),
            'grant_type': 'client_credentials',
            'scope': 'public'
        }

    res = requests.post("https://osu.ppy.sh/oauth/token", data=data, headers=headers)
    return res.json()['access_token'] 






