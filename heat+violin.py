import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
file_path = 'weather.xlsx'
sheet_name = 'weather_data'
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Exclude 'Time' column from correlation calculation
correlation_columns = df.columns.difference(['Time'])

# Heatmap
correlation_matrix = df[correlation_columns].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Violin Plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Temp (C)', y='Pressure (hPa)', data=df, inner='quartile')
plt.title('Violin Plot - Temperature vs Pressure')
plt.show()
