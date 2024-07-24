# trivia_fetcher.py
import requests

def fetchdata():
    url = "https://opentdb.com/api.php?amount=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])
    else:
        raise Exception(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
