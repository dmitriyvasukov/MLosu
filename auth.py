import requests





def get_token():
    client_id = 43370
    client_secret = 'RmI7HF6V8gXTERCcm21a794w5zvuxXOA1L8UU1NF'
    headers = {
             "Accept": "application/json",
             "Content-Type": "application/x-www-form-urlencoded",
        }


    data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials',
            'scope': 'public'
        }

    res = requests.post("https://osu.ppy.sh/oauth/token", data=data, headers=headers)
    return res.json()['access_token'] 






