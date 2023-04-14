import matplotlib.pyplot as plt

from die import Die


die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for _ in range(1000)]

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.hist(results, range=(0, 13))

ax.set_title("Results of Rolling Two D6 Dice 1000 Times", fontsize=24)
ax.set_xlabel("Dice Sum", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)

ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

plt.show()

