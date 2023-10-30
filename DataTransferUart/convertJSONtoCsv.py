import requests
import pandas as pd

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=0"

headers = {
    'User-Agent': 'Harald'  # Replace 'YourUniqueIdentifier' with an appropriate identifier
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    properties = data['properties']
    timeseries = properties['timeseries']

    data_list = []
    for entry in timeseries:
        time = entry['time']
        temperature = entry['data']['instant']['details']['air_temperature']
        humidity = entry['data']['instant']['details']['relative_humidity']
        air_pressure_at_sea_level = entry['data']['instant']['details']['air_pressure_at_sea_level']
        data_list.append({'Time': time, 'Temperature': temperature, 'humidity': humidity, 'air_pressure_at_sea_level': air_pressure_at_sea_level})

    df = pd.DataFrame(data_list)


    df.to_csv('weather_data.csv', index=False)
    print("CSV file created: weather_data.csv")

else:
    print("Failed to retrieve data from the API.")
    print("Response status code:", response.status_code)
    print("Response content:", response.content)
