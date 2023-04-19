import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep making random walks as long as the program is active.
while True:
    # Makes a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plots the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolors='None', s=1)

    # Both the x- and y-axes will have equal spacing between tick marks.
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='None', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None',
               s=100)
    
    # Removes the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == "n":
        break