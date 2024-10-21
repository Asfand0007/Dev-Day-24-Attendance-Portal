from django.urls import path
from .views import landingpage

app_name = "attendance"
urlpatterns = [
    path("", landingpage, name="landing_page"),
]
