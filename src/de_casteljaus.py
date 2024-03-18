import numpy as np
import matplotlib.pyplot as plt

def de_casteljaus_algorithm(control_points, t):
    if len(control_points) == 1:
        return control_points[0]
    new_points = []
    for i in range(len(control_points) - 1):
        new_points.append((1 - t) * control_points[i] + t * control_points[i + 1])
    return de_casteljaus_algorithm(new_points, t)

def bezier_curve(control_points, iterations):
    curve_points = []
    t_values = np.linspace(0, 1, 2 ** iterations + 1)
    for t in t_values:
        curve_points.append(de_casteljaus_algorithm(control_points, t))
    return np.array(curve_points)

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

    iterations = int(input("Enter the number of iterations: "))

    control_points_np = np.array(control_points)
    
    curve_points = bezier_curve(control_points_np, iterations)
    
    plot_curve(control_points_np, curve_points)

if __name__ == "__main__":
    main()
