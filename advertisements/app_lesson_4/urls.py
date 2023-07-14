from django.urls import path

from .views import example


urlpatterns = [
    path("", example),
    path("lesson_4", example)
]