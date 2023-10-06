from django.urls import path
from .views import workout

urlpatterns = [
    path("", workout, name="index"),

]