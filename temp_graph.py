# Changes in humidity and pressure with respect to temperature

import pandas as pd
import matplotlib.pyplot as plt

# Read the data from Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Plotting the line graph
plt.figure(figsize=(10, 6))

# Temperature vs Pressure
plt.plot(df['Temp (C)'], df['Pressure (hPa)'], label='Temperature vs Pressure', color='blue')

# Temperature vs Humidity
plt.plot(df['Temp (C)'], df['Humidity (%age)'], label='Temperature vs Humidity', color='red')

# Adding labels and title
plt.xlabel('Temperature (C)')
plt.ylabel('Values')
plt.title('Temperature vs Pressure/Humidity')
plt.legend()

# Show the plot
plt.show()
