import plotly.express as px

from die import Die

# Creates one D6 and one D10.
die_1 = Die(8)
die_2 = Die(8)

# Makes some rolls, and stores those results in a list.
results = []
num_rolls = 10_000_000
for roll_num in range(num_rolls):
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
title = f"Results of Rolling Two D8 Dice {num_rolls} Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customizes the chart. Makes labels appear as you hover over each bar.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html('Chapters_15-17/15/Exercises/15-6/dice_visual_d8d8.html')