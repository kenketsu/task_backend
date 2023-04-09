from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("profile", views.ProfileViewSet)

urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view(), name="create"),
    path("login-user/", views.LoginUserRetrieveAPIView.as_view(), name="login-user"),
    path("", include(router.urls)),
]
