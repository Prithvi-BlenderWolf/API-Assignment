import requests

url = "https://api.themoviedb.org/3/movie/top_rated?api_key=cd2a14c75563ecb0b6ea8a8fead1de34&language=en-US&page=1"

response = requests.get(url)
code = response.status_code

assert code==200 , "Code doesn't match"
json_response = response.json()
assert json_response['total_pages'] == 546, "Total pages is not matching"
