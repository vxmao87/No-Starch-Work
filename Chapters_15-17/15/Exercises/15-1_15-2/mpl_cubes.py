import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [pow(x, 3) for x in x_values]

plt.style.use('seaborn')

fig_1, ax_1 = plt.subplots()
ax_1.scatter(x_values, y_values, c=y_values, cmap=plt.cm.autumn, s=10)

ax_1.set_title("Cube Numbers", fontsize=24)
ax_1.set_xlabel("Value", fontsize=14)
ax_1.set_ylabel("Cube of Value", fontsize=14)

ax_1.tick_params(labelsize=14)

ax_1.axis([0, 5100, 0, 150_000_000_000])
# ax_1.ticklabel_format(style='plain')

plt.show()