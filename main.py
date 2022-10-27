"""

FFFFFFFFFFFFFFFFFFFFFF    RRRRRRRRRRRRRRRRR      EEEEEEEEEEEEEEEEEEEEEE   EEEEEEEEEEEEEEEEEEEEEE              DDDDDDDDDDDDD        RRRRRRRRRRRRRRRRR      IIIIIIIIII   FFFFFFFFFFFFFFFFFFFFFF   TTTTTTTTTTTTTTTTTTTTTTT   EEEEEEEEEEEEEEEEEEEEEE   RRRRRRRRRRRRRRRRR
 F::::::::::::::::::::F    R::::::::::::::::R     E::::::::::::::::::::E   E::::::::::::::::::::E              D::::::::::::DDD     R::::::::::::::::R     I::::::::I   F::::::::::::::::::::F   T:::::::::::::::::::::T   E::::::::::::::::::::E   R::::::::::::::::R
  F::::::::::::::::::::F    R::::::RRRRRR:::::R    E::::::::::::::::::::E   E::::::::::::::::::::E              D:::::::::::::::DD   R::::::RRRRRR:::::R    I::::::::I   F::::::::::::::::::::F   T:::::::::::::::::::::T   E::::::::::::::::::::E   R::::::RRRRRR:::::R
   FF::::::FFFFFFFFF::::F    RR:::::R     R:::::R   EE::::::EEEEEEEEE::::E   EE::::::EEEEEEEEE::::E              DDD:::::DDDDD:::::D   RR:::::R     R:::::R   II::::::II   FF::::::FFFFFFFFF::::F   T:::::TT:::::::TT:::::T   EE::::::EEEEEEEEE::::E   RR:::::R     R:::::R
      F:::::F       FFFFFF      R::::R     R:::::R     E:::::E       EEEEEE     E:::::E       EEEEEE                D:::::D    D:::::D   R::::R     R:::::R     I::::I       F:::::F       FFFFFF   TTTTTT  T:::::T  TTTTTT     E:::::E       EEEEEE     R::::R     R:::::R
       F:::::F                   R::::R     R:::::R     E:::::E                  E:::::E                             D:::::D     D:::::D   R::::R     R:::::R     I::::I       F:::::F                        T:::::T             E:::::E                  R::::R     R:::::R
        F::::::FFFFFFFFFF         R::::RRRRRR:::::R      E::::::EEEEEEEEEE        E::::::EEEEEEEEEE                   D:::::D     D:::::D   R::::RRRRRR:::::R      I::::I       F::::::FFFFFFFFFF              T:::::T             E::::::EEEEEEEEEE        R::::RRRRRR:::::R
           F:::::::::::::::F         R:::::::::::::RR       E:::::::::::::::E        E:::::::::::::::E                D:::::D     D:::::D   R:::::::::::::RR       I::::I       F:::::::::::::::F              T:::::T             E:::::::::::::::E        R:::::::::::::RR
           F:::::::::::::::F         R::::RRRRRR:::::R      E:::::::::::::::E        E:::::::::::::::E                D:::::D     D:::::D   R::::RRRRRR:::::R      I::::I       F:::::::::::::::F              T:::::T             E:::::::::::::::E        R::::RRRRRR:::::R
        F::::::FFFFFFFFFF         R::::R     R:::::R     E::::::EEEEEEEEEE        E::::::EEEEEEEEEE                   D:::::D     D:::::D   R::::R     R:::::R     I::::I       F::::::FFFFFFFFFF              T:::::T             E::::::EEEEEEEEEE        R::::R     R:::::R
       F:::::F                   R::::R     R:::::R     E:::::E                  E:::::E                             D:::::D     D:::::D   R::::R     R:::::R     I::::I       F:::::F                        T:::::T             E:::::E                  R::::R     R:::::R
      F:::::F                   R::::R     R:::::R     E:::::E       EEEEEE     E:::::E       EEEEEE                D:::::D    D:::::D   R::::R     R:::::R     I::::I       F:::::F                        T:::::T             E:::::E       EEEEEE     R::::R     R:::::R
   FF:::::::FF               RR:::::R     R:::::R   EE::::::EEEEEEEE:::::E   EE::::::EEEEEEEE:::::E              DDD:::::DDDDD:::::D   RR:::::R     R:::::R   II::::::II   FF:::::::FF                    TT:::::::TT         EE::::::EEEEEEEE:::::E   RR:::::R     R:::::R
  F::::::::FF               R::::::R     R:::::R   E::::::::::::::::::::E   E::::::::::::::::::::E              D:::::::::::::::DD   R::::::R     R:::::R   I::::::::I   F::::::::FF                    T:::::::::T         E::::::::::::::::::::E   R::::::R     R:::::R
 F::::::::FF               R::::::R     R:::::R   E::::::::::::::::::::E   E::::::::::::::::::::E              D::::::::::::DDD   R::::::R     R:::::R   I::::::::I   F::::::::FF                    T:::::::::T         E::::::::::::::::::::E   R::::::R     R:::::R
FFFFFFFFFFF               RRRRRRRR     RRRRRRR   EEEEEEEEEEEEEEEEEEEEEE   EEEEEEEEEEEEEEEEEEEEEE              DDDDDDDDDDDDD   RRRRRRRR     RRRRRRR   IIIIIIIIII   FFFFFFFFFFF                    TTTTTTTTTTT         EEEEEEEEEEEEEEEEEEEEEE   RRRRRRRR     RRRRRRR




Free Drifter is a game made on Python using Pygame.
Credits: FoxyCoder

"""

# Importing libraries
import sys, pygame, time, asyncio, threading, math
from datetime import datetime, timedelta

# Initializing pygame
pygame.init()


# Setting window size
size = width, height = 2200, 1200

# Initializing fonts
pygame.font.init()

# Creating screen
screen = pygame.display.set_mode(size)

# Importing images
bg_image = pygame.image.load("./Assets/Images/bg.png")
bg_rect = bg_image.get_rect()
needle_image = pygame.image.load("./Assets/Images/Needle.png")
speedometer_image = pygame.image.load("./Assets/Images/Speedometer.png")
car_image = pygame.image.load("./Assets/Images/car_half2.png")

# Declaring classes
class Car:
    # Drifting
    # Parameter: drift - bool - if a drift is active
    # Parameter: drift_side - "left" or "right" - side of the drift
    # Parameter: drift_distance - "how much the drift should turn the car"
    # If a drift has been going on, increase drift distance, else zero it
    def __init__(self, image):
        self.x = 1100
        self.y = 600
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
        self.drift = False
        self.drift_distance = 0
        self.colliding = False

    def display(self, screen):
        direction = self.direction*-1
        direction += self.drift_distance
        self.image = pygame.transform.rotate(self.perm_image, direction)
        screen.blit(self.image, self.image.get_rect(center=[self.x, self.y]))


    def rotate(self, angle):
        #self.image = pygame.transform.rotate(self.perm_image, angle)
        self.direction -= angle
        self.direction = self.direction % 360
        #print(self.direction)

    def check_wall_collision(self, needle):
        collision = False
        if self.x > 2175:
            self.speed = 1
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 8
            self.x -= self.speed

        if self.x < 25:
            self.speed = 1
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 8
            self.x += self.speed


        if self.y > 1175:
            self.speed = 1
            self.y -= self.speed
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 8

        if self.y < 25:
            self.speed = 1
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 8
            self.y += self.speed


        if self.y < 35 or self.y > 1165 or self.x < 35 or self.x > 2165:
            collision = True

        self.colliding = collision



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

    def accelerate(self, needle):
        self.speed2 = self.speed
        if self.speed < 1:
            self.acc_mult = 1.025
        elif self.speed < 3:
            self.acc_mult = 1.025
        elif self.speed < 4:
            self.acc_mult = 1.025
        elif self.speed < 5:
            self.acc_mult = 1.005
        elif self.speed < 6:
            self.acc_mult = 1.005
        elif self.speed < 7:
            self.acc_mult = 1.001
        elif self.speed < 8:
            self.acc_mult = 1.0005
        else:
            self.acc_mult = 1.005


        if self.speed < 12:
            self.speed *= self.acc_mult
            if needle.degrees_from_0 > 1 and not self.colliding:
                needle.degrees_from_0 -= self.acc_mult/2

    def drop_speed(self, needle):
        self.speed = self.speed / 1.005
        if self.speed < 0.5:
            self.speed = 0.5
        else:
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 0.3


    def brake(self):
        self.speed = self.speed / 1.02
        if self.speed < 0.5:
            self.speed = 0.5
        else:
            if needle.degrees_from_0 < 120:
                needle.degrees_from_0 += 1
class Data_Sign:
    def __init__(self, x, y, text, color, size):
        self.x = x
        self.y = y
        self.text = text
        #self.font = font
        self.color = color
        self.font = pygame.font.SysFont(name="Calibri", size=size, bold=True)
        self.text_obj = self.font.render(self.text, True, (self.color))

    def display(self, screen):
        self.text_obj = self.font.render(self.text, True, (self.color))
        print("display", self.x, self.y)
        screen.blit(self.text_obj, ((self.x - self.text_obj.get_width() // 2, self.y - self.text_obj.get_height() // 2)))
class Speedometer:
    def __init__(self, image):
        self.x = 30
        self.y = 30
        self.image = image

    def display(self, screen):
        screen.blit(pygame.transform.scale(surface=self.image, size=(200, 200)), (self.x, self.y))
class Needle:
    def __init__(self,x ,y, image):
        self.x = x
        self.y = y
        self.degrees_from_0 = 120
        self.image = image
        self.perm_image = image

    def display(self, screen):
        self.image = pygame.transform.rotate(self.perm_image, self.degrees_from_0)
        screen.blit(self.image, self.image.get_rect(center=[self.x, self.y]))

# Declaring items
needle = Needle(x=125, y=130, image=needle_image)
car = Car(image=car_image)
speedometer = Speedometer(speedometer_image)
fps = Data_Sign(x=2150, y=30, text="FPS", color = (255, 255, 255), size=20)
speed_text = Data_Sign(x= 130, y=125, text=f"6", color=(255, 255, 255), size=80)

# Declaring car shifts
rotation_shift = 0
x_shift = 0
y_shift = 0

# FPS Mechanism
prev = datetime.utcnow()
prev_fps_switch = datetime.utcnow()
FPS = 0
fps_toggle = False




while True:
    # Getting pressed keys
    keys = pygame.key.get_pressed()

    # FPS display
    FPS += 1
    print("FPS", FPS)
    if datetime.utcnow() - prev > timedelta(seconds=1):
        prev = datetime.utcnow()
        fps.text = f"FPS: {FPS}"
        FPS = 0

    # FPS display
    if keys[pygame.K_LSUPER] and keys[pygame.K_LALT]:
        if datetime.utcnow() - prev_fps_switch > timedelta(seconds=0.3):
            prev_fps_switch = datetime.utcnow()
            print("FPS CHANGE")
            if fps_toggle == True:
                fps_toggle = False
            else:
                fps_toggle = True

    # Event fetch
    event = pygame.event.poll()

    # Checking is user closed window
    if event.type == pygame.QUIT:
        exit()



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

    # Engine control
    if keys[pygame.K_w]:
        print("Key W is pressed.", car.speed)
        car.accelerate(needle)
    else:
        car.drop_speed(needle)

    # Brakes control
    if keys[pygame.K_s]:
        print("Key S is pressed.", car.speed)
        car.brake()

    # Drifting mechanism
    if (keys[pygame.K_SPACE] and keys[pygame.K_a] or keys[pygame.K_d]) or (car.speed > 6 and keys[pygame.K_a] or keys[pygame.K_d]) and not keys[pygame.K_s]:
        print("Dirfting")
        if keys[pygame.K_a] and car.drift_distance < 50:
            car.drift_distance += 1
        elif keys[pygame.K_d] and car.drift_distance > -50:
            car.drift_distance -= 1
    else:
        if car.drift_distance > 0:
            car.drift_distance -= 1
            if car.speed > 1:
                car.speed -= 0.1
            if car.drift_distance < 0:
                car.drift_distance = 0
        elif car.drift_distance < 0:
            car.drift_distance += 1
            if car.speed > 1:
                car.speed -= 0.1

            if car.drift_distance > 0:
                car.drift_distance = 0

    # Speed dial control (not visible, deprecated)
    if int(car.speed*10) % 2 == 0:
        speed_text.text = f"{int(car.speed*10)}"

    car.check_wall_collision(needle)

    # Executing object update functions
    car.drive()
    car.rotate(rotation_shift)
    screen.blit(bg_image, bg_rect)
    car.display(screen)



    if fps_toggle:
        fps.display(screen)


    # Speed dial display (deprecated)
    # speed_text.display(screen)
    # speedometer.display(screen)
    # needle.display(screen)

    # Updating display
    pygame.display.flip()