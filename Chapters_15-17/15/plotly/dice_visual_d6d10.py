import plotly.express as px

from die import Die

# Creates one D6 and one D10.
die_1 = Die()
die_2 = Die(10)

# Makes some rolls, and stores those results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyzes the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizes the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customizes the chart. Makes labels appear as you hover over each bar.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html('Chapters_15-17/15/plotly/charts/dice_visual_d6d10.html')