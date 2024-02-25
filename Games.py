import pygame

WIDTH = 800
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Daniel Is The King")
surface = pygame.Surface((100, 200))
surface.fill('Red')
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    screen.blit(surface, (200, 100))
    pygame.display.update()
    clock.tick(60)
