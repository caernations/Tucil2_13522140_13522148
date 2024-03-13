import pygame

def LinearCurve(positions, t, screen, color, trigger=True):
    P0_x = (1 - t) * positions[0].x
    P0_y = (1 - t) * positions[0].y

    P1_x = t * positions[1].x
    P1_y = t * positions[1].y

    curve = (P0_x + P1_x, P0_y + P1_y)
    
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, color, (positions[0].x, positions[0].y),(int(curve[0]), int(curve[1])), 5)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    elif trigger == False:
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
        return (int(curve[0]), int(curve[1]))


def quadraticCurveBruteForce(positions, t, screen, color, curve_list, green, trigger= True):

    P0_x = pow((1-t), 2) * positions[0].x
    P0_y = pow((1-t), 2) * positions[0].y

    P1_x = 2 * (1-t) * t * positions[1].x
    P1_y = 2 * (1-t) * t * positions[1].y

    P2_x = t ** 2 * positions[2].x
    P2_y = t ** 2 * positions[2].y

    curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
        first_line = [positions[0], positions[1]]
        second_line = [positions[1], positions[2]]

        a = LinearCurve(first_line, t,  screen, green, False)
        b = LinearCurve(second_line, t,  screen, green, False)

        pygame.draw.line(screen, green, a, b, 2)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))


def quadraticCurveDivideAndConquer(positions, t, screen, color, curve_list, green, trigger= True):
    P0_x = pow((1-t), 2) * positions[0].x
    P0_y = pow((1-t), 2) * positions[0].y

    P1_x = 2 * (1-t) * t * positions[1].x
    P1_y = 2 * (1-t) * t * positions[1].y

    P2_x = t ** 2 * positions[2].x
    P2_y = t ** 2 * positions[2].y

    curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
    if trigger == True:
        pygame.draw.line(screen, (0, 0, 0), (positions[0].x, positions[0].y), (positions[1].x, positions[1].y), 1)
        pygame.draw.line(screen, (0, 0, 0), (positions[1].x, positions[1].y), (positions[2].x, positions[2].y), 1)
        first_line = [positions[0], positions[1]]
        second_line = [positions[1], positions[2]]

        a = LinearCurve(first_line, t,  screen, green, False)
        b = LinearCurve(second_line, t,  screen, green, False)

        pygame.draw.line(screen, green, a, b, 2)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))