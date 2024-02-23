import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 400, 800

if __name__ == '__main__':

    # Black screen. Text message...
    # Initialize the game

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    fps = 3

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
    # React to the user's actions.

    # Display the score

    # Close window when user quit
