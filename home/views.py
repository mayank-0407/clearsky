from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    
    city=request.GET.get('entered_city')
    # city="patiala"
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1dbc234f1509d72a4aa482378a9afd82'
    data = requests.get(url).json()
    
    payload={'city':data['name'],
             'weather':data['weather'][0]['main'],
             'icon':data['weather'][0]['icon'],
             'celcius_temperature':data['main']['temp'],
             'kelvin_temperature':int(data['main']['temp'])-273,
             'pressure':data['main']['pressure'],
             'humidity':data['main']['humidity'],
             'description':data['weather'][0]['description'],
             }
    return render(request,"home/home.html",context={'data':payload})
