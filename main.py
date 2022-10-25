import sys, pygame, time, asyncio, threading, math
pygame.init()

size = width, height = 2200, 1200
pygame.font.init()

screen = pygame.display.set_mode(size)


bg_image = pygame.image.load("bg.png")
bg_rect = bg_image.get_rect()

speedometer_image = pygame.image.load("Speedometer.png")
car_image = pygame.image.load("car_half.png")

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
        self.acc_mult = 1.025
        self.colliding = False

    def display(self, screen):
        self.image = pygame.transform.rotate(self.perm_image, self.direction*-1)
        screen.blit(self.image, self.image.get_rect(center=[self.x, self.y]))


    def rotate(self, angle):
        #self.image = pygame.transform.rotate(self.perm_image, angle)
        self.direction -= angle
        self.direction = self.direction % 360
        #print(self.direction)

    def check_wall_collision(self):
        self.colliding = False
        if self.x > 2170:
            self.x -= self.speed
        if self.x < 30:
            self.x += self.speed

        if self.y > 1170:
            self.y -= self.speed
        if self.y < 30:
            self.y += self.speed



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
        if self.speed < 1:
            self.acc_mult = 1.025
        elif self.speed < 3:
            self.acc_mult = 1.01
        elif self.speed < 4:
            self.acc_mult = 1.002
        elif self.speed < 5:
            self.acc_mult = 1.001
        elif self.speed < 6:
            self.acc_mult = 1.001
        elif self.speed < 7:
            self.acc_mult = 1.001
        elif self.speed < 8:
            self.acc_mult = 1.0005
        else:
            self.acc_mult = 1.005


        if self.speed < 8:
            self.speed *= self.acc_mult

    def drop_speed(self):
        self.speed = self.speed / 1.005
        if self.speed < 0.5:
            self.speed = 0.5

    def brake(self):
        self.speed = self.speed / 1.02
        if self.speed < 0.5:
            self.speed = 0.5


class Data_Sign:
    def __init__(self, x, y, text, color):
        self.x = x
        self.y = y
        self.text = text
        #self.font = font
        self.color = color
        self.font = pygame.font.Font("DS-DIGIB.ttf", 120)
        self.text_obj = self.font.render(self.text, True, (self.color))

    def display(self, screen):
        self.text_obj = self.font.render(self.text, True, (self.color))
        screen.blit(self.text_obj, ((140 - self.text_obj.get_width() // 2, 145 - self.text_obj.get_height() // 2)))

class Speedometer:
    def __init__(self, image):
        self.x = 30
        self.y = 30
        self.image = image

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

car = Car(image=car_image)
speedometer = Speedometer(speedometer_image)
speed_text = Data_Sign(x= 110, y=70, text=f"6", color=(255, 255, 255))

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
        print("Key W is pressed.", car.speed)
        car.accelerate()
    else:
        car.drop_speed()

    if keys[pygame.K_s]:
        print("Key S is pressed.", car.speed)
        car.brake()
    if int(car.speed*10) % 2 == 0:
        speed_text.text = f"{int(car.speed*10)}"

    car.check_wall_collision()

    #if car.colliding == False:
    car.drive()
    car.rotate(rotation_shift)
    screen.blit(bg_image, bg_rect)
    car.display(screen)
    speedometer.display(screen)


    if car.speed < 0.9:
        speed_text.x = 110
        speed_text.display(screen)
    else:
        speed_text.x = 80
        speed_text.display(screen)

    pygame.display.flip()






