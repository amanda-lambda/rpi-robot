import explorerhat


class Robot():
    def __init__(self, left_id, right_id, left_invert, right_invert, power):
        """
        Create an instance of a two-motor drive robot. 
        Differential steering by joystick control.

        Params:
            left_id (int): ID of the left motor [1, 2].
            right_id (int): ID of the right motor [1, 2].
            left_invert (bool): flag to reverse direction of left motor
            right_invert (bool): flag to reverse direction of right motor
            max_power (int): Maximum power of motors, ranges from [0, 100]
        """
        # Set the motors
        motors = {1: explorerhat.motor.one, 2: explorerhat.motor.two}
        self.left = motors[left_id]
        self.right = motors[right_id]

        # Invert motor directions if needed
        if self.left_invert:
            self.left.invert()
        if self.right_invert:
            self.right.invert()

        # Maximum motor power
        self.power = max_power

    
    def stop(self):
        """
        Stop robot motors.
        """
        self.left.stop()
        self.right.stop()


    def drive(self, joy_x, joy_y):
        """
        Drive robot according to joystick inputs.

        Params:
            joy_x: joystick displacement on x-axis, with the range
                from (left, right) corresponding to (-1,1)
            joy_y: up/down joystick displacement, with the range 
                from (down, up) corresponding to (-1,1)
        """
        motor_l, motor_r = calculate_drive(joy_x, joy_y)
        if motor_l == 0:
            self.left.stop()
        elif motor_l > 0:
            self.left.forwards(motor_l)
        else: # motor_l < 0:
            self.left.backwards(motor_l)
        
        if motor_r == 0:
            self.right.stop()
        elif motor_r > 0:
            self.right.forwards(motor_r)
        else: # motor_l < 0:
            self.right.backwards(motor_r)

    
    def calculate_drive(self, joy_x, joy_y):
        """
        Translate joystick inputs into motor drives.
        http://home.kendra.com/mauser/Joystick.html

        Params:
            joy_x: joystick displacement on x-axis, with the range
                from (left, right) corresponding to (-1,1)
            joy_y: up/down joystick displacement, with the range 
                from (down, up) corresponding to (-1,1)
        
        Returns: 
            motor_l: power to left motor, range (-self.power, self.power)
            motor_r: power to right motor, range (-self.power, self.power)
        """
        # Intermediate values
        v = (1 - abs(joy_x)) * joy_y + joy_y
        w = (1 - abs(joy_y)) * joy_x + joy_x

        # Motor values
        motor_l = self.power * (v - w) / 2
        motor_r = self.power * (v + w) / 2

        return (motor_l, motor_r)
    