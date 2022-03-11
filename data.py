# we have considered importing the requests module over here
import requests

# we have considered a parameter as a dictionary over here
parameter = {
    "amount": 15, "type": "boolean"
}
# we basically consider a  response object over here
res = requests.get('https://opentdb.com/api.php?amount=15&category=18&difficulty=medium&type=boolean', params=parameter)
res.raise_for_status()

data = res.json()
# print(data["results"])

question_data = data["results"]

