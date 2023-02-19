from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view(), name="create"),
    path("users", views.UserListAPIView.as_view(), name="users"),
    path("login-user/", views.LoginUserRetrieveAPIView.as_view(), name="login-user"),
]
