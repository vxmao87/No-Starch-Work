# Link for more recent files:
# https://earthdata .nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data

from pathlib import Path
import csv
from datetime import datetime

import plotly.express as px


path = Path('Chapters_15-17/16/Exercises/16-9/world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

try:
    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    brightness_index = header_row.index('brightness')
    date_index = header_row.index('acq_date')
except ValueError:
    print("Invalid data provided!")
else:
    dates, lats, lons, brightnesses = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            lat = float(row[lat_index])
            lon = float(row[lon_index])
            brightness = float(row[brightness_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)

title = 'World Fires in 7 Days'
fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     title=title,
                     color=brightnesses,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
    )
fig.show()