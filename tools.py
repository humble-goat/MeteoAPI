import os
import datetime


def print_data(_data):
    if isinstance(_data, list):
        for counter, _part_day in enumerate(_data):
            day = datetime.datetime.fromtimestamp(_part_day['time'])
            celsius = int((_part_day['temperature'] - 32) * 5 / 9)
            wind_gust = _part_day['windGust']
            wind_speed = _part_day['windSpeed']
            humidity = _part_day['humidity'] * 100
            dew_point = int((_part_day['dewPoint'] - 32) * 5 / 9)
            summary = _part_day['summary']
            pressure = int(_part_day['pressure'])

            print(f'The forecast for {os.getenv("LOCATION").split(",")[0]} at {day.strftime("%d/%m/%Y %H:%M")}\n'
                  f'The weather seems: {summary}\n'
                  f'Temperature: {celsius}˚\n'
                  f'Dew point: {dew_point}˚\n'
                  f'Wind Gust: {wind_gust} km/h\n'
                  f'Wind Speed: {wind_speed} km/h\n'
                  f'Humidity: {humidity} %\n'
                  f'Pressure: {pressure} hPa\n'
                  )
    else:
        day = datetime.date.fromtimestamp(_data['time'])
        celsius = int((_data['temperature'] - 32) * 5 / 9)
        wind_gust = _data['windGust']
        wind_speed = _data['windSpeed']
        humidity = _data['humidity'] * 100
        dew_point = int((_data['dewPoint'] - 32) * 5 / 9)
        summary = _data['summary']
        pressure = int(_data['pressure'])

        print(f'The forecast for {os.getenv("LOCATION").split(",")[0]} at {day.strftime("%d/%m/%Y")}\n'
              f'The weather seems: {summary}\n'
              f'Temperature: {celsius}˚\n'
              f'Dew point: {dew_point}˚\n'
              f'Wind Gust: {wind_gust} km/h\n'
              f'Wind Speed: {wind_speed} km/h\n'
              f'Humidity: {humidity} %\n'
              f'Pressure: {pressure} hPa\n')
