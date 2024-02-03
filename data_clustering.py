import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D  # Import the 3D plotting toolkit


# Load the data from the Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Select the features for clustering (temperature, pressure, humidity)
features = df[['Temp (C)', 'Pressure (hPa)', 'Humidity (%age)']]

# Standardize the features (important for K-Means)
scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_standardized)

# Visualize the clusters in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Temp (C)'], df['Pressure (hPa)'], df['Humidity (%age)'], c=df['Cluster'], cmap='viridis', edgecolors='k', alpha=0.7)
ax.set_xlabel('Temperature (Celsius)')
ax.set_ylabel('Pressure (hPa)')
ax.set_zlabel('Humidity (%age)')
ax.set_title('K-Means Clustering of Weather Data')
plt.show()
