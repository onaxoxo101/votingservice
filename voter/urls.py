from django.contrib import admin
from django.urls import path
from .views import VoterListCreateView, SingleVoterView

urlpatterns = [
    path("", VoterListCreateView.as_view(), name="voter_list"),
    path("<int:pk>/", SingleVoterView.as_view(), name="single voter")
]