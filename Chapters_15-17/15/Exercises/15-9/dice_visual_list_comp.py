import plotly.express as px

from die import Die

# Creates two D6 dice.
die_1 = Die()
die_2 = Die()

# Makes some rolls, and stores those results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyzes the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualizes the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customizes the chart. Makes labels appear as you hover over each bar.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html('Chapters_15-17/15/Exercises/15-9/dice_visual_list_comp.html')