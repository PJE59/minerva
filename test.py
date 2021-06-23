from adafruit_motorkit import MotorKit
import keyboard
kit = MotorKit()

while True:
    # try:
    #     if keyboard.is_pressed('a'):
    #         kit.motor1.throttle = -1.0
    #     elif keyboard.is_pressed('d'):
    #         kit.motor1.throttle = 1.0
    #     else:
    #         kit.motor1.throttle = 0
    # except:
    #     break
    if keyboard.is_pressed('a'):
        kit.motor1.throttle = -1.0
    elif keyboard.is_pressed('d'):
        kit.motor1.throttle = 1.0
    else:
        kit.motor1.throttle = 0