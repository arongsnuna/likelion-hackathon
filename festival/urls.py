from django.urls import path
from . import views

urlpatterns = [
    path("", views.festival_list, name="festival_list"),
    path("<int:pk>", views.festival_detail, name="festival_detail"),
    path("search/", views.festival_search, name="festival_search"),
]