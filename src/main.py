import pygame
from screen import Screen
from curves import *

pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window_width, window_height = 800, 600 
screen = pygame.display.set_mode((window_width, window_height))
screen_width, screen_height = screen.get_size()

# Calculate positions relative to screen size
margin = 120  # Margin from the edge of the screen
window_height = screen_height // 2
window_width = screen_width // 2
# scale_factor = 0.75  # Scale down by 25%
# scaled_margin = margin * scale_factor
# scaled_horizontal_center = window_width * scale_factor
# scaled_vertical_center = window_height * scale_factor

clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font('freesansbold.ttf', 22)

# Colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
green = (2, 242, 102)

# Parameters
t = 0
speed = 0.002
quadratic_positions_bruteforce = [
    Screen(margin, screen_height - margin, "P0"),
    Screen(window_width // 2, window_height, "P1"),
    Screen(margin, margin, "P2")
]
quadratic_positions_divide_conquer = [
    Screen(window_width + margin, screen_height - margin, "P0"),
    Screen(window_width + (window_width // 2), window_height, "P1"),
    Screen(window_width + margin, margin, "P2")
]

quadratic_curve_bruteforce = []
quadratic_curve_divide_and_conquer = []

run = True
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
    bruteforce_text_x = (window_width // 2) - (text_bruteforce.get_width() // 2)
    divideconquer_text_x = window_width + (window_width // 2) - (text_divide_conquer.get_width() // 2)
    top_margin = 40
    text_y_position = top_margin

    screen.blit(text_bruteforce, (bruteforce_text_x, text_y_position))
    screen.blit(text_divide_conquer, (divideconquer_text_x, text_y_position))

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