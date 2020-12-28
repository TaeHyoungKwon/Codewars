import time

import pygame


def main(screen, label):
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                time.sleep(0, 10)
                screen = pygame.display.set_mode((250, 150))
                pygame.display.set_caption("mom")
            pygame.font.SysFont(None, 30)
            label = pygame.Surface(size=(32, 32))

        screen.fill((255, 255, 255))
        screen.blit(label, (50, 50))

        pygame.display.update()


if __name__ == "__main__":
    while True:
        pygame.font.init()
        pygame.font.SysFont(None, 30)
        pygame.display.set_caption("mom")

        screen = pygame.display.set_mode((250, 150))
        label = pygame.font.SysFont("study quickly!", 1, (0, 0, 0))

        main(screen, label)
