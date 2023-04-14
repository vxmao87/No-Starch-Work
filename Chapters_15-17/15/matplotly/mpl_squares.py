"""
Styles available for matplotlib:
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

import matplotlib.pyplot as plt


# Data points
input_values = [index for index in range(0, 6)]
squares = [pow(num, 2) for num in range(0, 6)]

# Uses the style listed below.
plt.style.use("seaborn-v0_8-white")

# Generates the plots
fig, ax = plt.subplots()

# Plots the graph. linewidth is the thickness of the generated line.
ax.plot(input_values, squares, linewidth=3)

# Sets the chart title and axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Sets the size of the tick labels.
ax.tick_params(labelsize=14)

plt.show()