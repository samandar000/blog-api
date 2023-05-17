from django.urls import path
from .views import UserView, Users, CreateUser, PostsView, PostView

urlpatterns = [
    path('users/<int:id>', UserView.as_view()),
    path('users/', Users.as_view()),
    path('users/', CreateUser.as_view()),
    path('posts/', PostsView.as_view()),
    path('posts/<int:id>', PostView.as_view()),
]