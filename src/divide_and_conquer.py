import numpy as np
import matplotlib.pyplot as plt

def is_flat_enough(control_points, iterations, current_iteration):
    if current_iteration >= iterations:
        return True
    return False

def subdivide(control_points):
    left = [control_points[0]]
    right = [control_points[-1]]
    while len(control_points) > 1:
        new_points = []
        for i in range(len(control_points) - 1):
            plt.plot([control_points[i][0], control_points[i + 1][0]], [control_points[i][1], control_points[i + 1][1]], 'yo--')
            plt.draw()
            plt.pause(0.00001)
            mid_point = (control_points[i] + control_points[i + 1]) / 2
            new_points.append(mid_point)
            if i == 0:
                left.append(mid_point)
            if i == len(control_points) - 2:
                right.append(mid_point)
        control_points = new_points

    right.reverse()
    return left, right

def bezier_divide_and_conquer(control_points, curve_points, iterations, current_iteration=0):
    if is_flat_enough(control_points, iterations, current_iteration):
        curve_points.append(control_points[0]) 
        curve_points.append(control_points[-1])
    else:
        left, right = subdivide(control_points)
        bezier_divide_and_conquer(left, curve_points, iterations, current_iteration + 1)
        bezier_divide_and_conquer(right, curve_points, iterations, current_iteration + 1)

def plot_curve(control_points, curve_points):
    # plt.figure(figsize=(10,5))
    plt.plot(control_points[:, 0], control_points[:, 1], 'co-', label='Control Points')
    plt.draw()
    plt.pause(0.05)
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'mo-', label='Bezier Curve')
    plt.draw()
    plt.pause(0.05)
    plt.legend()
    plt.title('Bezier Curve Divide and Conquer')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

