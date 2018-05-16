from django.urls import path

from . import views

app_name = "visits"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.article, name="article"),
]
