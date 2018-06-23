import requests
import json

def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')

    json_data = get_json_from_web(code)

    string_data = json_to_string(json_data)

    print(f"The temp in {string_data['city']} is {string_data['temp']} degrees and {string_data['cond']}")


def print_the_header():
    print("-------------------------------")
    print("         WEATHER APP")
    print("-------------------------------\n")


def get_json_from_web(zipcode):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&units=imperial&appid=1f5e7c4686890d545c6357c1b630666e"
    response = requests.get(url)

    converted_to_dict_data = json.loads(response.text)

    return converted_to_dict_data


def json_to_string(json_data):
    json_object = {"cond": json_data['weather'][0]['main'],\
                   "temp": json_data['main']['temp'],\
                   "city": json_data['name']}

    return json_object


if __name__ == "__main__":
    main()