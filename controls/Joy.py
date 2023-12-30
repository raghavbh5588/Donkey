import pygame
joysticks = []

def initiateController():
    pygame.init()
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()

def awaitCommand():
    while True:
        for event in pygame.event.get():
            if event.type == 1538:
                return event.dict("Button")

def translate(value, min, max):
    range = max - min
    value = value + 1
    add = (value/2) * range
    throttle = min + add
    return throttle

def streamControls():
    streamControls.stream = True
    def buttonReading():
        for event in pygame.event.get():
            if event.type == 1539 & event.dict['button'] == 2:
                streamControls.stream = False
    def joyReading():
        while streamControls.stream:
            throttle = pygame.joystick.Joystick.get_axis(0)
            throttle = translate(throttle, 0, 180)
            steer = pygame.joystick.Joystick.get_axis(3)
            steer = translate(steer, 45, 120)
            ctrls = tuple(throttle, steer)
            #publush ctrls
    #Start loops