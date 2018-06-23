import requests
import json


def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')

    json_data = get_json_from_web(code)

    cond = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    city = json_data['name']

    report = WeatherData().data(cond, temp, city)

    print(f"The temp in {report.city} is {report.temp} degrees and {report.cond}")


def print_the_header():
    print("-------------------------------")
    print("         WEATHER APP")
    print("-------------------------------\n")


def get_json_from_web(zipcode):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&units=imperial&appid=1f5e7c4686890d545c6357c1b630666e"
    response = requests.get(url)

    converted_to_dict_data = json.loads(response.text)

    return converted_to_dict_data


class WeatherData:
    def data(self, cond, temp, city):
        self.cond = cond
        self.temp = temp
        self.city = city
        return self




def get_weather_from_json(json_tuple):
    condition = json_tuple['weather']['main']
    temp = json_tuple['main']['temp']
    city = json_tuple['sys']['name']

    return temp


if __name__ == "__main__":
    main()