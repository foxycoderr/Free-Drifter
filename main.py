import sys, pygame, time, asyncio, threading
pygame.init()

size = width, height = 1920, 1080


screen = pygame.display.set_mode(size)


bg_image = pygame.image.load("bg.png")
bg_rect = bg_image.get_rect()

car_image = pygame.image.load("car.png")

screen.blit(bg_image, bg_rect)
pygame.display.flip()

class Car:
    def __init__(self, image):
        self.x = 960
        self.y = 540
        self.speed = 0
        self.image = image
        self.perm_image = image
        self.angle = 1
        self.direction = 0

    def display(self, screen):
        self.image = pygame.transform.rotate(self.perm_image, self.direction)
        screen.blit(self.image, self.image.get_rect(center=[self.x, self.y]))


    def rotate(self, angle):
        #self.image = pygame.transform.rotate(self.perm_image, angle)
        self.direction += angle






car = Car(image=car_image)

rotation_shift = 0
x_shift = 0
y_shift = 0

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    keys = pygame.key.get_pressed()

    # Rotation
    if keys[pygame.K_a]:
        print("Key A is pressed.")
        rotation_shift = 2
    elif keys[pygame.K_d]:
        print('key D is pressed.')
        rotation_shift = -2
    else:
        rotation_shift = 0


    car.rotate(rotation_shift)
    screen.blit(bg_image, bg_rect)
    car.display(screen)
    pygame.display.flip()






