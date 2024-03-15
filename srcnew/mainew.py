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
        return ((control_point1[0] + control_point2[0]) / 2, (control_point1[1] + control_point2[1]) / 2)

    def plot_curve(self):
        x = [point[0] for point in self.bezier_points]
        y = [point[1] for point in self.bezier_points]
        plt.plot(x, y, marker='o')
        plt.title('Bezier Curve')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

# Example usage:
if __name__ == "__main__":
    bezier = BezierCurve()
    ctrl1 = tuple(map(int, input("Enter first control point as two space separated integers: ").split()))
    ctrl2 = tuple(map(int, input("Enter second control point as two space separated integers: ").split()))
    ctrl3 = tuple(map(int, input("Enter third control point as two space separated integers: ").split()))
    iterations = int(input("Enter number of iterations: "))
    bezier.create_bezier(ctrl1, ctrl2, ctrl3, iterations)
    bezier.plot_curve()
