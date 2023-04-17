from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('Chapters_15-17/16/weather_data/3305090.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

rain_dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        rain_dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rain_dates, rainfalls, color='green', alpha=0.5)

title = "Daily Rainfall, 2022\nSeattle, WA"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=26)
fig.autofmt_xdate()
ax.set_ylabel("Measured Precipitation (in)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
