import requests

id = 1

api_url = f'http://localhost:8000/api/movie/{id}/'

response = requests.get(api_url)

if response.status_code == 200:
    movie_data = response.json()
    print(movie_data)
else:
    print("Error retrieving the movie.")
