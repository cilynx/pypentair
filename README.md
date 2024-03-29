# Python SDK for Pentair Pool Pumps

## Errors

|Error|Number|
|-|-|
|Messing up setting time|1|
|Sending H, M, and S to the time setter that only understand H, M|7|
|Sending a get or set with no parameters|8|
|Setting a program RPM lower than MIN_RPM|10|
|Setting Program 5 to Manual (which is not allowed per the docs)|10|
|Setting Program 5 to Egg Timer (which is not allowed per the docs)|10|
|Setting Program 1 to Disabled (which is not allowed per the docs)|10|
|Scheduling a time that isn't a real time|10|
|Schedule start time after playing with running schedules|25|

## Devices

|Device|Address|
|-|-|
|BROADCAST|0x0F|
|SUNTOUCH|0x10|
|EASYTOUCH|0x20|
|REMOTE_CONTROLLER|0x21|
|REMOTE_WIRELESS_CONTROLLER|0x22|
|QUICKTOUCH|0x48|
|INTELLIFLO_PUMP_1|0x60|
|INTELLIFLO_PUMP_2|0x61|
|INTELLIFLO_PUMP_3|0x62|
|INTELLIFLO_PUMP_4|0x63|
|INTELLIFLO_PUMP_5|0x64|
|INTELLIFLO_PUMP_6|0x65|
|INTELLIFLO_PUMP_7|0x66|
|INTELLIFLO_PUMP_8|0x67|
|INTELLIFLO_PUMP_9|0x68|
|INTELLIFLO_PUMP_10|0x69|
|INTELLIFLO_PUMP_11|0x6A|
|INTELLIFLO_PUMP_12|0x6B|
|INTELLIFLO_PUMP_13|0x6C|
|INTELLIFLO_PUMP_14|0x6D|
|INTELLIFLO_PUMP_15|0x6E|
|INTELLIFLO_PUMP_16|0x6F|

## Status Fields

|Device|Field|Address|
|-|-|-|
|Pump|RUN|0|
|Pump|MODE|1|
|Pump|DRIVE_STATE|2|
|Pump|WATTS_H|3|
|Pump|WATTS_L|4|
|Pump|RPM_H|5|
|Pump|RPM_L|6|
|Pump|GPM|7|
|Pump|PPC|8|
|Pump|UNKNOWN|9|
|Pump|ERROR|10|
|Pump|REMAINING_TIME_H|11|
|Pump|REMAINING_TIME_M|12|
|Pump|CLOCK_TIME_H|13|
|Pump|CLOCK_TIME_M|14|

## Actions

|Device|Action|Address|Notes|
|-|-|-|-|
|Pump|PING|0x00|
|Pump|SET|0x01|
|Pump|GET|0x02|
|Pump|GET_TIME|0x03|
|Pump|REMOTE_CONTROL|0x04|
|Pump|PUMP_PROGRAM|0x05|
|Pump|PUMP_POWER|0x06|
|Pump|PUMP_STATUS|0x07|
|Pump|SET_DATETIME|0x85|Need to figure out how these align with BROADCAST_ACTIONS, GET, and SET|
|Pump|GET_DATETIME|0xC5|
|Pump|GET_PUMP_STATUS|0xC7|
|Pump|GET_SCHEDULE_DETAILS|0xD1|
|Pump|GET_PUMP_CONFIG|0xD8|
|Pump|ERROR|0xFF|

## Settings

|Device|Scope|Setting|Address|
|-|-|-|-|
|Pump|Program 1|MODE|[0x03, 0x85]|
|Pump|Program 2|MODE|[0x03, 0x86]|
|Pump|Program 3|MODE|[0x03, 0x87]|
|Pump|Program 4|MODE|[0x03, 0x88]|
|Pump|Program 5|MODE|[0x03, 0x89]|
|Pump|Program 6|MODE|[0x03, 0x8A]|
|Pump|Program 7|MODE|[0x03, 0x8B]|
|Pump|Program 8|MODE|[0x03, 0x8C]|
|Pump|Program 1|RPM|[0x03, 0x8D]|
|Pump|Program 2|RPM|[0x03, 0x8E]|
|Pump|Program 3|RPM|[0x03, 0x8F]|
|Pump|Program 4|RPM|[0x03, 0x90]|
|Pump|Program 5|RPM|[0x03, 0x91]|
|Pump|Program 6|RPM|[0x03, 0x92]|
|Pump|Program 7|RPM|[0x03, 0x93]|
|Pump|Program 8|RPM|[0x03, 0x94]|
|Pump|Program 1|SCHEDULE_START|[0x03, 0x95]|
|Pump|Program 2|SCHEDULE_START|[0x03, 0x96]|
|Pump|Program 3|SCHEDULE_START|[0x03, 0x97]|
|Pump|Program 4|SCHEDULE_START|[0x03, 0x98]|
|Pump|Program 5|SCHEDULE_START|[0x03, 0x99]|
|Pump|Program 6|SCHEDULE_START|[0x03, 0x9A]|
|Pump|Program 7|SCHEDULE_START|[0x03, 0x9B]|
|Pump|Program 8|SCHEDULE_START|[0x03, 0x9C]|
|Pump|Program 1|SCHEDULE_END|[0x03, 0x9D]|
|Pump|Program 2|SCHEDULE_END|[0x03, 0x9E]|
|Pump|Program 3|SCHEDULE_END|[0x03, 0x9F]|
|Pump|Program 4|SCHEDULE_END|[0x03, 0xA0]|
|Pump|Program 5|SCHEDULE_END|[0x03, 0xA1]|
|Pump|Program 6|SCHEDULE_END|[0x03, 0xA2]|
|Pump|Program 7|SCHEDULE_END|[0x03, 0xA3]|
|Pump|Program 8|SCHEDULE_END|[0x03, 0xA4]|
|Pump|Program 1|EGG_TIMER|[0x03, 0xA5]|
|Pump|Program 2|EGG_TIMER|[0x03, 0xA6]|
|Pump|Program 3|EGG_TIMER|[0x03, 0xA7]|
|Pump|Program 4|EGG_TIMER|[0x03, 0xA8]|
|Pump|Program 5|EGG_TIMER|[0x03, 0xA9]|
|Pump|Program 6|EGG_TIMER|[0x03, 0xAA]|
|Pump|Program 7|EGG_TIMER|[0x03, 0xAB]|
|Pump|Program 8|EGG_TIMER|[0x03, 0xAC]|
