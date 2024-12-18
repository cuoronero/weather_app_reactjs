from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('weather/<str:city>/', views.get_weather_data, name='weather_data'),
]

