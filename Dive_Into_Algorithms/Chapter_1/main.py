import matplotlib.pyplot as plt


def ball_trajectory(x):
    location = 10 * x - 5 * (x ** 2)
    return location


def main_analytic():
    xs = [x / 100 for x in list(range(201))]
    ys = [ball_trajectory(x) for x in xs]
    plt.plot(xs, ys)
    plt.title('The Trajectory of a Thrown Ball')
    plt.xlabel('Horizontal Position of Ball')
    plt.ylabel('Vertical Position of Ball')
    plt.axhline(y=0)
    plt.show()


def main_algorithmic():
    xs = [x / 100 for x in list(range(201))]
    ys = [ball_trajectory(x) for x in xs]
    xs2 = [0.1, 2]
    ys2 = [ball_trajectory(0.1), 0]
    xs3 = [0.2, 2]
    ys3 = [ball_trajectory(0.2), 0]
    xs4 = [0.3, 2]
    ys4 = [ball_trajectory(0.3), 0]
    plt.title('The Trajectory of a Thrown Ball with Lines of Sight')
    plt.xlabel('Horizontal Position of Ball')
    plt.ylabel('Vertical Position of Ball')
    plt.plot(xs, ys, xs2, ys2, xs3, ys3, xs4, ys4)
    plt.show()


main_analytic()
main_algorithmic()
