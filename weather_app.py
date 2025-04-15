import requests
import sys

def weather(location, key):
    
    address = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"

    try:
        
        API_REQUEST = requests.get(address)
        
        
        if API_REQUEST.status_code == 200:
            final_data = API_REQUEST.json()

            city = final_data['name']
            country = final_data['sys']['country']
            temperature = final_data['main']['temp']
            humidity = final_data['main']['humidity']
            condition = final_data['weather'][0]['description']
            
            
            print(f"Weather in {city}, {country}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition.capitalize()}")
        else:
            print(f"Error: Could not retrieve weather data for '{location}'.")
            print(f"Response Code: {API_REQUEST.status_code}")
    except requests.exceptions.RequestException as e:
        
        print(f"Error occurred: {e}")

def main():
    key_1 = "eea825186c2965d2ed85eb065f65d03e"  
    location_1 = input("Enter the city name or ZIP code: ").strip()

    
    if not location_1:
        print("Please enter a valid city name or ZIP code.")
        sys.exit(1)

    
    weather(location_1, key_1)

if __name__ == "__main__":
    main()
