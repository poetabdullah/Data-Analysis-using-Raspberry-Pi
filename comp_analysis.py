import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Convert 'Date' and 'Time' to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

# Combine 'Date' and 'Time' to create a new 'Datetime' column
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))

# Create subplots for temperature, pressure, and humidity
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

# Temperature subplot
ax1.plot(df['Datetime'], df['Temp (C)'], label='Temperature', marker='o', color='blue')
ax1.set_ylabel('Temperature (Celsius)')
ax1.legend()

# Pressure subplot
ax2.plot(df['Datetime'], df['Pressure (hPa)'], label='Pressure', marker='o', color='green')
ax2.set_ylabel('Pressure (hPa)')
ax2.legend()

# Humidity subplot
ax3.plot(df['Datetime'], df['Humidity (%age)'], label='Humidity', marker='o', color='orange')
ax3.set_xlabel('Datetime')
ax3.set_ylabel('Humidity (%)')
ax3.legend()

# Customize the overall plot
plt.suptitle('Comparative Analysis of Temperature, Pressure, and Humidity')
plt.show()
