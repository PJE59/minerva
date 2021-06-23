from adafruit_motorkit import MotorKit
import pygame

pygame.init()

kit = MotorKit()

win = pygame.display.set_mode((100,100))

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      if event.type == KEYDOWN:
        key = event.key
        if key == pygame.K_a:
            kit.motor1.throttle = -0.8
        elif key == pygrame.K_d:
            kit.motor1.throttle = 0.8
        
            
             