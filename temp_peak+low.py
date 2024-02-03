import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Convert 'Date' and 'Time' to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

# Combine 'Date' and 'Time' to create a new 'Datetime' column
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))

# Plot temperature peaks and lows
plt.figure(figsize=(12, 6))
plt.plot(df['Datetime'], df['Temp (C)'], label='Temperature', marker='o', color='blue')

# Find temperature peaks and lows
peaks = df[df['Temp (C)'] == df['Temp (C)'].max()]
lows = df[df['Temp (C)'] == df['Temp (C)'].min()]

# Mark temperature peaks and lows on the plot
plt.scatter(peaks['Datetime'], peaks['Temp (C)'], color='red', label='Temperature Peaks')
plt.scatter(lows['Datetime'], lows['Temp (C)'], color='green', label='Temperature Lows')

# Customize the plot
plt.title('Temperature Peaks and Lows')
plt.xlabel('Datetime')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.grid(True)
plt.show()
