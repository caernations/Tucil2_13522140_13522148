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
    plt.figure(figsize=(10,5))
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'bo-', label='Bezier Curve')
    plt.legend()
    plt.title('Bezier Curve Divide and Conquer')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def main():
    num_points = int(input("Enter the number of control points (at least 2): "))
    control_points = []
    print("Enter the control points (x, y):")
    for i in range(num_points):
        point = input(f"Point {i+1}: ")
        x, y = map(float, point.split())
        control_points.append([x, y])

    iterations = int(input("Enter the number of iterations for curve refinement: "))

    control_points_np = np.array(control_points)
    
    curve_points = []
    bezier_divide_and_conquer(control_points_np, curve_points, iterations)
    curve_points = np.array(curve_points)
    
    plot_curve(control_points_np, curve_points)

if __name__ == "__main__":
    main()