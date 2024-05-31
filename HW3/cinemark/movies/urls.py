from django.urls import path
from . import views
from .views import redirect_view
urlpatterns = [
    # Regular Django views for rendering templates
    path('', redirect_view),
    path('movie/list/', views.movie_list, name='movie_list'),
    path('movie/<int:id>/', views.movie_details, name='movie_details'),
    path('movie/add/', views.movie_add, name='movie_add'),
    path('movie/update/<int:id>/', views.movie_update, name='movie_update'),
    path('movie/delete/<int:id>/', views.movie_delete, name='movie_delete'),
    
    # DRF API views for handling JSON requests
    path('api/movie/', views.MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('api/movie/<int:id>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail-update-delete'),
]