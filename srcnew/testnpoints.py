def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def bezier_curve(control_points, current_iteration, iterations):
    all_points = []
    curve = control_points
    if current_iteration < iterations:
        all_points = [control_points[0]]
        new_curve = [curve[0]]
        for i in range(len(curve) - 1):
            if i + 2 < len(curve):
                midpoint_1 = midpoint(curve[i], curve[i+1])
                midpoint_2 = midpoint(curve[i+1], curve[i+2])
                midpoint_3 = midpoint(midpoint_1, midpoint_2)
                new_curve.extend([midpoint_1, midpoint_3])
                
            if i == len(curve) - 2 :
                new_curve.append(midpoint_2)
            
        new_curve.append(curve[-1])
        
        mid_index = len(new_curve) // 2
        
        all_points.append(new_curve[len(new_curve) // 2]) 

        current_iteration += 1
        bezier_curve(new_curve[:mid_index+1], current_iteration, iterations) #left
        bezier_curve(new_curve[mid_index:], current_iteration, iterations) #right
    all_points.append(curve[-1])    

        
    return all_points

def main():
    control_points = [(100, 300), (200, 50), (300, 300), (400, 50), (500, 300)]
    iterations = 2
    current_iteration = 0

    result = bezier_curve(control_points, current_iteration, iterations)
    print(result)

if __name__ == "__main__":
    main()
