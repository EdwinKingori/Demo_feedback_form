from django.urls import path

from . import views

app_name = "profiles"
urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("/list/", views.ProfilesView.as_view()),
]
