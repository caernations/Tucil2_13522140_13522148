import time
import matplotlib.pyplot as plt
import numpy as np

class BezierCurve:
    def __init__(self):
        self.bezier_points = []

    def create_bezier(self, ctrl1, ctrl2, ctrl3, iterations):
        self.bezier_points = [ctrl1]  # Add the first control point
        t_values = np.linspace(0, 1, (2 ** iterations) + 1)  # Generate n+2 t values to include the endpoints
        for t in t_values[1:-1]:  # Skip the first and last t values to avoid duplicating the control points
            # Apply the Bezier formula for a quadratic curve directly
            x = (1 - t) ** 2 * ctrl1[0] + 2 * (1 - t) * t * ctrl2[0] + t ** 2 * ctrl3[0]
            y = (1 - t) ** 2 * ctrl1[1] + 2 * (1 - t) * t * ctrl2[1] + t ** 2 * ctrl3[1]
            self.bezier_points.append((x, y))
        self.bezier_points.append(ctrl3)  # Add the last control point


    def plot_curve(self, ctrl_points):
        # Control points for plotting
        ctrl_x, ctrl_y = zip(*ctrl_points)
        
        # Plot the control points
        plt.plot(ctrl_x, ctrl_y, 'ro--', label='Control Points')  # 'ro--' denotes red color, circle markers, and dashed lines
        
        # Plot the Bezier curve
        x = [point[0] for point in self.bezier_points]
        y = [point[1] for point in self.bezier_points]
        plt.plot(x, y, 'bo-', label='Bezier Curve')  # 'bo-' denotes blue color, circle markers, and solid lines
        
        # Set the title and labels
        plt.title('Bezier Curve Brute Force')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        # Show the legend
        plt.legend()
        
        # Display the plot
        plt.show()

