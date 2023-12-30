import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[0].angle = 180
kit.servo[1].angle = 0

def initate():
    kit.servo[1].angle = 45