from evdev import InputDevice


class Controller():
    def __init__(self, path):
        """
        Create an instance of a Nintendo JoyCon controller.

        Params:
            path (str): path to joycon device
        """
        self.game_pad = InputDevice(path)
        
        # Codes
        self.joy_x = 16
        self.joy_y = 17
        self.up = 307
        self.right = 305
        self.down = 304
        self.left  = 306
        self.home = 317
        self.minus = 312 


    def get_joystick(self):
        """
        Get joystick input.

        Returns:
            joy_x: joystick displacement on x-axis, with the range
                from (left, right) corresponding to (-1,1)
            joy_y: up/down joystick displacement, with the range 
                from (down, up) corresponding to (-1,1)
        """
        joy_x = self.game_pad.absinfo(self.joy_x).value
        joy_y = self.game_pad.absinfo(self.joy_y).value
        return (-joy_x, -joy_y)