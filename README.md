# Python SDK for Pentair Pool Pumps

## Errors

|Error|Number|
|-|-|
|When attempting to set a program RPM lower than MIN_RPM|10|
|When attempting to set Program 5 to Manual (which is not allowed per the docs)|10|
|When attempting to set Program 5 to Egg Timer (which is not allowed per the docs)|10|
|When attempting to set Program 1 to Disabled (which is not allowed per the docs)|10|
|When attempting to schedule a time that isn't a real time|10|

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
