import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemark_movies.settings')
django.setup()

from movies.models import Movie, User

# Empty existing rows
Movie.objects.all().delete()
User.objects.all().delete()

# Add 10 movie rows
movies = [
    Movie(title="1st Example Title", description="Description 1", director="Director 1", release_year="2021", budget="100M", runtime="120", rating="PG", genre="Action"),
    Movie(title="2nd Example Title", description="Description 2", director="Director 2", release_year="1986", budget="120M", runtime="120", rating="R", genre="Adventure"),
    Movie(title="3rd Example Title", description="Description 3", director="Director 3", release_year="2000", budget="110M", runtime="130", rating="PG", genre="Horror"),
    Movie(title="4th Example Title", description="Description 4", director="Director 4", release_year="2020", budget="130M", runtime="140", rating="R", genre="Noir"),
    Movie(title="5th Example Title", description="Description 5", director="Director 5", release_year="2024", budget="140M", runtime="150", rating="PG", genre="Fantasy"),
    Movie(title="6th Example Title", description="Description 6", director="Director 6", release_year="1940", budget="150M", runtime="160", rating="R", genre="Documentary"),
    Movie(title="7th Example Title", description="Description 7", director="Director 7", release_year="1960", budget="160M", runtime="170", rating="PG", genre="Drama"),
    Movie(title="8th Example Title", description="Description 8", director="Director 1", release_year="1968", budget="170M", runtime="180", rating="R", genre="Foriegn"),
    Movie(title="9th Example Title", description="Description 9", director="Director 9", release_year="1980", budget="180M", runtime="190", rating="PG", genre="Comedy"),
    Movie(title="10th Example Title", description="Description 10", director="Director 10", release_year="2001", budget="190M", runtime="200", rating="R", genre="Romance")
]

for movie in movies:
    movie.save()

# Add 3 user rows
users = [
    User(username="user1", password="password1", first_name="First1", last_name="Last1", email="user1@example.com"),
    User(username="user2", password="password2", first_name="First2", last_name="Last2", email="user2@example.com"),
    User(username="user3", password="password3", first_name="First3", last_name="Last3", email="user3@example.com")
]

for user in users:
    user.save()

# Retrieve all movies
Movie.objects.all()

# Filter for movies starting with some text
Movie.objects.filter(title__startswith='4')

# Get one movie (assuming you know the id or a unique field)
Movie.objects.get(pk=1)  # or any unique identifier

# Update one movie
movie_to_update = Movie.objects.get(pk=1)
movie_to_update.title = 'New Title'
movie_to_update.save()

# Delete one movie
movie_to_delete = Movie.objects.get(pk=2)
movie_to_delete.delete()

# Get data for user given a username
User.objects.get(username='user1')

#SQL Commands for finding a user. Find example attached in files. 

