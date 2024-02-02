import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("WARCRAFT_LOGS_APIKEY")


def main():
    ...


if __name__ == "__main__":
    main()