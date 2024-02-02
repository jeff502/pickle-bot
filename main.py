import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("WARCRAFT_LOGS_APIKEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORIZATION_URI = "https://www.warcraftlogs.com/oauth/authorize"
TOKEN_URI = "https://www.warcraftlogs.com/oauth/token" 
PUBLIC_URL = "https://www.warcraftlogs.com/api/v2/client"


def main():
    response = get_token_response()
    if response.status_code != 200:
        print(f"Incorrect response from server with status code: {response.status_code}.")
        return
    
    response_json = response.json()
    access_token = response_json["access_token"]
    data = get_data(access_token)
    

    
def get_data(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    



def get_token_response():
    data = {"grant_type": "client_credentials"}
    user_data = (CLIENT_ID, CLIENT_SECRET)
    with requests.Session() as sess:
        response = sess.post(TOKEN_URI, data=data, auth=user_data)
    return response




if __name__ == "__main__":
    main()