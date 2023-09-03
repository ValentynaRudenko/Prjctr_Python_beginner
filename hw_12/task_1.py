
import json
import requests
import os
from urllib import parse, request
from dotenv import load_dotenv
load_dotenv()


url = "http://api.giphy.com/v1/gifs/search"
MY_API_KEY = os.getenv('MY_API_KEY')
query = input("What do you want to find? Enter a word: ")
limit = input("How many options do you want? From 1 to 25: ")

params = parse.urlencode({
  "q": query,
  "api_key": MY_API_KEY,
  "limit": limit
})

with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

response_json_str = json.dumps(data, sort_keys=True, indent=4)

response_json = json.loads(response_json_str)
for i in range(int(limit)):
    print(response_json["data"][i]["bitly_url"])
