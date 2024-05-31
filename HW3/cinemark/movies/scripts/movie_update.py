import requests
import json

# Specify the ID of the movie you want to update
id = 1

api_url = f'http://localhost:8000/api/movie/{id}/'

movie_data = {
    "title": "Updated Movie Title",
    "description": "This is an updated description of the movie.",
    "director": "Updated Director Name",
    "release_year": "2021",
    "budget": "6000000",
    "runtime": "130",
    "rating": "PG-13",
    "genre": "Adventure",
    "image_url": "http://example.com/updated-movie-image.jpg",
    "youtube_url": "http://youtube.com/updated-example-trailer"
}

response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Movie updated successfully.")
else:
    print(f"Error updating the movie. Status code: {response.status_code}")