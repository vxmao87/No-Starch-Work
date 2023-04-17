from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('Chapters_15-17/16/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Prints the index and the column header.
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extracts dates and high temperatures.
# We use row[3] because TMAX is in index 3 in the dataset. Similarly with
# row[4].
# We will handle some errors below if one of the temp values are missing.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plots the high temps.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formats plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)

# Draws the dates diagonally to avoid them from overlapping.
fig.autofmt_xdate()

ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()