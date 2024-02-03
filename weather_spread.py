# This code was run on raspberry pi with few tweaks that collected the actual temperature data from the BME280 sensor and saved it in the workbook called "weather".

#!/usr/bin/env python

# Import all libraries we need!
from smbus2 import SMBus
from bme280 import BME280
import time
import datetime
from datetime import date
from openpyxl import load_workbook

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

# Take first reading and discard it to avoid garbage first row
temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()
time.sleep(1)	

# Load the workbook and select the sheet
wb = load_workbook('/home/pi/Python_Code/weather.xlsx')
sheet = wb['weather_data']

try:
	while True:
		
		# Read the sensor and get date and time
		temperature = round(bme280.get_temperature(),1)
		pressure = round(bme280.get_pressure(),1)
		humidity = round(bme280.get_humidity(),1)
		today = date.today()
		now = datetime.datetime.now().time()

		# Inform the user!
		print('Adding this data to the spreadsheet:')
		print(today)
		print(now)
		print('{}*C {}hPa {}%'.format(temperature, pressure, humidity))
	
		# Append data to the spreadsheet
		row = (today, now, temperature, pressure, humidity)
		sheet.append(row)
		
		#Save the workbook
		wb.save('/home/pi/Python_Code/weather.xlsx')

		# Wait for 2 minutes seconds (120 seconds)
		time.sleep(120)

finally:
	# Make sure the workbook is saved!
	wb.save('/home/pi/Python_Code/weather.xlsx')
	
	print('Goodbye!')
	