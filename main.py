import os
import requests
from dotenv import load_dotenv


load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORIZATION_URI = "https://www.warcraftlogs.com/oauth/authorize"
TOKEN_URI = "https://www.warcraftlogs.com/oauth/token" 
PUBLIC_URL = "https://www.warcraftlogs.com/api/v2/client"

QUERY = """
query($code:String){
  reportData {
    report(code: $code) {
        rankings(difficulty: 3, compare: Parses)
    }
  }
}

"""


def main():
    if os.path.isfile("access_token.txt"):
        access_token = read_data()
    else:
        access_token = get_access_token()
        write_data(access_token)
        access_token = read_data()

    player_dict = {}
    code = input("Please enter the Warcraft report code found on the ending of the url (E.g. https://sod.warcraftlogs.com/reports/THIS_CODE_HERE): ")

    data = get_data(QUERY, code=code)
    formated_data = data["data"]["reportData"]["report"]["rankings"]["data"]

    for item in formated_data[1::2]:     # Skipping the fightid, encounter, etc info
            for _, role in item["roles"].items():
                list_of_characters = role["characters"]
                
                for char in list_of_characters:
                    name = char.get('name')
                    rank_percent = char.get('rankPercent')

                    if type(rank_percent) == str:
                        rank_percent = 0
                    if name and rank_percent:
                        player_dict[name] = player_dict.get(name, 0) + int(rank_percent)


    sorted_data = [[k, v] for k, v in sorted(player_dict.items(), key=lambda item: item[1], reverse=True)]
    pickle_baller = sorted_data[0]
    pickle_receiver = sorted_data[-1]

    print(f"The pickle baller is {pickle_baller[0]}, with a total parse score of {pickle_baller[1]}!")
    print(f"The pickle reciever is {pickle_receiver[0]}, with a total measly parse score of {pickle_receiver[1]}!")


    
def get_access_token():
    response = get_token_response()
    if response.status_code != 200:
        print(f"Incorrect response from server with status code: {response.status_code}.")
        return
    
    response_json = response.json()
    access_token = response_json["access_token"]
    return access_token
    

def get_data(query, **kwargs):
    headers = get_headers()
    data = {"query": query, "variables": kwargs}
    with requests.Session() as sess:
        sess.headers = headers
        response = sess.get(PUBLIC_URL, json=data)
    return response.json()


def get_headers():
    access_token = get_access_token()
    return {"Authorization": f"Bearer {access_token}"}


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