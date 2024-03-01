from django.urls import path
from .views import ViewsRegister, close_session, login_session

urlpatterns = [
    path("", ViewsRegister.as_view(), name = "Authentication"),
    path("close_session", close_session, name = "Close_session"),
    path("login", login_session, name = "Login")
]
