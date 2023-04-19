from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('Chapters_15-17/16/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Prints the index and the column header.
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='red')

# Formats plot.
ax.set_title("Daily Precipitation, 2021\nSitka", fontsize=24)
ax.set_xlabel('', fontsize=16)

# Draws the dates diagonally to avoid them from overlapping.
fig.autofmt_xdate()

ax.set_ylabel("Rainfall (In)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()