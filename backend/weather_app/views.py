from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# request view
import requests
from django.http import JsonResponse

def get_weather_data(request, city):
    api_key = 'YOUR_API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # api_key = '895284fb2d2c50a520ea537456963d9c'
    # url = 'https://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid={api_key}'
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # weather_data = {
        #     'city': data['name'],
        #     'temperature': data['main']['temp'],
        #     'humidity': data['main']['humidity'],
        #     'wind_speed': data['wind']['speed']
        # }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'City not found'})