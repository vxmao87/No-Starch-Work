# Link: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

from pathlib import Path
import json

import plotly.express as px


# Reads data as a string and converts to a Python project.
path = Path('Chapters_15-17/16/Exercises/16-8/all_month.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Creates a more readable version of the data file.
path = Path('Chapters_15-17/16/Exercises/16-8/readable_all_month.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examines all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

"""
mags = each earthquake's magnitude
lons = longitude coordinates od earthquake
lats = latitude coordinates of earthquake
eq_titles = the actual earthquake
"""
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    # 16-6
    mags.append(abs(eq_dict['properties']['mag']))
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

# title = 'Global Earthquakes'
# 16-7
fig = px.scatter_geo(lat=lats, 
                     lon=lons, 
                     size=mags, 
                     title=all_eq_data['metadata']['title'],
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles
    )
fig.show()