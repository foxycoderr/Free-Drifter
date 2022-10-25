import sys, pygame, time, asyncio, threading, math
pygame.init()

size = width, height = 2200, 1200


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
        self.image = image
        self.perm_image = image
        self.angle = 1
        self.direction = 360
        self.speed = 0.2
        self.antispeed = 2
        self.x_shift = 0
        self.y_shift = 0
        self.speed2 = 0

    def display(self, screen):
        self.image = pygame.transform.rotate(self.perm_image, self.direction*-1)
        screen.blit(self.image, self.image.get_rect(center=[self.x, self.y]))


    def rotate(self, angle):
        #self.image = pygame.transform.rotate(self.perm_image, angle)
        self.direction -= angle
        self.direction = self.direction % 360
        #print(self.direction)

    def drive(self):
        #print(self.direction)
        #print(self.speed)
        #self.direction = 360 - self.direction
        #print(self.direction)
        if self.speed == 0:
            self.speed = 0.2
        change_x = math.cos(math.radians(int(90 - self.direction))) * self.speed
        change_y = math.sin(math.radians(int(90 - self.direction))) * self.speed

        #print("change = ", change_x, change_y)

        #print("coords = ", self.x, self.y)
        self.x += change_x
        self.y -= change_y

        self.antispeed = 1 / self.speed

    def accelerate(self):
        self.speed2 = self.speed
        if self.speed < 12:
            self.speed *= 1.025

    def drop_speed(self):
        self.speed = self.speed / 1.01
        if self.speed < 0.5:
            self.speed = 0.5











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
        print("Key A is pressed.", car.speed)
        if car.speed > 3:
            rotation_shift = 1.5
        elif car.speed > 5:
            rotation_shift = 2
        elif car.speed > 7:
            rotation_shift = 3
        else:
            rotation_shift = 0.7
    elif keys[pygame.K_d]:
        print('key D is pressed.', car.speed)
        if car.speed > 3:
            rotation_shift = -1.5
        elif car.speed > 5:
            rotation_shift = -2
        elif car.speed > 7:
            rotation_shift = -3
        else:
            rotation_shift = -0.7
    else:
        rotation_shift = 0

    #Movement
    if keys[pygame.K_w]:
        print("Key W is pressed.")
        car.accelerate()
    else:
        car.drop_speed()

    car.drive()
    car.rotate(rotation_shift)
    screen.blit(bg_image, bg_rect)
    car.display(screen)
    pygame.display.flip()






