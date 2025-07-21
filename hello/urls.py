from django.urls import path
from hello import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("add/", views.add_movie, name="add_movie"),
    path("delete/<int:pk>/", views.delete_movie, name="delete_movie"),
    path("favorites/", views.favorite_list, name="favorite_list"),
    path("edit/<int:pk>/", views.edit_movie, name="edit_movie"),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
]

