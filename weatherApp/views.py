from django.shortcuts import render

# Becasue we will have POST type of request so, we nee to import request
import  urllib.request
import json
# Because we nee to convert jason to python dictionary
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+
                                        city + '&units=metric&appid=eb107ed9a90cff9a7d61b6bb686068e1').read()
        list_of_data = json.loads(source)

        #The main data dictionary
        data = {
            "country_code": str(list_of_data['sys']['country']),
            # "coordinate": str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "feels_like": str(list_of_data['main']['feels_like']),
            "temp_min": str(list_of_data['main']['temp_min']),
            "temp_max": str(list_of_data['main']['temp_max']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }
        # print(data)
    else:
        data = {}
    return render(request, 'main/index.html', data)
