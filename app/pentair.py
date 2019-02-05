#!/usr/bin/env python3
DEBUG               = True
INSPECT_STATUS      = False
RAISE_PACKET_ERRORS = False

PACKET_FIELDS = {
    'PACKET_HEADER_0':  0,
    'PACKET_HEADER_1':  1,
    'PACKET_HEADER_2':  2,
    'PAYLOAD_HEADER':   3,
    'VERSION':          4,
    'DST':              5,
    'SRC':              6,
    'ACTION':           7,
    'DATA_LENGTH':      8,
    'DATA':             9,
}

ADDRESSES = {
    'BROADCAST':                    0x0F,
    'SUNTOUCH':                     0x10,
    'EASYTOUCH':                    0x20,
    'REMOTE_CONTROLLER':            0x21,
    'REMOTE_WIRELESS_CONTROLLER':   0x22,
    'QUICKTOUCH':                   0x48,
    'INTELLIFLO_PUMP_1':            0x60,
    'INTELLIFLO_PUMP_2':            0x61,
    'INTELLIFLO_PUMP_3':            0x62,
    'INTELLIFLO_PUMP_4':            0x63,
    'INTELLIFLO_PUMP_5':            0x64,
    'INTELLIFLO_PUMP_6':            0x65,
    'INTELLIFLO_PUMP_7':            0x66,
    'INTELLIFLO_PUMP_8':            0x67,
    'INTELLIFLO_PUMP_9':            0x68,
    'INTELLIFLO_PUMP_10':           0x69,
    'INTELLIFLO_PUMP_11':           0x6A,
    'INTELLIFLO_PUMP_12':           0x6B,
    'INTELLIFLO_PUMP_13':           0x6C,
    'INTELLIFLO_PUMP_14':           0x6D,
    'INTELLIFLO_PUMP_15':           0x6E,
    'INTELLIFLO_PUMP_16':           0x6F
}

SRC = ADDRESSES['REMOTE_CONTROLLER']

BROADCAST_ACTIONS = {
    'ACK_MESSAGE':                  0x01,

    'CONTROLLER_STATUS':            0x02,
    'DELAY_CANCEL':                 0x03,
    'DATE_TIME':                    0x05,
    'PUMP_STATUS':                  0x07,
    'HEATER_TEMPERATURE_STATUS':    0x08,
    'CUSTOM_NAMES':                 0x0A,
    'CIRCUIT_NAMES':                0x0B,
    'HEATER_PUMP_STATUS':           0x10,
    'SCHEDULE_DETAILS':             0x11,
    'INTELLICHEM':                  0x12,
    'INTELLIFLO_SPA_SIDE_CONTROL':  0x16,
    'PUMP_STATUS_2':                0x17, # Differentation with 0x07?
    'PUMP_CONFIG':                  0x18,
    'INTELLICHLOR_STATUS':          0x19,
    'PUMP_CONFIG_EXTENDED':         0x1B,
    'VALVE_STATUS':                 0x1D,
    'HIGH_SPEED_VALVE_CIRCUITS':    0x1E,
    'IS4_IS10':                     0x20,
    'INTELLIFLO_SPA_SIDE_REMOTE':   0x21,
    'HEATER_PUMP_STATUS':           0x22,
    'DELAY_STATUS':                 0x23,
    'LIGHT_GROUPS':                 0x27,
    'HEAT_SETTINGS':                0x28,

    'SET_COLOR':                    0x60,
}

# For STATUS (0x02) through HEAT_SETTINGS (0x28):
# - Add 0x80 for Setter
#SET = 0x80
# - Add 0xC0 for Getter
#GET = 0xC0

ACTIONS = {
    'ACK_MESSAGE':      0x00,
    'SET':              0x01,
    'GET':              0x02,
    'GET_TIME':         0x03,
    'REMOTE_CONTROL':   0x04,
    'PUMP_SPEED':       0x05,
    'PUMP_POWER':       0x06,
    'PUMP_STATUS':      0x07,
    '__0x08__':         0x08,
    '__0x09__':         0x09,
    '__0x0A__':         0x0A,
    'SET_DATETIME':     0x85, # Need to figure out how these align with the BROADCAST_ACTIONS, GET, and SET
    'GET_DATETIME':     0xC5,
    'GET_PUMP_STATUS':  0xC7,
    'GET_SCHEDULE_DETAILS': 0xD1,
    'GET_PUMP_CONFIG':  0xD8,
    'ERROR':            0xFF,
}

PUMP_STATUS_FIELDS = {
    'RUN':                  0,
    'MODE':                 1,
    'DRIVE_STATE':          2,
    'WATTS_H':              3,
    'WATTS_L':              4,
    'RPM_H':                5,
    'RPM_L':                6,
    'GPM':                  7,
    'PPC':                  8,
    'UNKNOWN':              9,
    'ERROR':                10,
    'REMAINING_TIME_H':     11,
    'REMAINING_TIME_M':     12,
    'CLOCK_TIME_H':         13,
    'CLOCK_TIME_M':         14
}

PUMP_SPEED = {
    'SPEED_1':      0x02,
    'SPEED_2':      0x03,
    'SPEED_3':      0x04,
    'SPEED_4':      0x05,
    'QUICK_CLEAN':  0x0a,
    'TIME_OUT':     0x0b,
}

PROGRAM = [         # Addresses for getting and setting Program RPMs
    None,
    [0x03, 0x27],   # Program 1
    [0x03, 0x28],   # Program 2
    [0x03, 0x29],   # Program 3
    [0x03, 0x2a],   # Program 4
    [0x03, 0xbb],   # Seems to be an alias of 0x27
    [0x03, 0xbc],   # Seems to be an alias of 0x28
    [0x03, 0xbd],   # Seems to be an alias of 0x29
    [0x03, 0xbe],   # Seems to be an alias of 0x30
]

RUN_PROGRAM = {                 # Addresses for running Programs
    'STOP': [0x00],
    '1':    [0x00, 0x08],   # Program 1
    '2':    [0x00, 0x10],   # Program 2
    '3':    [0x00, 0x18],   # Program 3
    '4':    [0x00, 0x20],   # Program 4
}

MODE = {
    'OFF':              0x00,
    'RPM':              [0x02, 0xC4],
    'GPM':              [0x02, 0xE4],
    'RUN_PROGRAM':      [0x03, 0x21],
    'SET_TIMER':        [0x03, 0x2b],
}

PUMP_POWER = {
    False:  0x04,
    True:   0x0A,
}

REMOTE_CONTROL_MODES = {
    False:  0x00,
    True:   0xff
}

WEEKDAYS = {
    'SUNDAY':       1,
    'MONDAY':       2,
    'TUESDAY':      4,
    'WEDNESDAY':    8,
    'THURSDAY':     16,
    'FRIDAY':       32,
    'SATURDAY':     64,
}

# SCHEDULE_DAYS are WEEKDAYS + 128 as the most significant bit of the mask is always high

def bytelist(x):
    return list(x.to_bytes(2, byteorder='big'))

def lookup(dict, val): # Dictionary inversion
    try:
        return list(dict.keys())[list(dict.values()).index(val)]
    except:
        return val

def pp(prop):
    return binascii.hexlify(bytearray([prop]))

import serial
RS485 = serial.Serial(
        port        = '/dev/ttyUSB0',
        baudrate    = 9600,
        parity      = serial.PARITY_NONE,
        stopbits    = serial.STOPBITS_ONE,
        bytesize    = serial.EIGHTBITS,
        timeout     = 1
        )

import binascii
import time

class Packet():
    header             = [0xFF, 0x00, 0xFF]
    payload_header     = 0xA5
    version            = 0x00

    def __init__(self, *args, src=ADDRESSES['REMOTE_CONTROLLER'], dst=None, action=None, data=None):
        if args is not ():
            self.bytes      = args
        else:
            self.dst        = dst
            self.action     = action
            self.src        = src
            if isinstance(data, int):
                self.data   = [data]
            else:
                self.data   = data


    def inspect(self):
        print("   Destination:\t\t", pp(self.dst), lookup(ADDRESSES, self.dst))
        print("   Source:\t\t", pp(self.src), lookup(ADDRESSES, self.src))
        if self.dst == ADDRESSES['BROADCAST']:
            print("   Action:\t\t", pp(self.action), lookup(BROADCAST_ACTIONS, self.action))
        else:
            print("   Action:\t\t", pp(self.action), lookup(ACTIONS, self.action))
        print("   Data Length:\t\t", pp(self.data_length))
        if self.data_length > 0:
            print("   Data:\t\t", binascii.hexlify(bytearray(self.data)))

        if self.action == ACTIONS['PUMP_STATUS'] and self.data_length > 0:
            data = self.data
#            print(data)
            run = pp(data[PUMP_STATUS_FIELDS['RUN']])
            print("      Run:\t\t", run, "ON" if run == "0a" else "OFF" if run == "04" else "")
            print("      Mode:\t\t", pp(data[PUMP_STATUS_FIELDS['MODE']]))
            print("      Drive State:\t", pp(data[PUMP_STATUS_FIELDS['DRIVE_STATE']]))
            watts_h = data[PUMP_STATUS_FIELDS['WATTS_H']]
            watts_l = data[PUMP_STATUS_FIELDS['WATTS_L']]
            print("      Watts_H:\t\t", pp(data[PUMP_STATUS_FIELDS['WATTS_H']]))
            print("      Watts_L:\t\t", pp(data[PUMP_STATUS_FIELDS['WATTS_L']]))
            print("         Watts:\t\t\t", watts_h*0x100+watts_l)
            rpm_h = data[PUMP_STATUS_FIELDS['RPM_H']]
            rpm_l = data[PUMP_STATUS_FIELDS['RPM_L']]
            print("      RPM_H:\t\t", pp(data[PUMP_STATUS_FIELDS['RPM_H']]))
            print("      RPM_L:\t\t", pp(data[PUMP_STATUS_FIELDS['RPM_L']]))
            print("         RPM:\t\t\t", rpm_h*0x100+rpm_l)
            print("      REMAINING_TIME_H:\t", data[PUMP_STATUS_FIELDS['REMAINING_TIME_H']])
            print("      REMAINING_TIME_M:\t", data[PUMP_STATUS_FIELDS['REMAINING_TIME_M']])
            print("      CLOCK_TIME_H:\t", data[PUMP_STATUS_FIELDS['CLOCK_TIME_H']])
            print("      CLOCK_TIME_M:\t", data[PUMP_STATUS_FIELDS['CLOCK_TIME_M']])

    def send(self):
        RS485.write(bytearray(self.bytes))
        if DEBUG: print()
        if DEBUG: print("Request: ", self.bytes)
        response = getResponse()
        if DEBUG: print("Response:", response.bytes)
        if response.action == self.action:
            return response
        elif response.action == ACTIONS['ERROR']:
            if RAISE_PACKET_ERRORS:
                raise ValueError("Received an ERROR {} from the pump".format(response.bytes[9]), response.bytes)
            return response
        else:
            raise ValueError("This packet goes somewhere else -- maybe we need a buffer")

    @property
    def bytes(self):
        return Packet.header + self.payload + self.checkbytes

    @bytes.setter
    def bytes(self, array):
        packet = array[0]
        if packet[0:5] != Packet.header + [Packet.payload_header] + [Packet.version]:
            packet = Packet.header + [Packet.payload_header] + [Packet.version] + packet

        payload_start   = PACKET_FIELDS['PAYLOAD_HEADER']
        data_length     = packet[PACKET_FIELDS['DATA_LENGTH']]
        data_end        = payload_start + data_length + PACKET_FIELDS['DATA'] - PACKET_FIELDS['PAYLOAD_HEADER']
        packet_length   = len(packet)

        payload = packet[payload_start:data_end]

        if packet_length > data_length + PACKET_FIELDS['DATA']:
            read_checksum = 256 * packet[-2] + packet[-1]
            if read_checksum != sum(payload):
                raise ValueError("Provided checksum does not match calculated checksum")
                return False

        self.dst        = packet[PACKET_FIELDS['DST']]
        self.src        = packet[PACKET_FIELDS['SRC']]
        self.action     = packet[PACKET_FIELDS['ACTION']]

        if data_end > PACKET_FIELDS['DATA']:
            self.data   = packet[PACKET_FIELDS['DATA']:data_end]
        else:
            self.data   = None

        return self.bytes

    @property
    def checksum(self):
        return sum(self.payload)

    @property
    def checkbytes(self):
        return bytelist(self.checksum)

    @property
    def data_length(self):
        if self.data:
            return len(self.data)
        else:
            return 0

    @property
    def payload(self):
        if self.data_length:
            return [Packet.payload_header, Packet.version, self.dst, self.src, self.action, self.data_length] + self.data
        else:
            return [Packet.payload_header, Packet.version, self.dst, self.src, self.action, self.data_length]

class Pump():
    def __init__(self, index):
        self.address            = ADDRESSES["INTELLIFLO_PUMP_" + str(index)]
        self.__program          = None
        self.__program_1        = None
        self.__program_2        = None
        self.__program_3        = None
        self.__program_4        = None
        self.__remote_control   = None
        self.__speed            = None

    def send(self, action, data=None):

        self.remote_control = True
        response = Packet(dst=self.address, action=action, data=data).send()
        # Should add some error checking and retry logic here -- confirm that
        # the response packet is for the same action we sent or handle the
        # error if not.
        self.remote_control = False

        return response

    @property
    def datetime(self):
        return self.send(0x03)
    # Need to actually implement this one
    # Error 19: ?
    # Error 8: Missing parameters?
    # Error 7: Extra parameters?

    @datetime.setter
    def datetime(self, data):
        return self.send(ACTIONS['SET_DATETIME'], [data['hour'], data['minute'], WEEKDAYS[data['dow']], data['dom'], data['month'], data['year'], data['dst'], data['auto_dst']])

    @property
    def mode(self):
        return self.status['mode']

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
        response.inspect()

        raise ValueError("Did not achieve desired PUMP_POWER state within 2-minutes.")

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, index):
        self.send(ACTIONS['SET'], MODE['RUN_PROGRAM'] + RUN_PROGRAM[index])
        self.__program = index
        return self.__program

    @property
    def program_1(self): # Don't currently know a way to read this from the pump
        return self.__program_1

    @program_1.setter
    def program_1(self, rpm):
        response = self.send(ACTIONS['SET'], PROGRAM[1] + bytelist(rpm))
        self.__program_1 = rpm
        return self.__program_1

    @property
    def program_2(self): # Don't currently know a way to read this from the pump
        return self.__program_2

    @program_2.setter
    def program_2(self, rpm):
        response = self.send(ACTIONS['SET'], PROGRAM[2] + bytelist(rpm))
        self.__program_2 = rpm
        return self.__program_2

    @property
    def program_3(self): # Don't currently know a way to read this from the pump
        return self.__program_3

    @program_3.setter
    def program_3(self, rpm):
        response = self.send(ACTIONS['SET'], PROGRAM[3] + bytelist(rpm))
        self.__program_3 = rpm
        return self.__program_3

    @property
    def program_4(self): # Don't currently know a way to read this from the pump
        return self.__program_4

    @program_4.setter
    def program_4(self, rpm):
        response = self.send(ACTIONS['SET'], PROGRAM[4] + bytelist(rpm))
        self.__program_4 = rpm
        return self.__program_4

    @property
    def remote_control(self):
        return self.__remote_control

    @remote_control.setter
    def remote_control(self, state):
        response = Packet(
                dst     = self.address,
                action  = ACTIONS['REMOTE_CONTROL'],
                data    = [REMOTE_CONTROL_MODES[state]]
                ).send()
        self.__remote_control = state

    @property
    def rpm(self):
        return self.status['rpm']

    @rpm.setter
    def rpm(self, rpm):
        if DEBUG: print("Requesting RPM change to", rpm)
        for x in range(0,120):
            response = self.send(ACTIONS['SET'], MODE['RPM'] + bytelist(rpm))
            if self.rpm == rpm:
                if DEBUG: print("Successfully set RPM to ", rpm)
                return
            if DEBUG: print("Desired RPM:", rpm, "Actual RPM:", self.rpm)
            time.sleep(1)
        response.inspect()
        raise ValueError("Failed to achieve {} RPM within 2-minutes.".format(rpm))

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        response = self.send(ACTIONS['PUMP_SPEED'], [PUMP_SPEED[speed]])
        self.__speed = speed
        return self.__speed

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
    def time(self):
        return list(self.send(ACTIONS['GET_TIME']).data)
        # Could also get from self.status, but that puts more bytes on the bus
        # return self.status['time']

    @property
    def timer(self):
        return self.status['timer']

    @property
    def watts(self):
        return self.status['watts']

def broadcastDateTime(): #TODO Actually implement this
    broadcast(BROADCAST_ACTIONS['DATE_TIME'], [15,34, 1, 10, 7, 16, 0, 1])

def setPumpTimer():
    data = MODE['SET_TIMER']
    data.extend([0x00, 0x05])
    sendPump(ACTIONS['SET'], data)

def broadcast(action, data=None):
    dst = ADDRESSES['BROADCAST']
    RS485.write(buildPacket(dst, action, data))

def getResponse():
    pbytes = []
    while True:
        for c in RS485.read():
            pbytes.append(c)
            if len(pbytes) > 4:
                pbytes.pop(0)
            if pbytes == Packet.header + [Packet.payload_header]:
                pbytes.extend(list(RS485.read(4)))              # Version, DST, SRC, Action
                data_length = ord(RS485.read())                 # Data Length
                pbytes.append(data_length)                      #
                pbytes.extend(list(RS485.read(data_length)))    # Data
                pbytes.extend(list(RS485.read(2)))              # Checksum
                return Packet(pbytes)
