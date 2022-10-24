import sys, pygame, time, asyncio, threading
pygame.init()

size = width, height = 1920, 1080


screen = pygame.display.set_mode(size)


bg_image = pygame.image.load("bg.png")
bg_rect = bg_image.get_rect()

screen.blit(bg_image, [100, 100])
pygame.display.flip()


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()


    screen.blit(bg_image, bg_rect)
    pygame.display.flip()






