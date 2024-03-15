import matplotlib.pyplot as plt

class BezierCurve:
    def __init__(self):
        self.bezier_points = []
        self.midpoints = []

    def create_bezier(self, ctrl1, ctrl2, ctrl3):
        self.bezier_points = []
        self.midpoints = []
        self.bezier_points.append(ctrl1)  # add the first control point
        self.populate_bezier_points(ctrl1, ctrl2, ctrl3, 0)
        self.bezier_points.append(ctrl3)  # add the last control point

    def populate_bezier_points(self, ctrl1, ctrl2, ctrl3, current_iteration):
        iterations = 10  # You can adjust this value as per your requirement
        if current_iteration < iterations:
            # calculate next mid points
            mid_point1 = self.mid_point(ctrl1, ctrl2)
            mid_point2 = self.mid_point(ctrl2, ctrl3)
            mid_point3 = self.mid_point(mid_point1, mid_point2)
            # the next control point
            self.midpoints.append(mid_point3)  # store the midpoint
            current_iteration += 1
            self.populate_bezier_points(ctrl1, mid_point1, mid_point3, current_iteration)  # left branch
            self.bezier_points.append(mid_point3)  # add the next control point
            self.populate_bezier_points(mid_point3, mid_point2, ctrl3, current_iteration)  # right branch

    def mid_point(self, control_point1, control_point2):
        return ((control_point1[0] + control_point2[0]) / 2, (control_point1[1] + control_point2[1]) / 2)

    def plot_curve_with_midpoints(self):
        x = [point[0] for point in self.bezier_points]
        y = [point[1] for point in self.bezier_points]
        plt.plot(x, y, marker='o', label='Bezier Curve')
        
        mid_x = [point[0] for point in self.midpoints]
        mid_y = [point[1] for point in self.midpoints]
        plt.scatter(mid_x, mid_y, color='red', label='Midpoints')
        
        plt.title('Bezier Curve with Midpoints')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()

# Example usage:
if __name__ == "__main__":
    bezier = BezierCurve()
    ctrl1 = (100, 300)
    ctrl2 = (400, 50)
    ctrl3 = (700, 300)
    bezier.create_bezier(ctrl1, ctrl2, ctrl3)
    bezier.plot_curve_with_midpoints()
