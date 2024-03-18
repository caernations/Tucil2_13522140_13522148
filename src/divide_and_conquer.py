import time

import matplotlib.pyplot as plt

class BezierCurve:
    def __init__(self):
        self.bezier_points = []

    def create_bezier(self, ctrl1, ctrl2, ctrl3, iterations):
        self.bezier_points = []
        self.bezier_points.append(ctrl1)  # add the first control point
        self.populate_bezier_points(ctrl1, ctrl2, ctrl3, 0, iterations)
        self.bezier_points.append(ctrl3)  # add the last control point

    def populate_bezier_points(self, ctrl1, ctrl2, ctrl3, current_iteration, iterations):
        if current_iteration < iterations:
            # calculate next mid points
            mid_point1 = self.mid_point(ctrl1, ctrl2)
            mid_point2 = self.mid_point(ctrl2, ctrl3)
            mid_point3 = self.mid_point(mid_point1, mid_point2)
            
            # the next control point
            current_iteration += 1
            self.populate_bezier_points(ctrl1, mid_point1, mid_point3, current_iteration, iterations)  # left branch
            self.bezier_points.append(mid_point3)  # add the next control point
            self.populate_bezier_points(mid_point3, mid_point2, ctrl3, current_iteration, iterations)  # right branch


    def mid_point(self, control_point1, control_point2):
        # plot a line between control_point1 and control_point2
        plt.plot([control_point1[0], control_point2[0]], [control_point1[1], control_point2[1]], 'go--', label='Midpoints' if not plt.gca().get_legend_handles_labels()[1] else '')
        plt.draw()
        plt.pause(0.04)
        return ((control_point1[0] + control_point2[0]) / 2, (control_point1[1] + control_point2[1]) / 2)
    

    def plot_curve(self, ctrl_points):
        # Control points for plotting
        ctrl_x, ctrl_y = zip(*ctrl_points)
        
        # Plot the control points
        plt.plot(ctrl_x, ctrl_y, 'ro--', label='Control Points')  # 'ko--' denotes black color, circle markers, and dashed lines
        plt.draw()
        plt.pause(0.04)  
        # Plot the Bezier curve
        x = [point[0] for point in self.bezier_points]
        y = [point[1] for point in self.bezier_points]
        plt.plot(x, y, 'bo-', label='Bezier Curve')  # 'bo-' denotes blue color, circle markers, and solid lines
        plt.draw()
        plt.pause(0.04)  
             
        # Set the title and labels
        plt.title('Bezier Curve Divide and Conquer')
        plt.xlabel('X')
        plt.ylabel('Y')
        
        # Show the legend
        plt.legend()
        
        # Display the plot
        plt.show()

if __name__ == "__main__":
    bezier = BezierCurve()
    ctrl1 = tuple(map(int, input("Enter first control point as two space separated integers: ").split()))
    ctrl2 = tuple(map(int, input("Enter second control point as two space separated integers: ").split()))
    ctrl3 = tuple(map(int, input("Enter third control point as two space separated integers: ").split()))
    iterations = int(input("Enter number of iterations: "))
    start_time = time.time()
    bezier.create_bezier(ctrl1, ctrl2, ctrl3, iterations)
    end_time = time.time()
    bezier.plot_curve([ctrl1, ctrl2, ctrl3])
    print(f"Execution time: {end_time - start_time} seconds")