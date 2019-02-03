#!/usr/bin/env python3

DEBUG = True

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
SET = 0x80
# - Add 0xC0 for Getter
GET = 0xC0

ACTIONS = {
        'ACK_MESSAGE':      0x00,
        'PUMP_PROGRAM':     0x01,
        '__0x02__':         0x02,
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
        'FILTER':  0x00,
        'MANUAL':       0x01,
        'SPEED_1':      0x02,
        'SPEED_2':      0x03,
        'SPEED_3':      0x04,
        'SPEED_4':      0x05,
        'FEATURE_1':    0x06,
        }

PUMP_PROGRAM = {
        'OFF':              0x00,
        'RPM':              [0x02, 0xC4],
        'GPM':              [0x02, 0xE4],
        'EXTERNAL':         [0x03, 0x21],
        'SET_PROGRAM_1':    [0x03, 0x27],
        'SET_PROGRAM_2':    [0x03, 0x28],
        'SET_PROGRAM_3':    [0x03, 0x29],
        'SET_PROGRAM_4':    [0x03, 0x30],
        'SET_TIMER':        [0x03, 0x31],
        }

PUMP_POWER = {
        True:   0x04,
        False:  0x10
        }

EXTERNAL_PROGRAM = {
        'STOP':     0x00,
        1:          [0x00, 0x08],
        2:          [0x00, 0x10],
        3:          [0x00, 0x18],
        4:          [0x00, 0x20],
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

class Packet():
    header             = [0xFF, 0x00, 0xFF]
    payload_header     = 0xA5
    version            = 0x00

    def __init__(self, *args, src=ADDRESSES['REMOTE_CONTROLLER'], dst=None, action=None, data=None):
        print("Packet.__init__()")
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

#        print("__init__() self.data", self.data)
        if DEBUG: self.inspect

    @property
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
        print("Packet.send(", self.bytes, ")")
        RS485.write(bytearray(self.bytes))
        return getResponse()

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
                print("Bad Checksum", read_checksum, sum(payload))
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
        return [int(sum(self.payload) / 0x100), int(sum(self.payload) % 0x100)]

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
        self.__power            = None
        self.__program          = None
        self.__program_1        = None
        self.__program_2        = None
        self.__program_3        = None
        self.__program_4        = None
        self.__remote_control   = None
        self.__rpm              = None
        self.__speed            = None

    def send(self, command, data=None):
        if data != None:
            print(("Pump.send(command=", hex(command), ", data=", data, ")"))
        else:
            print(("Pump.send(command=", hex(command), ")"))

        self.remote_control = True
        response = Packet(
                dst     = self.address,
#                dst     = ADDRESSES['BROADCAST'],
                action  = command,
                data    = data,
                ).send()
        self.remote_control = False

        return response

    @property
    def datetime(self):
        return self.send(0x03)
    #HERE
    # Error 19: ?
    # Error 8: Missing parameters
    # Error 7: Extra parameters

    @datetime.setter
    def datetime(self, data):
        return self.send(ACTIONS['SET_DATETIME'], [data['hour'], data['minute'], WEEKDAYS[data['dow']], data['dom'], data['month'], data['year'], data['dst'], data['auto_dst']])

    @property
    def time(self):
        packet = self.send(ACTIONS['GET_TIME'])
        return list(packet.data)

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, state):
        self.send(ACTIONS['PUMP_POWER'], [PUMP_POWER[state]])
        self.__power = state
        return self.__power

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, index):
        self.send(ACTIONS['PUMP_PROGRAM'], PUMP_PROGRAM['EXTERNAL'] + EXTERNAL_PROGRAM[index])
        self.__program = index
        return self.__program

    @property
    def program_1(self):
        return self.__program_1

    @program_1.setter
    def program_1(self, rpm): # TODO -- this isn't working. Need to investigate.
        response = self.send(ACTIONS['PUMP_PROGRAM'], PUMP_PROGRAM['SET_PROGRAM_1'] + [int(rpm / 0x100), int(rpm % 0x100)])
        self.__program_1 = rpm
        return self.__program_1

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
        return self.__remote_control

    @property
    def rpm(self):
        self.status()
        return self.__rpm

    @rpm.setter
    def rpm(self, rpm):
        response = self.send(ACTIONS['PUMP_PROGRAM'], PUMP_PROGRAM['RPM'] + [int(rpm / 0x100), int(rpm % 0x100)])
        if int(rpm / 0x100) == response[PACKET_FIELDS['DATA']] and int(rpm % 0x100) == response[PACKET_FIELDS['DATA']+1]:
            print("Success")
            return rpm
        else:
            print("Failure", binascii.hexlify(response))
            return False

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        response = self.send(ACTIONS['PUMP_SPEED'], [PUMP_SPEED[speed]])
        self.__speed = speed
        return self.__speed

    def status(self):
        response = self.send(ACTIONS['PUMP_STATUS'])
        if response.action == ACTIONS['PUMP_STATUS']:
            data = response.data
            self._mode = data[PUMP_STATUS_FIELDS['MODE']]
            self._watts = 0x100 * data[PUMP_STATUS_FIELDS['WATTS_H']] + data[PUMP_STATUS_FIELDS['WATTS_L']]
            self.__rpm = 0x100 * data[PUMP_STATUS_FIELDS['RPM_H']] + data[PUMP_STATUS_FIELDS['RPM_L']]
            self._hour_r, self._minute_r = data[PUMP_STATUS_FIELDS['REMAINING_TIME_H']], data[PUMP_STATUS_FIELDS['REMAINING_TIME_M']]
            self._hour_c, self._minute_c = data[PUMP_STATUS_FIELDS['CLOCK_TIME_H']], data[PUMP_STATUS_FIELDS['CLOCK_TIME_M']]
            return self._mode, self._watts, self.__rpm, self._hour_r, self._minute_r, self._hour_c, self._minute_c
        else:
            return False

def broadcastDateTime(): #TODO Actually implement this
    broadcast(BROADCAST_ACTIONS['DATE_TIME'], [15,34, 1, 10, 7, 16, 0, 1])

def setPumpTimer():
    data = PUMP_PROGRAM['SET_TIMER']
    data.extend([0x00, 0x05])
    sendPump(ACTIONS['PUMP_PROGRAM'], data)

def broadcast(command, data=None):
    dst = ADDRESSES['BROADCAST']
    RS485.write(buildPacket(dst, command, data))

def getResponse():
    print("getResponse()")
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
