import urllib.request
import json
import time


def get_json(url):
    request_urlopen = urllib.request.urlopen(url)
    response = request_urlopen.read().decode("utf-8")
    return response


request_end_point = "http://api.openweathermap.org/data/2.5"
request_api_name = "forecast"
request_appid = "d298334de2c10c2ffb1781632245f212"
request_city = "Minneapolis"
request_country = "us"
request_units = "imperial"

# "http://api.openweathermap.org/data/2.5/forecast?q=Minneapolis,us&units=imperial&appid=d298334de2c10c2ffb1781632245f212"
request = (request_end_point + "/" + request_api_name + "?q=" + request_city + "," + request_country + "&units="
           + request_units + "&appid=" + request_appid)
print(request)
json_response = get_json(request)

weather_json = json.loads(json_response)

for weather_json_object in weather_json['list']:
    date_time = weather_json_object['dt']
    date_time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_time))
    temp = weather_json_object['main']['temp']  # main is a dict
    weather_main = weather_json_object['weather'][0]['main']  # [weather] is a list, but take the first instance
    weather_description = weather_json_object['weather'][0]['description']
    print(

        "          <tr>\r\n" +
        "            <td>" + date_time_formatted + "</td>\r\n" +
        "            <td>" + weather_main + ": " + weather_description + "</td>\r\n" +
        "            <td>" + str(temp) + "\u00b0 F</td>\r\n" +
        "          </tr>")

