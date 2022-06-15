
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("posts", views.compose, name="compose"),
    path("posts/<str:action>", views.posts, name ="posting"),
    path("profile/<int:user_id>", views.profile, name="profile"),
]