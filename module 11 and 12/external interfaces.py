"""
import requests

def get_chuck_norris_joke():
    ur1 = "https://api.chucknorris.io/jokes/random"
    response = requests.get(ur1)
    data = response.json()
    return data["value"]

def main():
    joke = get_chuck_norris_joke()
    print(joke)

if __name__ == '__main__':
    main()

"""

import requests

def main():
    city = input("Enter municipality name: ")

    api_key = "9878e9af551b658e0bb3deaccbe3a6e8"
    ur1 = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(ur1)
    data = response.json()

    if response.status_code == 200:
        print("Error: could not fetch weather data!")
        return

    description = data["weather"][0]["description"]

    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {temp_celsius:.1f} °C")

if __name__ == "__main__":
    main()
