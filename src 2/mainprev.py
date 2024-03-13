import pygame
from screen import Screen
from curves import *


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


## dibawah ini kode awal sebelum di modif

# Get user input for the coordinates
P0 = list(map(int, input("Masukkan koordinat titik awal (pisahkan dengan spasi): ").split()))
P1 = list(map(int, input("Masukkan koordinat titik kontrol (pisahkan dengan spasi): ").split()))
P2 = list(map(int, input("Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split()))

# Use user input for the coordinates
quadratic_positions_bruteforce = [
    Screen(P0[0], P0[1] + screen_height // 2, "P0"),
    Screen(P1[0], P1[1] + screen_height // 2, "P1"),
    Screen(P2[0], P2[1] + screen_height // 2, "P2")
]
quadratic_positions_divide_conquer = [
    Screen(P0[0], P0[1], "P0"),
    Screen(P1[0], P1[1], "P1"),
    Screen(P2[0], P2[1], "P2")
]
quadratic_curve_bruteforce = []
quadratic_curve_divide_and_conquer = []

# # Draw the quadratic curves
# quadraticCurveBruteForce(quadratic_positions_bruteforce, t, screen, red, quadratic_curve_bruteforce, green)
# quadraticCurveDivideAndConquer(quadratic_positions_divide_conquer, t, screen, red, quadratic_curve_divide_and_conquer, green)

# # Draw the lines connecting the points if enough points exist
# if len(quadratic_curve_bruteforce) > 2:
#     pygame.draw.lines(screen, red, False, [(x, y + screen_height // 2) for x, y in quadratic_curve_bruteforce], 5)
# if len(quadratic_curve_divide_and_conquer) > 2:
#     pygame.draw.lines(screen, red, False, quadratic_curve_divide_and_conquer, 5)

# # Draw the control points for both curves
# for point in quadratic_positions_bruteforce + quadratic_positions_divide_conquer:
#     point.display(screen, black)
    
    
    
# run = True
while run:
    screen.fill(white)
    clock.tick(fps)
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
    quadraticCurveBruteForce(quadratic_positions_bruteforce, t, screen, red, quadratic_curve_bruteforce, green)
    quadraticCurveDivideAndConquer(quadratic_positions_divide_conquer, t, screen, red, quadratic_curve_divide_and_conquer, green)

    # Draw the lines connecting the points if enough points exist
    if len(quadratic_curve_bruteforce) > 2:
        pygame.draw.lines(screen, red, False, quadratic_curve_bruteforce, 5)
    if len(quadratic_curve_divide_and_conquer) > 2:
        pygame.draw.lines(screen, red, False, quadratic_curve_divide_and_conquer, 5)

    # Reset the curve once 't' completes a cycle
    if t >= 1:
        t = 0
        quadratic_curve_bruteforce.clear()
        quadratic_curve_divide_and_conquer.clear()

    # Draw the control points for both curves
    for point in quadratic_positions_bruteforce + quadratic_positions_divide_conquer:
        point.display(screen, black)

    # Increment 't' for the next frame
    t += speed
    pygame.display.update()

pygame.quit()