from django.contrib import admin
from django.urls import path, include
from mainpage import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('exhibitions/', include("exhibition.urls")),
    path('festivals/', include("festival.urls")),
    path('accounts/', include('allauth.urls')),
    path('post/', include("post.urls")),

    path('', views.home, name="home")
]
