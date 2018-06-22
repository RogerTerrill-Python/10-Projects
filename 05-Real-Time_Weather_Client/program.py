import requests


def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')

    html = get_html_from_web(code)


    # display for the forecast
    print("Hello from main")


def print_the_header():
    print("-------------------------------")
    print("         WEATHER APP")
    print("-------------------------------\n")


def get_html_from_web(zipcode):
    url = f"https://www.wunderground.com/weather/us/ca/silverado/{zipcode}"
    response = requests.get(url)
    print(response.text[0:250])

    return response.text


if __name__ == "__main__":
    main()