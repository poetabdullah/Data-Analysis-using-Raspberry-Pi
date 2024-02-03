import pandas as pd
import matplotlib.pyplot as plt

# Assuming your DataFrame is named 'df'
# If not, replace 'df' with your DataFrame variable
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Scatter plot: Temperature vs Pressure
plt.figure(figsize=(10, 6))
plt.scatter(df['Temp (C)'], df['Pressure (hPa)'], color='blue', alpha=0.7)
plt.title('Temperature vs Pressure')
plt.xlabel('Temperature (C)')
plt.ylabel('Pressure (hPa)')
plt.grid(True)
plt.show()

# Scatter plot: Pressure vs Humidity
plt.figure(figsize=(10, 6))
plt.scatter(df['Pressure (hPa)'], df['Humidity (%age)'], color='green', alpha=0.7)
plt.title('Pressure vs Humidity')
plt.xlabel('Pressure (hPa)')
plt.ylabel('Humidity (%age)')
plt.grid(True)
plt.show()
