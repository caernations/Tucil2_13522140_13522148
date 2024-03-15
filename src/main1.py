import pygame
from screen import Screen
from curves import *
from divide_and_conquer import quadraticBezierDivideAndConquer, generate_control_points

pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width, window_height = 1000, 900
screen = pygame.display.set_mode((window_width, window_height))
screen_width, screen_height = screen.get_size()

# Calculate positions relative to screen size
margin = 100  # Margin from the edge of the screen
vertical_center = screen_height // 2
horizontal_center = screen_width // 2
scale_factor = 0.75  # Scale down by 25%
scaled_margin = margin * scale_factor
scaled_horizontal_center = horizontal_center * scale_factor
scaled_vertical_center = vertical_center * scale_factor

clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 32)

# Colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)

# Parameters
t = 0
speed = 0.002


### DARI SINI YG AKU MODIF

# Get user input for the coordinates and iterations
P0 = list(map(float, input("Masukkan koordinat titik awal (pisahkan dengan spasi): ").split()))
P1 = list(map(float, input("Masukkan koordinat titik kontrol (pisahkan dengan spasi): ").split()))
P2 = list(map(float, input("Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split()))
iterations = int(input("Masukkan jumlah iterasi: "))

# P0[1] *= -1
# P1[1] *= -1
# P2[1] *= -1

# Use user input for the coordinates
quadratic_positions_divide_conquer = [
    Screen(P0[0], (P0[1]) + screen_height // 2, f"P0 ({P0[0]}, {P0[1] *-1})"),
    Screen(P1[0], (P1[1]) + screen_height // 2, f"P1 ({P1[0]}, {P1[1] *-1})"),
    Screen(P2[0], (P2[1]) + screen_height // 2, f"P2 ({P2[0]}, {P2[1] *-1})")
    # Screen(P0[0], (P0[1]), "P0"),
    # Screen(P1[0], (P1[1]), "P1"),
    # Screen(P2[0], (P0[1]), "P2")
]


quadratic_curve_divide_and_conquer = []

# Draw the quadratic curves
# quadraticCurveBruteForce(quadratic_positions_bruteforce, t, screen, red, quadratic_curve_bruteforce, green)
quadratic_curve_divide_and_conquer = quadraticBezierDivideAndConquer(P0, P1, P2, iterations)

# Draw the lines connecting the points if enough points exist
if len(quadratic_curve_divide_and_conquer) > 2:
    pygame.draw.lines(screen, red, False, quadratic_curve_divide_and_conquer, 5)

# Draw the control points for both curves
control_points_divide_conquer = generate_control_points(P0, P1, P2, iterations)
for point in control_points_divide_conquer:
    Screen(point[0], point[1], "").display(screen, green)
    
# Draw the coordinate text for both curves
for point in quadratic_positions_divide_conquer:
    coord_text = font.render(f"{point.text}: ({point.x}, {point.y})", True, green)
    screen.blit(coord_text, (point.x - 40, point.y + 20))



### SAMPE SINI YG AKU MODIF
    
run = True
while run:
    screen.fill(white)
    clock.tick(fps)
    
    # Define the size of each cell
    cell_size = 50

    # Draw horizontal lines (rows)
    for i in range(0, screen_height, cell_size):
        pygame.draw.line(screen, black, (0, i), (screen_width, i), 1)

    # Draw vertical lines (columns)
    for i in range(0, screen_width, cell_size):
        pygame.draw.line(screen, black, (i, 0), (i, screen_height), 1)
    
    frameRate = int(clock.get_fps())
    pygame.display.set_caption("Quadratic Bezier Curves Comparison - FPS : {}".format(frameRate))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key is pygame.K_ESCAPE:
                pygame.display.set_mode((screen_width, screen_height))  # Exit fullscreen
                run = False

    # GUI Text
    text_bruteforce = font.render("BruteForce T = " + str(t)[:5], True, black)
    text_divide_conquer = font.render("DivideConquer T = " + str(t)[:5], True, black)
    bruteforce_text_x = (horizontal_center // 2) - (text_bruteforce.get_width() // 2)
    divideconquer_text_x = horizontal_center + (horizontal_center // 2) - (text_divide_conquer.get_width() // 2)
    top_margin = 40
    text_y_position_bruteforce = top_margin + screen_height // 2
    text_y_position_divide_conquer = top_margin

    screen.blit(text_bruteforce, (bruteforce_text_x, text_y_position_bruteforce))
    screen.blit(text_divide_conquer, (divideconquer_text_x, text_y_position_divide_conquer))

    # Draw the quadratic curves
    quadraticCurveDivideAndConquer(quadratic_positions_divide_conquer, t, screen, red, quadratic_curve_divide_and_conquer, green)

    # Draw the lines connecting the points if enough points exist
    if len(quadratic_curve_divide_and_conquer) > 2:
        pygame.draw.lines(screen, red, False, quadratic_curve_divide_and_conquer, 5)

    # Reset the curve once 't' completes a cycle
    if t >= 1:
        t = 0
        quadratic_curve_divide_and_conquer.clear()
        
    # Draw the control points for both curves
    for point in quadratic_positions_divide_conquer:
        point.display(screen, black)

    # Increment 't' for the next frame
    t += speed
    pygame.display.update()

pygame.quit()