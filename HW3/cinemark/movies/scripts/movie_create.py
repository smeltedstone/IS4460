import requests
import json

api_url = 'http://localhost:8000/api/movie/'

movie_data = {
    "title": "Example Movie Title",
    "description": "This is an example description of the movie.",
    "director": "Director Name",
    "release_year": "2020",
    "budget": "5000000",
    "runtime": "120",
    "rating": "PG-13",
    "genre": "Action",
    "image_url": "http://example.com/movie-image.jpg",
    "youtube_url": "http://youtube.com/example-trailer"
}

response = requests.post(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Movie created successfully.")
else:
    print(f"Error creating movie. Status code: {response.status_code}")