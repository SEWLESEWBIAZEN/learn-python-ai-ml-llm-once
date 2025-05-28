import requests

# Setup api key
API_KEY ="d77ff13a2361a4cdbb2dbf82b8c81318"
APP_URL = f"https://api.openweathermap.org/data/2.5/weather"

#  Get weather
def get_weather(city):
    FULL_URL = f"{APP_URL}?q={city}&appid={API_KEY}"
    try:
        response = requests.get(FULL_URL)
        data = response.json()
        if response.status_code == 200:              
            weather={
                "City":data['name'],
                "Temprature":f"{data['main']['temp']}C",
                "Weather":f"{data['main']['humidity']}%",
                "Wind Speed":f"{data['wind']['speed']}m/s"
            }
            return weather
        elif response.status_code == 404:
            print ("City is not found")
        else:
            print("An error occured. Status Code: ", response.status_code)
    except Exception as e:
        print("An Exception occurred.",e)
    return None

# display weather
def display_weather(weather):
    for key,value in weather.items():
        print(f"{key}: {value}")

# main method, app entry
def main():
    while True:
        print("\n Weather App.")
        city = input("Enter the city name: or q to quit: ")
        if(city.lower()=='q'):
            break

        weather = get_weather(city)
        if(weather):
            display_weather(weather)

# calling app entry
main()

