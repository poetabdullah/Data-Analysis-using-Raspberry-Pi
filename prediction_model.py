import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Load the data from the Excel file
df = pd.read_excel('weather.xlsx', sheet_name='weather_data')

# Target variable: Weather condition (Sunny, Cloudy, Snowy)
# Assume conditions: Sunny (0), Cloudy (1), Snowy (2)
df['Weather'] = 0  # Assume all instances are sunny
df.loc[df['Temp (C)'] < 10, 'Weather'] = 2  # Assume temperature below 10°C is snowy
df.loc[(df['Temp (C)'] >= 10) & (df['Temp (C)'] < 20), 'Weather'] = 1  # Assume temperature between 10°C and 20°C is cloudy

# Select features and target variable
features = df[['Temp (C)', 'Pressure (hPa)', 'Humidity (%age)']]
target = df['Weather']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_rep)

# Example: User input for prediction
user_temp = float(input("Enter temperature: "))
user_pressure = float(input("Enter pressure: "))
user_humidity = float(input("Enter humidity:"))

# Create a DataFrame with feature names for user input
user_input_df = pd.DataFrame([[user_temp, user_pressure, user_humidity]], columns=['Temp (C)', 'Pressure (hPa)', 'Humidity (%age)'])

# Standardize user input
user_input_scaled = scaler.transform(user_input_df)

# Make prediction for user input
user_prediction = clf.predict(user_input_scaled)[0]

# Map predicted label back to weather condition
weather_conditions = {0: 'Sunny', 1: 'Cloudy', 2: 'Snowy'}
predicted_condition = weather_conditions[user_prediction]

print(f"Predicted Weather Condition: {predicted_condition}")
