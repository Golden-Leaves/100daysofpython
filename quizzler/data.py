import requests

open_trivia_db_parameters = {
    "amount": 200,
    "type": "boolean",

}
open_trivia_db_response = requests.get(url = "https://opentdb.com/api.php?", params = open_trivia_db_parameters)
open_trivia_db_response.raise_for_status()
open_trivia_db_data = open_trivia_db_response.json()
question_data = open_trivia_db_data["results"]

#if __name__ == "__main__":
    #main()

