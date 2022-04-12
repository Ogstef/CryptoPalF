from django.urls import path
from . import views

app_name = "website"


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name ="about"),
    path("rate",views.rate, name="rate"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profpage, name="profpage"),
    path("contact", views.contact, name="contact"),
    path("searched", views.search, name="search")
]