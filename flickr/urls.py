from django.urls import path
from . import views

app_name='flickr'
urlpatterns =[
    path('', views.index, name='index'),
    path('search/<str:user_id>/', views.search, name='search')
]