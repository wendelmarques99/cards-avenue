from django.urls import path
from cards.views import run

urlpatterns = [
    path("", run)
]