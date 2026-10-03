from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city="Kathmandu"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978"
    data=requests.get(url,{'units':"metric"}).json()

    
    temp=data['main']['temp']
    pressure=data['main']['pressure']
    humidity=data['main']['humidity']
    speed=data['wind']['speed']
    temp_min=data['main']['temp_min']
    temp_max=data['main']['temp_max']
    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    visibility=data['visibility']

    city_url=f"https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id=20Z-uMm25czNIdLHvAhFrpcYplKY2CpDpb7FxZN1ods"
    # city_response = requests.get(city_url).json()
    city_data = requests.get(city_url).json()
    city_img = None
    if city_data.get("results"):
        city_img = city_data["results"][0]["urls"]["regular"]
    

    return render(request,'index.html',{'temp':temp,'city':city,'pressure':pressure,
                                        'humidity':humidity,'visibility':visibility,
                                        'speed':speed,'temp_min':temp_min,'description':description,
                                         'temp_max':temp_max,'icon':icon,'city_img':city_img })