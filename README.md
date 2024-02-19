# pickle-bot

## Description

This program is designed to analyze Warcraft Logs and determine the top performer based on individual class performance and their parses within their given role.

## Features

- Analyzes Warcraft Logs data to identify top performers.
- Allows users to specify which raid report to analyze top performer(s).

### Installation

1. Clone this repository to your local machine using the following command in your terminal:
  `git clone https://github.com/jeff502/pickle-bot.git`
2. Navigate to the project directory:
  `cd file/path/here`
3. Install dependencies:
    `pip install -r requirements.txt`

4. Obtain a Client ID and Client Secret:
- Sign up and obtain a Client ID/Secret from [Warcraft Logs API Clients](https://www.warcraftlogs.com/api/clients/).

5. Create a `.env` file.

6. Add Client ID and Secret to the newly formed `.env` file using the `.env.example` file as a reference.

7. Run the script and give a Warcraft Logs report code found at the end of a URL: `https://vanilla.warcraftlogs.com/reports/REPORT-CODE-HERE`
  `python main.py`

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

This program utilizes the Warcraft Logs API for retrieving and analyzing raid data.
Special thanks to the creators of Warcraft Logs for providing such a valuable resource for the Warcraft community.
