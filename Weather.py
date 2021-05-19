  
import requests


def weather_data(query):
    res = requests.get('http://api.openweathermap.'
                       'org/data/2.5/weather?'
                       + query +
                       '&appid=a1c86d677225cae3648789045729a448&units='
                       'metric')
    return res.json()


def print_weather(result, city):
    Temperature = ("{}'s temperature: {}°C ".
                   format(city, result['main']['temp']))
    WindSpeed = ("Wind speed: {} m/s".
                 format(result['wind']['speed']))
    Discription = ("Description: {}".
                   format(result['weather'][0]['description']))
    Weather = ("Weather: {}".format(result['weather'][0]['main']))
    print(Temperature)
    print(WindSpeed)
    print(Discription)
    print(Weather)
    return Temperature


def main():
    city = 'Tampere'

    try:
        query = 'q='+city
        w_data = weather_data(query)
        print_weather(w_data, city) 
         

    except:
        print('City name not found...')

main()
print(Temperature)