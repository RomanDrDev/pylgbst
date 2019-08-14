import logging
import sys
import time

from examples.bb8joystick import joystick
from examples.bb8joystick.bb8 import BB8
from examples.bb8joystick.joystick import Joystick

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if 'pydevd' in sys.modules else logging.WARNING)

    bb8 = BB8("BB-CC13")
    joystick = Joystick()


    def set_bb_color(flag):
        if flag:
            bb8.color(255, 255, 255)
        else:
            bb8.color(0, 0, 0)


    def set_heading(angle):
        a = int(angle) % 360
        print("Angle", a)
        bb8.heading(a)


    def roll(speed, direction):
        print("Roll", speed, direction)
        if speed < 0.1:
            speed = 0
        bb8.roll(speed, direction)


    def stop(state):
        if not state:
            print("Stop")
            bb8.roll(0, 0)
            bb8.stabilize()


    try:
        joystick.on_button(set_bb_color)
        joystick.on_button(stop)
        joystick.on_rotation(set_heading)
        joystick.on_joystick(roll)
        print("All set up")

        while joystick._hub.connection.is_alive():
            time.sleep(1)
    finally:
        bb8.disconnect()
        joystick.disconnect()
