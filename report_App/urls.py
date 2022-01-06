from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('download_data/', views.download_data, name='download_data'),
]