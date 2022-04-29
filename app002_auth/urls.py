from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="log_in"),
    path("logout/", views.log_out, name="log_out"),
    path("sign_up/", views.sign_up, name="sign_up")
]
