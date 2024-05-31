import requests

id = 3

api_url = f'http://localhost:8000/api/movie/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print("Movie deleted successfully.")
else:
    print(f"Error deleting the movie. Status code: {response.status_code}")
