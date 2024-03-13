import pygame

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 24)
class Screen:
    def __init__(self, x, y, text = " "):
        self.x = x
        self.y = y
        self.text = text
    def display(self, screen, color):
        text = font.render(self.text, True, color)
        textRect = text.get_rect()
        if self.y > 540:
            textRect.center = (self.x , self.y + 10)
        else:
            textRect.center = (self.x , self.y - 15)

        screen.blit(text, textRect)
        pygame.draw.circle(screen, color, (self.x, self.y), 7)
        pygame.draw.circle(screen, (120, 120, 120), (self.x, self.y), 5)