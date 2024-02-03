import pandas as pd

# Load the data from the Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Exclude datetime columns for less complexity reasons
numerical_columns = df.select_dtypes(include=['number']).columns
df_numeric = df[numerical_columns]

# Calculate mean, median, mode, etc.
mean_values = df_numeric.mean()
median_values = df_numeric.median()
mode_values = df_numeric.mode().iloc[0]
std_deviation = df_numeric.std()

# Display the results
print("Mean values:")
print(mean_values)
print("\nMedian values:")
print(median_values)
print("\nMode values:")
print(mode_values)
print("\nStandard Deviation:")
print(std_deviation)
