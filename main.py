import config as cfg
from robot import Robot
from controller import Controller

r = Robot(
    left_id=cfg.left_id, right_id=cfg.right_id, 
    left_invert=cfg.left_invert, right_invert=cfg.right_invert, 
    power=cfg.power
)
c = Controller(path=cfg.path)

while True:
    try:
        joy_x, joy_y = c.get_joystick()
        r.drive(joy_x, joy_y)
    except:
        r.stop()

r.stop() 