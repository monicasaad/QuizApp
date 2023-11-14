import requests

# parameters to pass into get request - amount for # of q's, type for type of question (T/F, mcq)
parameters = {
    "amount": 10,
    "type": "boolean"
}

# get question data from open trivia api
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # check for exceptions
data = response.json()  # extract json data from api

question_data = data["results"]  # select out data for questions and save to a new variable
