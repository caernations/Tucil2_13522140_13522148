import os
import time
import numpy as np
import matplotlib.pyplot as plt
from divide_and_conquer import bezier_divide_and_conquer, plot_curve
from bruteforce import BezierCurve


# MENU
def get_menu_option():
    menu_options = ('1', '2')
    
    while True:
        print()
        print()
        print("  ________          _____                 _________                               ")
        print("  ___  __ )____________(_)____________    __  ____/___  ___________   ______      ")
        print("  __  __  |  _ \\__  /_  /_  _ \\_  ___/    _  /    _  / / /_  ___/_ | / /  _ \\\\    ")
        print("  _  /_/ //  __/_  /_  / /  __/  /        / /___  / /_/ /_  /   __ |/ //  __/     ")
        print("  /_____/ \\___/_____/_/  \\___//_/         \\____/  \\__,_/ /_/    _____/ \\___/      ")
        print("                                                                                  ")
        print("  by Yasmin Farisah Salma (13522140)  &  Auralea Alvinia Syaikha (13522148)       ")

        print()
        print()
        print()
        print("  ╔═════════════════ MENU ══════════════╗")
        print("  ║                                     ║")
        print("  ║  1. Create using Divide & Conquer   ║")
        print("  ║  2. Create using Brute Force        ║")
        print("  ║                                     ║")
        print("  ╚═════════════════════════════════════╝")
        print()
        user_input = input(">> Enter your option (1 / 2): ")
        
        
        
        if user_input in menu_options:
            return user_input
        else:
            print()
            print("OPTION NOT AVAILABLE! Please enter either 1 or 2.")
            time.sleep(1)
            
user_input = get_menu_option()

if user_input == '1':
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
    start_time = time.time()
    bezier_divide_and_conquer(control_points_np, curve_points, iterations)
    curve_points = np.array(curve_points)
    end_time = time.time()
    print()
    print()
    print("----------------------------------------")
    print("            EXECUTION TIME              ")
    print("----------------------------------------")
    print(f"Execution time: {end_time - start_time} seconds")
    plot_curve(control_points_np, curve_points)
    print()
    print()

else:
    bezier = BezierCurve()
    ctrl1 = tuple(map(int, input("Enter first control point as two space separated integers: ").split()))
    ctrl2 = tuple(map(int, input("Enter second control point as two space separated integers: ").split()))
    ctrl3 = tuple(map(int, input("Enter third control point as two space separated integers: ").split()))
    iterations = int(input("Enter number of iterations: "))
    start_time = time.time()
    bezier.create_bezier(ctrl1, ctrl2, ctrl3, iterations)
    end_time = time.time()
    print()
    print()
    print("----------------------------------------")
    print("            EXECUTION TIME              ")
    print("----------------------------------------")
    print(f"Execution time: {end_time - start_time} seconds")
    bezier.plot_curve([ctrl1, ctrl2, ctrl3])
    print()
    print()