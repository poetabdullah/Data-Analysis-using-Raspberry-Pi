# Overall weather graph:

import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Combine 'Date' and 'Time' columns to create a 'Datetime' column
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))

# Plotting
plt.plot(df['Datetime'], df['Temp (C)'], marker='o', color='blue', label='Temperature')
plt.plot(df['Datetime'], df['Pressure (hPa)'], marker='o', color='red', label='Pressure')
plt.plot(df['Datetime'], df['Humidity (%age)'], marker='o', color='black', label='Humidity')

# Customize plot
plt.title('Weather Data')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()

# Adjust x-axis labels
plt.xticks(df['Datetime'], [time.strftime('%H:%M:%S') for time in df['Datetime']], rotation=45, ha='right')

# Show plot
plt.tight_layout()  # Ensure tight layout to prevent clipping of labels
plt.show()
