from random import choice


class RandomWalk:
    """
    A class to generate random walks.
    """
    def __init__(self, num_points=5000):
        """
        Initiates attributes of a walk.
        """
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    
    def fill_walk(self):
        """
        Calculates all points in the walk.
        """

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go, and how far to go.
            """
            15-4: Changing the values in x-distance changes how long the random
            walk gets in the x-axis, and vice versa for the y-axis. Removing
            either 1 or -1 from either of the axis determines whether the random
            walk gets longer horizontally (x) or vertically (y).
            """
            # 15-5
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejects moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculates the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


    def get_step(self):
        """
        Decides which direction to go, and how far to go.
        """
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance