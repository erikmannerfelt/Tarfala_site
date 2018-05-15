from django.urls import path

from . import views

app_name = "glaciers"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.article, name="article"),
    path("massifs/", views.MassifView.as_view(), name="massifs"),
    path("massifs/<int:pk>/", views.MassifGlacierView.as_view(), name="massif_glaciers"),
]