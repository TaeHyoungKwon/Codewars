
today_temperature, today_wind_speed = map(int, input().split())
tomorrow_temperature, tomorrow_wind_speed = map(int, input().split())


if tomorrow_temperature < 0 and tomorrow_wind_speed >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif tomorrow_temperature < today_temperature:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif tomorrow_wind_speed > today_wind_speed:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")
