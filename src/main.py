from os import system
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
        print("  __  __  |  _ \\__  /_  /_  _ \\_  ___/    _  /    _  / / /_  ___/_ | / /  _ \\\\")
        print("  _  /_/ //  __/_  /_  / /  __/  /        / /___  / /_/ /_  /   __ |/ //  __/     ")
        print("  /_____/ \\___/_____/_/  \\___//_/         \\____/  \\__,_/ /_/    _____/ \\___/ ")
        print("                                                                                  ")
        print("  by Yasmin Farisah Salma (13522140)  &  Auralea Alvinia Syaikha (13522148)       ")

        print()
        print()
        print()
        print("  ╔═══════════════ MENU ════════════════╗")
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
            print("OPTION NOT AVAILABLE!\nPlease enter either 1 or 2.\n")
            system('pause')
            system('cls')
            
user_input = get_menu_option()

if user_input == '1':
    while True:
        try:
            num_points = int(input("Enter the number of control points ( >1 ): "))
            if num_points < 2:
                raise ValueError("Number of control points must be at least 2.")
            break
        except ValueError as e:
            print(e)
            
    control_points = []
    print("Enter the control points (x, y):")
    for i in range(num_points):
        while True:
            point = input(f"Control point {i + 1}: ")
            try:
                x, y = map(float, point.split(','))
                control_points.append([x, y])
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by comma.")
                
    while True:
        try:
            iterations = int(input("Enter the number of iterations ( >=0 ): "))
            if iterations < 0:
                raise ValueError("Number of iterations must be >= 0.")
            break
        except ValueError as e:
            print(e)

    control_points_np = np.array(control_points)
    
    curve_points = []
    start_time = time.time()
    bezier_divide_and_conquer(control_points_np, curve_points, iterations)
    curve_points = np.array(curve_points)
    end_time = time.time()
    print("\n----------------------------------------")
    print("            EXECUTION TIME              ")
    print("----------------------------------------")
    print(f"Execution time: {end_time - start_time} seconds")
    plot_curve(control_points_np, curve_points)

else:
    bezier = BezierCurve()
    while True:
        try:
            num_points = int(input("Enter the number of control points ( >1 ): "))
            if num_points < 2:
                raise ValueError("Number of control points must be at least 2.")
            break
        except ValueError as e:
            print(e)
            
    control_points = []
    print("Enter the control points (x, y):")
    for i in range(num_points):
        while True:
            point = input(f"Point {i + 1}: ")
            try:
                x, y = map(float, point.split(','))
                control_points.append([x, y])
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
                
    while True:
        try:
            iterations = int(input("Enter the number of iterations ( >= 0): "))
            if iterations < 0:
                raise ValueError("Number of iterations must be >= 0.")
            break
        except ValueError as e:
            print(e)

    start_time = time.time()
    bezier.create_bezier(control_points, iterations)
    end_time = time.time()
    print("\n----------------------------------------")
    print("            EXECUTION TIME              ")
    print("----------------------------------------")
    print(f"Execution time: {end_time - start_time} seconds")
    bezier.animate_curve(control_points, iterations)
    print()
    print()