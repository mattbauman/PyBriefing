import urllib.request
import json
import datetime
import time
import platform
import os


def get_json(url):
    request_urlopen = urllib.request.urlopen(url)
    response = request_urlopen.read().decode("utf-8")
    return response


def write_tr(write_date_time, write_weather_main, write_temp):
    php_out.write(

        "<tr>\n" +
        "\t<td>" + write_date_time + "</td>\n" +
        "\t<td>" + write_weather_main + "</td>\n" +
        "\t<td>" + str(write_temp) + "&#176;F</td>\n" +
        "</tr>"
    )


def write_current(write_current_date_time, write_current_weather_main, write_current_temp):
    print(
        write_current_date_time +
        write_current_weather_main +
        str(write_current_temp)
    )


def card_start(weekday, yyyy_mm_dd):
    php_out.write(
        '<div class="w3-card-4 w3-margin w3-white">' +
        'Weather (Minneapolis) - <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap</a>\n')
    php_out.write('<div class ="w3-container">\n')
    php_out.write('<h5><b>' + weekday + ', ' + yyyy_mm_dd + '</h5></b>\n')
    php_out.write('<table>\n')


def card_end():
    php_out.write('</table>\n')
    php_out.write('</div>\n')
    php_out.write('</div>\n')


def get_day_of_week(day_of_week_int):
    if day_of_week_int == 0:
        return "Monday"
    elif day_of_week_int == 1:
        return "Tuesday"
    elif day_of_week_int == 2:
        return "Wednesday"
    elif day_of_week_int == 3:
        return "Thursday"
    elif day_of_week_int == 4:
        return "Friday"
    elif day_of_week_int == 5:
        return "Saturday"
    elif day_of_week_int == 6:
        return "Sunday"


if platform.system() == "Linux":
    path = "/opt/bitnami/apache2/htdocs/mattbauman.com/briefing/"
else:
    path = "C:/Users/matt/Documents/GitHub/PyBriefing/"

completeName = os.path.join(path, "weather.php")
php_out = open(completeName, "w")
request_end_point = "http://api.openweathermap.org/data/2.5"
OpenWeatherMap_key = open(path + "OpenWeatherMap_key.txt", "r")
request_appid = OpenWeatherMap_key.read()
request_city = "Minneapolis"
request_country = "us"
request_units = "imperial"

# Current Weather
request_api_name = "weather"
current_weather = (request_end_point + "/" + request_api_name + "?q=" + request_city + "," + request_country + "&units="
                   + request_units + "&appid=" + request_appid)
current_weather_json_response = get_json(current_weather)
current_weather_json = json.loads(current_weather_json_response)
current_main = current_weather_json['weather'][0]['main']
current_temp = current_weather_json['main']['temp']
current_temp_str = str(round(float(current_temp)))
current_wind_speed = current_weather_json['wind']['speed']
current_dt_int = current_weather_json['dt']
current_dt_tm_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_dt_int))
current_date_str = str(current_dt_tm_formatted)[0:10]
current_time_str = str(current_dt_tm_formatted)[11:16]
current_time_str = datetime.datetime.strptime(current_time_str, '%H:%M').strftime('%I:%M %p')

request_api_name = "forecast"
# "http://api.openweathermap.org/data/2.5/forecast?q=Minneapolis,us&units=imperial&appid=d298334de2c10c2ffb1781632245f212"
request = (request_end_point + "/" + request_api_name + "?q=" + request_city + "," + request_country + "&units="
           + request_units + "&appid=" + request_appid)
json_response = get_json(request)
weather_json = json.loads(json_response)
date_last = ""
for weather_json_object in weather_json['list']:
    date_time = weather_json_object['dt']
    date_time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_time))
    date_str = str(date_time_formatted)[0:10]
    time_str = str(date_time_formatted)[11:16]
    time_str = datetime.datetime.strptime(time_str, '%H:%M').strftime('%I:%M %p')
    temp_str = weather_json_object['main']['temp']  # main is a dict
    temp = str(round(float(temp_str)))
    weather_main = weather_json_object['weather'][0]['main']  # [weather] is a list, but take the first instance
    # weather_description = weather_json_object['weather'][0]['description']

    date_weekday_int = datetime.date(int(date_str[0:4]), int(date_str[5:7]), int(date_str[8:10])).weekday()
    date_weekday = get_day_of_week(date_weekday_int)

    if date_last == "":  # first
        card_start(date_weekday, date_str)
        if current_date_str == date_str:
            write_tr(current_time_str, current_main, current_temp_str)
    elif date_last != date_str:
        card_end()
        card_start(date_weekday, date_str)
    write_tr(time_str, weather_main, temp)
    date_last = date_str
card_end()
