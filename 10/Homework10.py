
import requests
weather_response = requests.get ('https://api.forecast.io/forecast/64f4867f7d4c86182f3d1c6ed881dbfc/40.7142700,-74.0059700')
weather_data = weather_response.json()
daily_weather = weather_data['daily']['data']
temperature = weather_data['currently']['temperature']


summary = daily_weather[0]['summary']

high_temp = daily_weather[0]['temperatureMax']
low_temp = daily_weather[0]['temperatureMin']
hot_limit= 80
cold_limit = 68

if high_temp > hot_limit:
    temp_feeling = "Slightly Hot"
if high_temp > cold_limit and high_limit < hot_limit:
    temp_feeling = "Just about Perfect"
if high_temp < cold_limit:
    temp_feeling = "Cool"

rain_probability = daily_weather[0]['precipProbability']
rain_likelihood = rain_probability * 100

if rain_likelihood < 20:
    rain_warning = "No chances of Rain."
if rain_likelihood > 20 and rain_likelihood < 30:
    rain_warning = "A very faint possibility of Rain. You could always get Umbrellas for 5 dollars."
if rain_likelihood > 30 and rain_likelihood < 60:
    rain_warning = "You wouldn't want to take chances. Carry an Umbrella"
if rain_likelihood > 60:
    rain_warning = "It looks like Rain is on the cards. Leaky Subway Stairs, coming right up."
if rain_likelihood > 80:
    rain_warning = "Why are you even bothering going out? Stay indoors and enjoy."


weather_forecast_output = ["The temperature now is" + str(temperature) + " degrees Fahrenheit(ugh) and " + str(summary) +" Today will be " + str(temp_feeling) + " with an expected high of " + str(high_temp) + " degrees Fahrenheit and an expected low of " + str(low_temp) + " degrees Fahrenheit. It's going to rain with a probability of " + str(rain_likelihood) + " percent so " + str(rain_warning)]

def date_in_words(date):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    import dateutil.parser
    date = dateutil.parser.parse(date)
    return months[date.month - 1]

def day_in_number(day):
    import dateutil.parser
    day = dateutil.parser.parse(day)
    return day.day

def year_in_number(year):
    import dateutil.parser
    year = dateutil.parser.parse(year)
    return year.year

import time
datestring = time.strftime("%Y-%m-%d-%H-%M")

date_in_words(datestring)
day_in_number(datestring)
year_in_number(datestring)

final_date = [date_in_words(datestring), day_in_number(datestring), "-", year_in_number(datestring)]
specified_subjectline = ["8AM weather forecast:", final_date]


import requests
key = 'key-3a2bbee3565fa5844cd5408b67f877a1'
recipient = 'harshadevulapalli@outlook.com'


request_url = 'https://api.mailgun.net/v3/sandbox9157d0b51bda4555b4b664c238b56e3a.mailgun.org/messages'
request = requests.post(request_url, auth=('api', key), data={
    'from': 'postmaster@sandbox9157d0b51bda4555b4b664c238b56e3a.mailgun.org',
    'to': recipient,
    'subject': specified_subjectline,
    'text': weather_forecast_output
})
