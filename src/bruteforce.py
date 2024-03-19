import numpy as np
from scipy.special import comb  # For binomial coefficients
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class BezierCurve:
    def __init__(self):
        self.bezier_points = []

    def create_bezier(self, control_points, iterations):
        n = len(control_points) - 1
        t_values = np.linspace(0, 1, (2 ** iterations) + 1)
        bezier_points = [self.calculate_bezier_point(t, control_points, n) for t in t_values]
        return bezier_points

    def calculate_bezier_point(self, t, control_points, n):
        x, y = 0, 0
        for i, (px, py) in enumerate(control_points):
            bernstein_poly = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
            x += px * bernstein_poly
            y += py * bernstein_poly
        return x, y

    def animate_curve(self, control_points, iterations):
        n = len(control_points) - 1
        fig, ax = plt.subplots()
        ax.set_title('Bezier Curve Animation')
        line, = ax.plot([], [], 'bo-', label='Bezier Curve')
        ctrl_x, ctrl_y = zip(*control_points)
        ax.plot(ctrl_x, ctrl_y, 'ro--', label='Control Points')
        ax.legend()

        def init():
            line.set_data([], [])
            return line,

        def update(frame):
            x, y = zip(*self.create_bezier(control_points, frame))
            line.set_data(x, y)
            return line,

        anim = FuncAnimation(fig, update, frames=range(1, iterations + 1), init_func=init, blit=True, repeat=False)
        plt.show()
        return anim