from evdev import InputDevice, categorize, ecodes

joy_y = 17
joy_x = 16
up = 307
right = 305
down = 304
left  = 306
home = 317
minus = 312 

game_pad = InputDevice('/dev/input/event0')

while True():
    print(game_pad.absinfo(16).value, game_pad.absinfo(16).min, game_pad.absinfo(16).max)
    print(game_pad.absinfo(17).value, game_pad.absinfo(17).min, game_pad.absinfo(17).max)
    time.sleep(2)
Right + 
Bottom +
game_pad.capabilities(verbose=True)
{('EV_SYN', 0): [('SYN_REPORT', 0), ('SYN_CONFIG', 1), ('SYN_DROPPED', 3), ('?', 4), ('?', 20)], ('EV_KEY', 1): [(['BTN_A', 'BTN_GAMEPAD', 'BTN_SOUTH'], 304), (['BTN_B', 'BTN_EAST'], 305), ('BTN_C', 306), (['BTN_NORTH', 'BTN_X'], 307), (['BTN_WEST', 'BTN_Y'], 308), ('BTN_Z', 309), ('BTN_TL', 310), ('BTN_TR', 311), ('BTN_TL2', 312), ('BTN_TR2', 313), ('BTN_SELECT', 314), ('BTN_START', 315), ('BTN_MODE', 316), ('BTN_THUMBL', 317), ('BTN_THUMBR', 318), ('?', 319)], ('EV_ABS', 3): [(('ABS_X', 0), AbsInfo(value=32768, min=0, max=65535, fuzz=0, flat=4095, resolution=0)), (('ABS_Y', 1), AbsInfo(value=32768, min=0, max=65535, fuzz=0, flat=4095, resolution=0)), (('ABS_RX', 3), AbsInfo(value=32768, min=0, max=65535, fuzz=255, flat=4095, resolution=0)), (('ABS_RY', 4), AbsInfo(value=32768, min=0, max=65535, fuzz=255, flat=4095, resolution=0)), (('ABS_HAT0X', 16), AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0)), (('ABS_HAT0Y', 17), AbsInfo(value=0, min=-1, max=1, fuzz=0, flat=0, resolution=0))], ('EV_MSC', 4): [('MSC_SCAN', 4)]}


for event in gamepad.read_loop():

#     Listening for events (press ctrl-c to exit) ...
# time 1600884964.13867 type 3 (EV_ABS), code 17   (ABS_HAT0Y), value -1
# time 1600884964.13867 --------- SYN_REPORT --------
# time 1600884964.468594 type 3 (EV_ABS), code 16   (ABS_HAT0X), value 1
# time 1600884964.468594 --------- SYN_REPORT --------
# time 1600884964.6786  type 3 (EV_ABS), code 17   (ABS_HAT0Y), value 0
# time 1600884964.6786  --------- SYN_REPORT --------
# time 1600884964.828594 type 3 (EV_ABS), code 17   (ABS_HAT0Y), value 1
# time 1600884964.828594 --------- SYN_REPORT --------
# time 1600884965.02367 type 3 (EV_ABS), code 16   (ABS_HAT0X), value 0
# time 1600884965.02367 --------- SYN_REPORT --------
# time 1600884965.308604 type 3 (EV_ABS), code 16   (ABS_HAT0X), value -1
# time 1600884965.308604 --------- SYN_REPORT --------
# time 1600884965.578608 type 3 (EV_ABS), code 17   (ABS_HAT0Y), value 0
# time 1600884965.578608 --------- SYN_REPORT --------
# time 1600884965.908699 type 3 (EV_ABS), code 17   (ABS_HAT0Y), value -1
# time 1600884965.908699 --------- SYN_REPORT --------
# time 1600884966.14868 type 3 (EV_ABS), code 16   (ABS_HAT0X), value 0
# time 1600884966.14868 --------- SYN_REPORT --------
# time 1600884966.898723 type 3 (EV_ABS), code 17   (ABS_HAT0Y), value 0
# time 1600884966.898723 --------- SYN_REPORT --------
# time 1600884967.633747 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589828
# time 1600884967.633747 type 1 (EV_KEY), code 307  (['BTN_NORTH', 'BTN_X']), value 1
# time 1600884967.633747 --------- SYN_REPORT --------
# time 1600884967.798731 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589828
# time 1600884967.798731 type 1 (EV_KEY), code 307  (['BTN_NORTH', 'BTN_X']), value 0
# time 1600884967.798731 --------- SYN_REPORT --------
# time 1600884968.068722 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589826
# time 1600884968.068722 type 1 (EV_KEY), code 305  (['BTN_B', 'BTN_EAST']), value 1
# time 1600884968.068722 --------- SYN_REPORT --------
# time 1600884968.189953 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589826
# time 1600884968.189953 type 1 (EV_KEY), code 305  (['BTN_B', 'BTN_EAST']), value 0
# time 1600884968.189953 --------- SYN_REPORT --------
# time 1600884968.413698 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589825
# time 1600884968.413698 type 1 (EV_KEY), code 304  (['BTN_A', 'BTN_GAMEPAD', 'BTN_SOUTH']), value 1
# time 1600884968.413698 --------- SYN_REPORT --------
# time 1600884968.563706 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589825
# time 1600884968.563706 type 1 (EV_KEY), code 304  (['BTN_A', 'BTN_GAMEPAD', 'BTN_SOUTH']), value 0
# time 1600884968.563706 --------- SYN_REPORT --------
# time 1600884968.788761 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589827
# time 1600884968.788761 type 1 (EV_KEY), code 306  (BTN_C), value 1
# time 1600884968.788761 --------- SYN_REPORT --------
# time 1600884968.953695 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589827
# time 1600884968.953695 type 1 (EV_KEY), code 306  (BTN_C), value 0
# time 1600884968.953695 --------- SYN_REPORT --------
# time 1600884969.658752 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589838
# time 1600884969.658752 type 1 (EV_KEY), code 317  (BTN_THUMBL), value 1
# time 1600884969.658752 --------- SYN_REPORT --------
# time 1600884969.883786 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589838
# time 1600884969.883786 type 1 (EV_KEY), code 317  (BTN_THUMBL), value 0
# time 1600884969.883786 --------- SYN_REPORT --------
# time 1600884971.008784 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589833
# time 1600884971.008784 type 1 (EV_KEY), code 312  (BTN_TL2), value 1
# time 1600884971.008784 --------- SYN_REPORT --------
# time 1600884971.203739 type 4 (EV_MSC), code 4    (MSC_SCAN), value 589833
# time 1600884971.203739 type 1 (EV_KEY), code 312  (BTN_TL2), value 0
# time 1600884971.203739 --------- SYN_REPORT --------

for event in game_pad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event) 
        print(absevent.event.type, absevent.event.code, absevent.event.value)
    #     if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
    #         last["ABS_RZ"] = absevent.event.value

    #    if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': 
    #         last["ABS_Z"] = absevent.event.value

_input_report = bytes(gamepad.read(49))


def _get_nbit_from_input_report(offset_byte, offset_bit, nbit):
        byte = _input_report[offset_byte]
        return (byte >> offset_bit) & ((1 << nbit) - 1)


self._input_report = bytes(self._INPUT_REPORT_SIZE)

def _get_nbit_from_input_report(self, offset_byte, offset_bit, nbit):
        byte = self._input_report[offset_byte]
        return (byte >> offset_bit) & ((1 << nbit) - 1)
        
def get_stick_left_horizontal(self):
        return self._get_nbit_from_input_report(6, 0, 8) \
            | (self._get_nbit_from_input_report(7, 0, 4) << 8)

    def get_stick_left_vertical(self):
        return self._get_nbit_from_input_report(7, 4, 4) \
            | (self._get_nbit_from_input_report(8, 0, 8) << 4)

    def get_stick_right_horizontal(self):
        return self._get_nbit_from_input_report(9, 0, 8) \
            | (self._get_nbit_from_input_report(10, 0, 4) << 8)

    def get_stick_right_vertical(self):
        return self._get_nbit_from_input_report(10, 4, 4) \
            | (self._get_nbit_from_input_report(11, 0, 8) << 4)