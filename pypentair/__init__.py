#!/usr/bin/env python3

from .pump import Pump


DEBUG               = True
INSPECT_STATUS      = False
RAISE_PACKET_ERRORS = False

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


# Programs 1-4 can be programmed in all three modes.
# Programs 5-8 can only be programmed in Schedule
# mode since there are no buttons on the control panel
# for Programs 5-8.  The default setting for Programs 5-8
# is "Disabled".
#
# - Manual
#   - Set Type
#     - Set Speed
#     - Set Flow
# - Schedule
#   - Set Type
#     - Set Speed
#     - Set Flow
#   - Set Start Time
#   - Set Stop Time
# - Egg Timer
#   - Set Type
#     - Set Speed
#     - Set Flow
#   - Set Duration

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




def lookup(dict, val): # Dictionary inversion
    try:
        return list(dict.keys())[list(dict.values()).index(val)]
    except:
        return val

def pp(prop):
    return binascii.hexlify(bytearray([prop]))



import binascii
import time
