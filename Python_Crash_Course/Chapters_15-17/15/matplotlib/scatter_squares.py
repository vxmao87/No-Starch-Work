import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# # Plots a single point (2, 4)
# ax.scatter(2, 4, s=200)

# Plots a set of points using x- and y-values.
# Add colors like red or even (0, 0.8, 0) if you want to change the color of the points.
# Values close to 0 produce darker colors.
# Values close to 1 produce lighter colors.
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Sets chart title and axis labels.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Sets size of the tick labels.
ax.tick_params(labelsize=14)

# Sets the range for each axis.
ax.axis([0, 1100, 0, 1_000_000])
ax.ticklabel_format(style='plain')

# The commented out code and the line below it cannot be ran at the same time.
# Otherwise, your saved matplotlib picture will be empty!
# plt.show()
plt.savefig('Chapters_15-17/15/sample_plot.png')