import pandas as pd

weather_data = {
    'day': ['Monday', 'Tuesday', 'Wednesday'],
    'sport': ['Tennis', 'Cricket', 'Football'],
    'temperature': [35, 45, 33],
    'windspeed': [5,5.55,6.01]
}

df = pd.DataFrame(weather_data)

# print(df)

print(df[['day', 'temperature']][df.temperature==df.temperature.max()]['temperature'])
