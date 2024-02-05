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
QUERY = """
    query($code:String){
        reportData{
            report(code:$code){
                fights(difficulty:3){
                    id
                    name
                }
            }
        }
}
    """

def main():
    # if os.path.isfile("access_token.txt"):
    #     access_token = read_data()
    # else:
    #     access_token = get_access_token()
    #     write_data(access_token)
    #     access_token = read_data()

    access_token = get_access_token()
    code = "ypVWbwjAHQqCGJT7"
    data = get_data(access_token, QUERY, code=code)
    print(data)

    
def get_access_token():
    response = get_token_response()
    if response.status_code != 200:
        print(f"Incorrect response from server with status code: {response.status_code}.")
        return
    
    response_json = response.json()
    access_token = response_json["access_token"]
    return access_token
    
def get_data(access_token, query, **kwargs):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"query": query, "variables": kwargs}
    with requests.Session() as sess:
        sess.headers = headers
        response = sess.get(PUBLIC_URL, json=data)
    return response.json()


def write_data(data):
    with open("access_token.txt", "w+") as file:
        file.write(data)
    

def read_data():
    text = None
    with open("access_token.txt", "r") as file:
        text = file.readlines()
    return text

def get_token_response():
    data = {"grant_type": "client_credentials"}
    user_data = (CLIENT_ID, CLIENT_SECRET)
    with requests.Session() as sess:
        response = sess.post(TOKEN_URI, data=data, auth=user_data)
    return response




if __name__ == "__main__":
    main()