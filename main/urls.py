
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home" ),
    path('createNews', views.NewsList, name = "createNews"),
    path('NewsPaper', views.NewsPaper, name ="NewsPaper")
]