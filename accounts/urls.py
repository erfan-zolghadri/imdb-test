from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", authtoken_views.obtain_auth_token, name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
