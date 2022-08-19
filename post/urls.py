from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('freeposts/', views.freeposts, name='freeposts_list'),
    path('reviewposts/', views.reviewposts, name='reviewposts_list'),
    path('withposts/', views.withposts, name='withposts_list'),
    #path('freedetail/<int:pk>', views.freePostDetail, name='freeposts_detail'),
]