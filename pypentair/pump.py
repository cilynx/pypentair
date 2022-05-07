from .program import Program
from .packet import Packet

ACTIONS = {
    'PING':                 0x00,
    'SET':                  0x01,
    'GET':                  0x02,
    'GET_TIME':             0x03,
    'REMOTE_CONTROL':       0x04,
    'PUMP_PROGRAM':         0x05,
    'PUMP_POWER':           0x06,
    'PUMP_STATUS':          0x07,
    '__0x08__':             0x08,
    '__0x09__':             0x09,
    '__0x0A__':             0x0A,
    'SET_DATETIME':         0x85, # Need to figure out how these align with the BROADCAST_ACTIONS, GET, and SET
    'GET_DATETIME':         0xC5,
    'GET_PUMP_STATUS':      0xC7,
    'GET_SCHEDULE_DETAILS': 0xD1,
    'GET_PUMP_CONFIG':      0xD8,
    'ERROR':                0xFF,
}

SETTING = {
    '__0x01, 0xC4__':       [0x01, 0xC4],   # 100
    '__0x01, 0xFE__':       [0x01, 0xFE],   # Changes often, generally in increments of 0x40.

    'ACTUAL_RPM':           [0x02, 0x06],
    '__0x02, 0x0A__':       [0x02, 0x0A],   # Always just a bit lower than Watts from PUMP_STATUS
    '__0x02, 0x1A__':       [0x02, 0x1A],   # [0x00, 0x00] to [0x51, 0x07] on SVRS alarm, back to 0 on reprime
    'SVRS_ALARM':           [0x02, 0x1C],   # [0x00, 0x00] to [0xff, 0xff] on SVRS alarm, back to 0 on reprime
    'CONTRAST':             [0x02, 0xBD],
    'ADDRESS':              [0x02, 0xC0],
    'TARGET_RPM':           [0x02, 0xC4],
    'RAMP':                 [0x02, 0xD1],
    'PRIME_DELAY':          [0x02, 0xD2],
    'GPM':                  [0x02, 0xE4],

    '__0x03, 0x00__':       [0x03, 0x00],   # 7860
    '__0x03, 0x16__':       [0x03, 0x16],   # 1600
    'PRIME_SENSITIVITY':    [0x03, 0x17],
    '__0x03, 0x18__':       [0x03, 0x18],   # 50    # Vacuum Flow?
    '__0x03, 0x19__':       [0x03, 0x19],   # 55    # Max Priming Flow?
    'SVRS_RESTART_TIMER':   [0x03, 0x1A],
    'SVRS_RESTART_ENABLE':  [0x03, 0x1B],
    'RUNNING_PROGRAM':      [0x03, 0x21],
    '__0x03, 0x22__':       [0x03, 0x22],   # 0
    '__0x03, 0x23__':       [0x03, 0x23],   # 0
    '__0x03, 0x24__':       [0x03, 0x24],   # 0
    '__0x03, 0x25__':       [0x03, 0x25],   # 0
    '__0x03, 0x26__':       [0x03, 0x26],   # 0
    '__0x03, 0x27__':       [0x03, 0x27],   # Through [0x03, 0x2A] -- offset by Program id.  Related to Program RPM?
    'SET_TIMER':            [0x03, 0x2B],
    '__0x03, 0x2C__':       [0x03, 0x2C],   # 2
    '__0x03, 0x2D__':       [0x03, 0x2D],   # 1
    '__0x03, 0x2E__':       [0x03, 0x2E],   # 0
    'CELSIUS':              [0x03, 0x30],
    '24_HOUR':              [0x03, 0x31],
    '__0x03, 0x34__':       [0x03, 0x34],   # 3445
    '__0x03, 0x35__':       [0x03, 0x35],   # 1115
    '__0x03, 0x36__':       [0x03, 0x36],   # 10  Error 25 if I try to set it to anything
    '__0x03, 0x37__':       [0x03, 0x37],   # 1
    '__0x03, 0x38__':       [0x03, 0x38],   # 0
    '__0x03, 0x39__':       [0x03, 0x39],   # 3445
    '__0x03, 0x3A__':       [0x03, 0x3A],   # 1115
    '__0x03, 0x3B__':       [0x03, 0x3B],   # 10  Error 25 if I try to set it to anything
    '__0x03, 0x3C__':       [0x03, 0x3C],   # 2
    '__0x03, 0x3D__':       [0x03, 0x3D],   # 0
    '__0x03, 0x3E__':       [0x03, 0x3E],   # 0

    'PROGRAM_MODE':         [0x03, 0x85],   # Through [0x03, 0x8C] -- offset by Program id
    'PROGRAM_RPM':          [0x03, 0x8D],   # Through [0x03, 0x94] -- offset by Program id
    'SCHEDULE_START':       [0x03, 0x95],   # Through [0x03, 0x9C] -- offset by Program id
    'SCHEDULE_END':         [0x03, 0x9D],   # Through [0x03, 0xA4] -- offset by Program id
    'EGG_TIMER':            [0x03, 0xA5],   # Through [0x03, 0xAC] -- offset by Program id

    'TIME_OUT_TIMER':       [0x03, 0xAD],
    'QUICK_RPM':            [0x03, 0xAE],
    'QUICK_TIMER':          [0x03, 0xAF],
    'ANTIFREEZE_ENABLE':    [0x03, 0xB0],
    'ANTIFREEZE_RPM':       [0x03, 0xB1],
    'ANTIFREEZE_TEMP':      [0x03, 0xB2],
    'PRIME_ENABLE':         [0x03, 0xB3],
    '__0x03, 0xB4__':       [0x03, 0xB4],   # 3450 Prime RPM?
    'PRIME_MAX_TIME':       [0x03, 0xB5],
    'MIN_RPM':              [0x03, 0xB6],
    'MAX_RPM':              [0x03, 0xB7],
    'PASSWORD_ENABLE':      [0x03, 0xB8],
    'PASSWORD_TIMEOUT':     [0x03, 0xB9],
    'PASSWORD':             [0x03, 0xBA],
    'PROGRAM_RPM_ALT':      [0x03, 0xBB],   # Through [0x03, 0xBE] -- offset by Program id
    '__0x03, 0xC0__':       [0x03, 0xC0],   # 1
    '__0x03, 0xC1__':       [0x03, 0xC1],   # 1
    '__0x03, 0xC2__':       [0x03, 0xC2],   # 1441
    '__0x03, 0xC3__':       [0x03, 0xC3],   # 0
    'SOFT_PRIME_COUNTER':   [0x03, 0xC4],   # Error 11 when trying to set.
}


def bytelist(x):
    return list(x.to_bytes(2, byteorder='big'))


class Pump():
    def __init__(self, id):
        # self._address = ADDRESSES["INTELLIFLO_PUMP_" + str(index)]
        self._address = 0x60 + id - 1
        self._remote_control = None
        self._program = None

    def get(self, address):
        return self.send(ACTIONS['GET'], address).idata

    def set(self, address, value):
        return self.send(ACTIONS['SET'], address + bytelist(value)).idata

    def send(self, action, data=None):
        # self.remote_control = True
        response = Packet(dst=self.address, action=action, data=data).send()
        # Should add some error checking and retry logic here -- confirm that
        # the response packet is for the same action we sent or handle the
        # error if not.
        # self.remote_control = False
        return response

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = Packet(
            dst=self.address,
            action=ACTIONS['SET'],
            data=SETTING['ADDRESS'] + bytelist(int(address))
        ).send().idata

    @property
    def ampm(self):
        return not self.send(ACTIONS['GET'], SETTING['24_HOUR']).idata

    @ampm.setter
    def ampm(self, state):
        self.send(ACTIONS['SET'], SETTING['24_HOUR'] + bytelist(not state))

    @property
    def antifreeze_enable(self):
        return self.send(ACTIONS['GET'], SETTING['ANTIFREEZE_ENABLE']).idata

    @antifreeze_enable.setter
    def antifreeze_enable(self, state):
        self.send(ACTIONS['SET'], SETTING['ANTIFREEZE_ENABLE'] + bytelist(state))

    @property
    def antifreeze_rpm(self):
        return self.send(ACTIONS['GET'], SETTING['ANTIFREEZE_RPM']).idata

    @antifreeze_rpm.setter
    def antifreeze_rpm(self, rpm):
        self.send(ACTIONS['SET'], SETTING['ANTIFREEZE_RPM'] + bytelist(rpm))

    @property
    def antifreeze_temp(self):
        return self.send(ACTIONS['GET'], SETTING['ANTIFREEZE_TEMP']).idata

    @antifreeze_temp.setter
    def antifreeze_temp(self, temp):
        self.send(ACTIONS['SET'], SETTING['ANTIFREEZE_TEMP'] + bytelist(temp))

    @property
    def celsius(self):
        return self.send(ACTIONS['GET'], SETTING['CELSIUS']).idata

    @celsius.setter
    def celsius(self, state):
        self.send(ACTIONS['SET'], SETTING['CELSIUS'] + bytelist(state))

    @property
    def contrast(self):
        return self.send(ACTIONS['GET'], SETTING['CONTRAST']).idata

    @contrast.setter
    def contrast(self, state):
        self.send(ACTIONS['SET'], SETTING['CONTRAST'] + bytelist(state))

    @property
    def dt(self):
        return self.send(ACTIONS['GET_DATETIME']).payload
        # return self.send(0x03)
    # Need to actually implement this one
    # Error 19: ?
    # Error 8: Missing parameters?
    # Error 7: Extra parameters?

    @dt.setter
    def dt(self, data):
        return self.send(ACTIONS['SET_DATETIME'], [data['hour'], data['minute'], WEEKDAYS[data['dow']], data['dom'], data['month'], data['year'], data['dst'], data['auto_dst']])

    def sync_clock(self):
        now = datetime.now()
        dow = now.weekday()
        if dow == 6:
            dow = 0
        else:
            dow = 2**dow
        print(now.hour)
        print(now.minute)
        print(dow)
        print(now.day)
        print(now.month + 1)
        print(now.strftime('%y'))
        print(int(bool(now.dst())))
        return self.send(action=133, data=[13,10,16,29,8,19,0,0])
        # return self.send(ACTIONS['SET_DATETIME'], [now.hour, now.minute, dow, now.day, now.month, int(now.strftime('%y')), int(bool(now.dst())), 1])

    @property
    def fahrenheit(self):
        return not self.celsius

    @fahrenheit.setter
    def fahrenheit(self, state):
        self.celsius = not state

    @property
    def id(self):
        return self.address - 95

    @id.setter
    def id(self, id):
        self.address = id + 95

    @property
    def max_rpm(self):
        return self.send(ACTIONS['GET'], SETTING['MAX_RPM']).idata

    @max_rpm.setter
    def max_rpm(self, rpm):
        self.send(ACTIONS['SET'], SETTING['MAX_RPM'] + bytelist(rpm))

    @property
    def min_rpm(self):
        return self.send(ACTIONS['GET'], SETTING['MIN_RPM']).idata

    @min_rpm.setter
    def min_rpm(self, rpm):
        self.send(ACTIONS['SET'], SETTING['MIN_RPM'] + bytelist(rpm))

    @property
    def mode(self):
        return self.status['mode']

    @property
    def password_enable(self):
        return self.send(ACTIONS['GET'], SETTING['PASSWORD_ENABLE']).idata

    @password_enable.setter
    def password_enable(self, state):
        self.send(ACTIONS['SET'], SETTING['PASSWORD_ENABLE'] + bytelist(state))

    @property
    def password_timeout(self):
        return self.send(ACTIONS['GET'], SETTING['PASSWORD_TIMEOUT']).idata

    @password_timeout.setter
    def password_timeout(self, timeout):
        self.send(ACTIONS['SET'], SETTING['PASSWORD_TIMEOUT'] + bytelist(timeout))

    @property
    def password(self):
        return self.send(ACTIONS['GET'], SETTING['PASSWORD']).idata

    @password.setter
    def password(self, password):
        self.send(ACTIONS['SET'], SETTING['PASSWORD'] + bytelist(password))

    @property
    def power(self):
        return self.status['run'] == 0x0A

    @power.setter
    def power(self, state):
        if DEBUG: print("Attempting to set power:", state)
        for x in range(0,120):
            response = self.send(ACTIONS['PUMP_POWER'], [PUMP_POWER[state]])
            if DEBUG: print("Desired power state:", state, "Actual power state:", self.power)
            if self.power == state:
                if DEBUG: print("Successfully set power:", state)
                return
            time.sleep(1)
        raise ValueError("Did not achieve desired PUMP_POWER state within 2-minutes.")

    @property
    def prime_enable(self):
        return self.send(ACTIONS['GET'], SETTING['PRIME_ENABLE']).idata

    @prime_enable.setter
    def prime_enable(self, state):
        self.send(ACTIONS['SET'], SETTING['PRIME_ENABLE'] + bytelist(state))

    @property
    def prime_delay(self):
        return self.send(ACTIONS['GET'], SETTING['PRIME_DELAY']).idata

    @prime_delay.setter
    def prime_delay(self, minutes):
        self.send(ACTIONS['SET'], SETTING['PRIME_DELAY'] + bytelist(minutes))

    @property
    def prime_max_time(self):
        return self.send(ACTIONS['GET'], SETTING['PRIME_MAX_TIME']).idata

    @prime_max_time.setter
    def prime_max_time(self, minutes):
        self.send(ACTIONS['SET'], SETTING['PRIME_MAX_TIME'] + bytelist(minutes))

    @property
    def prime_sensitivity(self):
        return self.send(ACTIONS['GET'], SETTING['PRIME_SENSITIVITY']).idata

    @prime_sensitivity.setter
    def prime_sensitivity(self, sensitivity):
        self.send(ACTIONS['SET'], SETTING['PRIME_SENSITIVITY'] + bytelist(sensitivity))

    @property
    def quick_rpm(self):
        return self.send(ACTIONS['GET'], SETTING['QUICK_RPM']).idata

    @quick_rpm.setter
    def quick_rpm(self, rpm):
        self.send(ACTIONS['SET'], SETTING['QUICK_RPM'] + bytelist(rpm))

    @property
    def quick_timer(self):
        minutes = self.send(ACTIONS['GET'], SETTING['QUICK_TIMER']).idata
        return [int(minutes/60), minutes % 60]

    @quick_timer.setter
    def quick_timer(self, time):
        minutes = 60 * time[0] + time[1]
        self.send(ACTIONS['SET'], SETTING['QUICK_TIMER'] + bytelist(minutes))

    @property
    def running_program(self):
        return(int(self.send(ACTIONS['GET'], SETTING['RUNNING_PROGRAM']).idata/8))

    @running_program.setter
    def running_program(self, index):
        self.send(ACTIONS['SET'], SETTING['RUNNING_PROGRAM'] + [index*8])

    def program(self, index):
        return Program(self, index)

    @property
    def programs(self):
        return [self.program(index) for index in range(1, 9)]

    @property
    def ramp(self):
        return self.send(ACTIONS['GET'], SETTING['RAMP']).idata

    @ramp.setter
    def ramp(self, rpm):
        self.send(ACTIONS['SET'], SETTING['RAMP'] + bytelist(rpm))

    @property
    def remote_control(self):
        return self._remote_control

    @remote_control.setter
    def remote_control(self, state):
        response = Packet(
                dst     = self.address,
                action  = ACTIONS['REMOTE_CONTROL'],
                data    = [REMOTE_CONTROL_MODES[state]]
                ).send()
        self._remote_control = state

    @property
    def rpm(self):
        return self.send(ACTIONS['GET'], SETTING['ACTUAL_RPM']).idata

    @property
    def trpm(self):
        return self.send(ACTIONS['GET'], SETTING['TARGET_RPM']).idata

    @trpm.setter
    def trpm(self, rpm):
        self.send(ACTIONS['SET'], SETTING['TARGET_RPM'] + bytelist(rpm))

    @rpm.setter
    def rpm(self, rpm):
        if DEBUG: print("Requesting RPM change to", rpm)
        for x in range(0,120):
            response = self.send(ACTIONS['SET'], SETTING['TARGET_RPM'] + bytelist(rpm))
            if self.rpm == self.trpm:
                if DEBUG: print("Successfully set RPM to ", rpm)
                return
            if DEBUG: print("Desired RPM:", self.trpm, "Actual RPM:", self.rpm)
            time.sleep(1)
        raise ValueError("Failed to achieve {} RPM within 2-minutes.".format(rpm))

    @property
    def running_program(self):
        return self._program

    @running_program.setter
    def running_program(self, id):
        self.send(ACTIONS['PUMP_PROGRAM'], [PUMP_PROGRAM[id]])
        self._program = id
        return self._program

    @property
    def soft_prime_counter(self):
        return self.send(ACTIONS['GET'], SETTING['SOFT_PRIME_COUNTER']).idata

    @soft_prime_counter.setter
    def soft_prime_counter(self, minutes):
        self.send(ACTIONS['SET'], SETTING['SOFT_PRIME_COUNTER'] + bytelist(minutes))

    @property
    def status(self):
        response = self.send(ACTIONS['PUMP_STATUS'])
        # We should be able to get rid of this sanity check once we implement
        # sanity checking in self.send()
        if response.action == ACTIONS['PUMP_STATUS']:
            if INSPECT_STATUS:
                response.inspect()
            data = response.data
            return {
                'run':      data[PUMP_STATUS_FIELDS['RUN']],
                'mode':     data[PUMP_STATUS_FIELDS['MODE']],
                'watts':    data[PUMP_STATUS_FIELDS['WATTS_L']] + 256 * data[PUMP_STATUS_FIELDS['WATTS_H']],
                'rpm':      data[PUMP_STATUS_FIELDS['RPM_L']] + 256 * data[PUMP_STATUS_FIELDS['RPM_H']],
                'timer':    [data[PUMP_STATUS_FIELDS['REMAINING_TIME_H']], data[PUMP_STATUS_FIELDS['REMAINING_TIME_M']]],
                'time':     [data[PUMP_STATUS_FIELDS['CLOCK_TIME_H']], data[PUMP_STATUS_FIELDS['CLOCK_TIME_M']]]
                }
        else:
            return False

    @property
    def svrs_alarm(self):
        return self.send(ACTIONS['GET'], SETTING['SVRS_ALARM']).idata

    @property
    def svrs_restart_enable(self):
        return self.send(ACTIONS['GET'], SETTING['SVRS_RESTART_ENABLE']).idata

    @svrs_restart_enable.setter
    def svrs_restart_enable(self, state):
        self.send(ACTIONS['SET'], SETTING['SVRS_RESTART_ENABLE'] + bytelist(state))

    @property
    def svrs_restart_timer(self):
        return self.send(ACTIONS['GET'], SETTING['SVRS_RESTART_TIMER']).idata

    @svrs_restart_timer.setter
    def svrs_restart_timer(self, seconds):
        self.send(ACTIONS['SET'], SETTING['SVRS_RESTART_TIMER'] + bytelist(seconds))

    @property
    def time(self):
        return list(self.send(ACTIONS['GET_TIME']).data)
        # Could also get from self.status, but that puts more bytes on the bus
        # return self.status['time']

    @property
    def timer(self):
        return self.status['timer']

    @property
    def time_out_timer(self):
        minutes = self.send(ACTIONS['GET'], SETTING['TIME_OUT_TIMER']).idata
        return [int(minutes/60), minutes % 60]

    @time_out_timer.setter
    def time_out_timer(self, time):
        minutes = 60 * time[0] + time[1]
        self.send(ACTIONS['SET'], SETTING['TIME_OUT_TIMER'] + bytelist(minutes))

    @property
    def watts(self):
        return self.status['watts']
